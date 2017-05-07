import stripe

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from users.models import Buyer


class CreateCustomerView(LoginRequiredMixin, View):
    def get_success_url(self):
        return reverse('magazine:list')

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_API_KEY
        token = request.POST['stripeToken']

        customer = stripe.Customer.create(
            email=request.user.email,
            source=token,
        )

        Buyer.objects.filter(id=request.user.id)\
                     .update(customer_id=customer.id)

        return redirect(self.get_success_url())


class ChargeCustomerView(LoginRequiredMixin, View):
    def get_success_url(self):
        return reverse('magazine:list')

    def post(self, request, *args, **kwargs):
        print("Make charge here. Use celery.")
        return redirect(self.get_success_url())
