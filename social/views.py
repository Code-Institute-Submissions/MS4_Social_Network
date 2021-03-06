from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm
from django.contrib import messages


# View for Post List
class PostListView(LoginRequiredMixin, View):
    def get_default_context(self, request) -> dict: # get posts
        posts = Post.objects.filter().order_by('-created_on')
        return {
            'post_list': posts
        }

    def get(self, request, *args, **kwargs):
        context = self.get_default_context(request)
        context["form"] = PostForm()
        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        """
        Post form
        """
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            form=PostForm()
            messages.success(request, 'Posted!')
        context = self.get_default_context(request)
        context["form"] = form
        return render(request, 'social/post_list.html', context)


# Post detail view, show a specific post only
class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        """
        Shows a specific post with comments
        """
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'social/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        """
        Post new comment
        """
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            form=CommentForm()
            messages.success(request, 'Commented!')

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'social/post_detail.html', context)


# Function for reply on comments
class CommentReplyView(LoginRequiredMixin, View):
    """
    Reply on comments, get the parent comment then comment
    """
    def post(self, request, post_pk, pk, *args, **kwargs):
        post = Post.objects.get(pk=post_pk)
        parent_comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST)
        # If form valid post comment
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.parent = parent_comment
            new_comment.save()
            form=CommentForm()
            messages.success(request, 'Commented!')

        return redirect('post-detail', pk=post_pk)


class UserIsAuthorMixin(UserPassesTestMixin):
    # If the user logged in is author of post give them access to edit post otherwise throw 403 error
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Function for user to edit post
class PostEditView(LoginRequiredMixin, UserIsAuthorMixin, UpdateView):
    """
    Get model body then edit the Post
    """
    model = Post
    fields = ['body']
    template_name = 'social/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})


# Function for user to delete post
class PostDeleteView(LoginRequiredMixin, UserIsAuthorMixin, DeleteView):
    model = Post
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')

# Function for user to delete comments
class CommentDeleteView(LoginRequiredMixin, UserIsAuthorMixin, DeleteView):
    """
    Get specific comment then delete
    """
    model = Comment
    template_name = 'social/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})


# Function for user to edit comments
class CommentEditView(LoginRequiredMixin, UserIsAuthorMixin, UpdateView):
    """
    Get specific comment then edit
    """
    model = Comment
    fields = ['comment']
    template_name = 'social/comment_edit.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})


# Function for user to view there profile
class ProfileView(View):
    """
    Get your profile and display
    """
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user

        # Show followers
        followers = profile.followers.all()
        if len(followers) == 0:
            is_following = False
        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False
        number_of_followers = len(followers)
        """
        Show user information
        """
        context = {
            'user': user,
            'profile': profile,
            'posts': Post.objects.filter(author=user).order_by('-created_on'),
            'number_of_followers': number_of_followers,
            'is_following': is_following,
        }

        return render(request, 'social/profile.html', context)


# Function for user to edit there profile
class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'birth_date', 'location', 'picture']
    template_name = 'social/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    # If the user == profile user send to view otherwise throw 403 error
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


# Function for user to add followers
class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('profile', pk=profile.pk)


# Function for user to remove followers
class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)


# Function for user to like
class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        is_dislike = False
        """
        if else statement to check if user already liked the post
        """
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


# Function for user to dislike
class Dislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        is_like = False
        """
        if else statement to check if user already disliked the post
        """
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
                post.dislikes.add(request.user)

        if is_dislike:
                post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


# Function for user to like a comment
class AddCommentLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        is_dislike = False
        """
        if else statement to check if user already liked the comment
        """
        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            comment.dislikes.remove(request.user)

        is_like = False

        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            comment.likes.add(request.user)

        if is_like:
            comment.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


# Function for user to dislike a comment
class AddCommentDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        is_like = False
        """
        if else statement to check if user already disliked the comment
        """
        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            comment.likes.remove(request.user)

        is_dislike = False

        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            comment.dislikes.add(request.user)

        if is_dislike:
            comment.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


# Function for user to search for other users
class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )
        """
        return profile list on search
        """
        context = {
            'profile_list': profile_list,
        }

        return render(request, 'social/search.html', context)


# Function to list followers and profile
class ListFollowers(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        followers = profile.followers.all()
        """
        Shows profile followers in a list
        """
        context = {
            'profile': profile,
            'followers': followers,
        }

        return render(request, 'social/followers_list.html', context)
