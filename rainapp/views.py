from django.shortcuts import render, redirect
from .forms import ViewerDataForm

def collect_data(request):
    if request.method == 'POST':
        form = ViewerDataForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')  # After submission
    else:
        form = ViewerDataForm()
    return render(request, 'form.html', {'form': form})