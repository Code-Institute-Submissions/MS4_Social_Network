  
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm
from django.conf import settings
from products.models import Product
from .models import Order
from django.contrib.auth.models import User
from social.models import UserProfile
from django.contrib import messages
import stripe


# Checkout view
@login_required()
def checkout(request, pk):
    product = Product.objects.get(id=pk)
    user = User.objects.get(email=request.user.email)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect(reverse('products'))
        payment_form = MakePaymentForm(request.POST)
        order = Order(
            user=user,
            product=product,
            total=product.price
        )

        if payment_form.is_valid():
            order.save()

            try:
                # create a token for card details via stripe
                cardStripped = stripe.Token.create(
                    card={
                        'number': payment_form.cleaned_data['credit_card_number'],
                        'exp_month': int(payment_form.cleaned_data['expiry_month']),
                        'exp_year': int(payment_form.cleaned_data['expiry_year']),
                        'cvc': str(payment_form.cleaned_data['ccv'])
                    }
                )
           
                # create a payment via stripe
                stripe.Charge.create(
                    amount=int(product.price * 100),
                    currency="USD",
                    description=request.user.email,
                    card=cardStripped
                )
                
                # send user to success page
                return render(request, "checkout/success.html",
                        {'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLIC_KEY, 'product': product,
                        'customer': user})

            except stripe.error.CardError:
                # payment was rejected by stripe 
                # save order and show error message
                order.payment_status = 'payment_rejected'
                order.save()
                messages.error(request, 'payment rejected')

    else:
        payment_form = MakePaymentForm()

    return render(request, "checkout/checkout.html",
            {'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLIC_KEY, 'product': product,
            'customer': user})
