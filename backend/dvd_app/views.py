from . import models, forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

def front_page(request):
    model = models.DVD

    if request.method == "POST":
        form = forms.DVDCreate(request.POST)
        if form.is_valid():
            input_arr = [form.cleaned_data.get("title"),form.cleaned_data.get("category"),str(form.cleaned_data.get("runTime"))+" Mins.",str(form.cleaned_data.get("year")),str(form.cleaned_data.get("price"))]    
            with open('Catalog.txt','a') as f:
                f.write(', '.join(input_arr))
                f.write('\n\n')
            return HttpResponseRedirect('')
    else:
        form = forms.DVDCreate()
    
    return render(request, 'register_dvd.html', {'form':form})