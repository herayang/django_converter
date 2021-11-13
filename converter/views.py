from django.shortcuts import render
from django.http import HttpResponse 
from converter.forms import ConvertForm
from converter.forms import LenForm
from converter.forms import VolForm

# Main page (Converts temperature)
def converter(request):
    if request.method == 'POST':
        form = ConvertForm(request.POST)

        if form.is_valid(): 
            temp = form.cleaned_data['desired_temp'] 
            choice = form.cleaned_data['in_what']

            if choice == '1':
                temp = (temp - 32) * 5/9
                temp = "{:.2f}".format(temp)
            else: 
                temp = (temp * 9/5) + 32 
                temp = "{:.2f}".format(temp)   
        return render(request,'convertPages.html',{'form':form,'temp':temp})
        
    else: 
        form = ConvertForm()
        return render(request,'convertPages.html',{'form':form})

# Page for length conversion
def len_convert(request):
    if request.method == 'POST':
        len_form = LenForm(request.POST)

        if len_form.is_valid(): 
            user_len = len_form.cleaned_data['desired_len']
            len_choice = len_form.cleaned_data['in_unit']
            
            if len_choice == '1': 
                user_len = user_len / 0.393701
                user_len = "{:.2f}".format(user_len)
                
            else: 
                user_len = user_len * 0.393701
                user_len = "{:.2f}".format(user_len)
            
        return render(request,'convertLen.html',{'len_form':len_form,'user_len':user_len})
        
    else: 
        len_form = LenForm()
        return render(request,'convertLen.html',{'len_form':len_form})


def vol_convert(request):
    if request.method == 'POST':
        vol_form = VolForm(request.POST)

        if vol_form.is_valid(): 
            user_vol = vol_form.cleaned_data['desired_vol']
            vol_choice = vol_form.cleaned_data['in_unit']
            
            if vol_choice == '1': 
                user_vol = user_vol * 29.57353
                user_vol = "{:.2f}".format(user_vol)
                
            else: 
                user_vol = user_vol / 29.57353
                user_vol = "{:.2f}".format(user_vol)
            
        return render(request,'conVol.html',{'vol_form':vol_form,'user_vol':user_vol})
        
    else: 
        vol_form = VolForm()
        return render(request,'conVol.html',{'vol_form':vol_form})