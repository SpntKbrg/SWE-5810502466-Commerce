from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
@login_required
def checkout(request) :
  publishKey = settings.STRIPE_PUBLISHABLE_KEY
  customer_id = request.user.userStripe.stripe_id
  if request.method == "POST" :
    token = request.POST['stripeToken']
    try :
      customer = stripe.Customer.retrive(customer_id)
      customer.sources.create(source=token)
      charge = stripe.Charge.create(
  amount=1000,
  currency="gbp",
  description="Example charge",
  source=token,
)
    except stripe.errorCardError as e :
      pass
  context = {'publishKey':publishKey}
  template = 'checkout.html'
  return render(request, template, context)
