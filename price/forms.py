
from django.forms import ModelForm
from .models import Order
from django import forms


class CustomerForm(ModelForm):
	
	class Meta:
		model = Order
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(CustomerForm,self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
		self.fields['email'].widget.attrs['placeholder'] = 'Enter the Email'
		self.fields['credit_card'].widget.attrs['placeholder'] = 'Enter Your Credit Card Number'
		self.fields['expire_date'].widget.attrs['placeholder'] = 'Enter Your Credit Card Expire Date (MM/YY)'
		self.fields['cvv'].widget.attrs['placeholder'] = 'Enter CVV'
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control p-0'
