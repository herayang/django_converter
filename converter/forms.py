from django import forms 


class ConvertForm(forms.Form):
    temp_choice = (('1','fahrenheit'),("2","celcius"))
    desired_temp = forms.FloatField(label="Enter temperature in c/f")
    in_what = forms.ChoiceField(choices = temp_choice, label="Temperature in")

class LenForm(forms.Form):
    len_choice = (('1','inch'),("2","cm"))
    desired_len = forms.FloatField(label="Enter Length in cm/in")
    in_unit = forms.ChoiceField(choices = len_choice, label="Unit")

class VolForm(forms.Form):
    liq_choice = (('1','fluid ounce'),("2","mililiter"))
    desired_vol = forms.FloatField(label="Enter Length in fl oz/ml")
    in_unit = forms.ChoiceField(choices = liq_choice, label="Unit")