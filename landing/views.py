from django.shortcuts import render
from django.views import View
from social.models import Post
from social.views import PostListView
from social.forms import PostForm

# Landing page 
class Index(View):
    def get_default_context(self, request) -> dict:
        posts = Post.objects.filter().order_by('-created_on')
        return {
            'post_list': posts
        }
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = self.get_default_context(request)
            context["form"] = PostForm()
            return render(request, 'social/post_list.html', context)

        else:
            return render(request, 'landing/index.html')
