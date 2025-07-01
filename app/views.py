from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

def buy_now(request):
    # Create your product/order logic here
    order_id = "12345"  # Replace with your actual order ID logic
    price = "10.00"     # Replace with your actual price logic
    
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": price,
        "item_name": f"Order {order_id}",
        "invoice": order_id,
        "currency_code": "USD",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('payment_success')),
        "cancel_return": request.build_absolute_uri(reverse('payment_failed')),
        "custom": "premium_plan",  # Custom data you want to send
    }
    
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        "form": form,
        "price": price,
        "order_id": order_id
    }
    return render(request, "payment/buy_now.html", context)

def payment_success(request):
    # Handle successful payment
    return render(request, "payment/success.html")

def payment_failed(request):
    # Handle failed/cancelled payment
    return render(request, "payment/failed.html")