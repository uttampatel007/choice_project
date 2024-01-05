from django.shortcuts import render

from .forms import ChoiceForm
from .models import Choice
from django.contrib.auth.decorators import login_required


@login_required
def choices(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.user = request.user
            choice.save()
    else:
        form = ChoiceForm()
    
    choices = Choice.objects.filter(user=request.user)
    return render(request, 'choices/choices.html', {'form': form, 'choices': choices})
