from django import forms
from .models import *



class FirstForm(forms.ModelForm):
    class Meta:
        model = signin
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = log
        fields = '__all__'


# forms.py


class HotelForm(forms.ModelForm):

	class Meta:
		model = Hotel
		fields = ['name', 'hotel_Main_Img']
