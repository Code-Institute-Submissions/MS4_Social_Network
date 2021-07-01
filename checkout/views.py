  
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm
from django.conf import settings
from products.models import Product
from .models import Order
from django.contrib.auth.models import User
from social.models import UserProfile
import stripe

# Create your views here.


@login_required()
def checkout(request, pk):
    product = Product.objects.get(id=pk)
    user = User.objects.get(email=request.user.email)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    message = None
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
            return redirect(reverse('profile'))
        elif payment_form.is_valid():
            order.save()

            try:
                # secure token via stripe
                cardStripped = stripe.Token.create(
                    card={
                        'number': payment_form.cleaned_data['credit_card_number'],
                        'exp_month': int(payment_form.cleaned_data['expiry_month']),
                        'exp_year': int(payment_form.cleaned_data['expiry_year']),
                        'cvc': str(payment_form.cleaned_data['ccv'])
                    },
                )
           
                # stripe takes integer amount so need to multiply from cents up
                stripe.Charge.create(
                    amount=int(product.price * 100),
                    currency="USD",
                    description=request.user.email,
                    card=cardStripped
                )

                return render(request, "checkout/success.html",
                        {'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLIC_KEY, 'product': product,
                        'customer': user})

            except stripe.error.CardError:
                # user has not paid, update the Order status
                order.payment_status = 'payment_rejected'
                order.save()
                message = stripe.error.CardError

            else:
                # user has not paid, update the Order status
                order.payment_status = 'payment_rejected'
                order.save()
            
        else:
            messages.success(request, "Please enter your payment information below.")

    else:
        payment_form = MakePaymentForm()

    return render(request, "checkout/checkout.html",
            {'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLIC_KEY, 'product': product,
            'customer': user})
