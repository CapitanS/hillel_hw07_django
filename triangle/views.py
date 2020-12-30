import math

from django.shortcuts import render

from .forms import TriangleForm


# Create your views here.
def get_hypotenuse(request):
    """View function for calculating an hypotenuse."""
    if request.method == 'POST':
        form = TriangleForm(request.POST)
        if form.is_valid():
            adjacent_cathetus = form.cleaned_data['adjacent_cathetus']
            opposing_cathetus = form.cleaned_data['opposing_cathetus']
            hypotenuse = round(math.hypot(adjacent_cathetus, opposing_cathetus), 2)
            return render(request, 'triangle.html', {'hypotenuse': hypotenuse})
    else:
        form = TriangleForm()
    return render(request, 'triangle.html', {'form': form})
