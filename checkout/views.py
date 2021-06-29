  
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm
from django.conf import settings
from products.models import Product
from .models import Order
from django.contrib import messages
from django.contrib.auth.models import User
from social.models import UserProfile
import stripe

# Create your views here.


@login_required()
def checkout(request, pk):
    product = Product.objects.get(id=pk)
    user = User.objects.get(email=request.user.email)
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect(reverse('products'))
        payment_form = MakePaymentForm(request.POST)
        order = Order(
            user=user,
            product=product,
            total=product.price
        )

        # if payment is nothing, save order and go to profile page
        if product.price == 0:
            order.payment_status = 'payment_collected'
            order.save()
            profile = UserProfile.objects.get(user=user)
            profile.Product = product
            profile.save()
            messages.success(request, "Your service level has been changed.")
            return redirect(reverse('profile'))

        elif payment_form.is_valid():
            order.save()

            try:
                # stripe takes integer amount so need to multiply from cents up
                customer = stripe.Charge.create(
                    amount=int(product.price * 100),
                    currency="USD",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                # user has not paid, update the Order status
                order.payment_status = 'payment_rejected'
                order.save()
                messages.error(request, "Sorry, your card was declined.")

            if customer.paid:
                # user has paid, update the Order status
                messages.success(request, "Your payment was success and your service level has been updated.")
                order.payment_status = 'payment_collected'
                order.save()
                # user has paid, update the Customer object with the product, so they get more features enabled
                profile = UserProfile.objects.get(user=user)
                profile.product_level = product
                profile.save()
                return redirect(reverse('profile'))
            else:
                # user has not paid, update the Order status
                order.payment_status = 'payment_rejected'
                order.save()
                messages.error(request, "Unable to take payment")
        else:
            messages.success(request, "Please enter your payment information below.")
    else:
        payment_form = MakePaymentForm()

    return render(request, "checkout/checkout.html",
                  {'payment_form': payment_form, 'product': product,
                   'customer': user})
