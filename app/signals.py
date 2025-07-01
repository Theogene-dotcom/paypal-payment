from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

@receiver(valid_ipn_received)
def paypal_ipn_handler(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # Check that the receiver email is the same we expect
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            # Not a valid payment
            return
        
        # Check if the payment amount is correct
        if ipn_obj.mc_gross != "10.00" or ipn_obj.mc_currency != "USD":
            # Handle incorrect payment
            return
        
        # Get the order ID from the invoice
        order_id = ipn_obj.invoice
        
        # Update your order in database
        # Example:
        # order = get_object_or_404(Order, id=order_id)
        # order.paid = True
        # order.save()
        
        # You can also check ipn_obj.custom for additional data
        # plan = ipn_obj.custom
    else:
        # Handle other payment statuses if needed
        pass