from django.shortcuts import render
from .utils import CVStructureMaker


def display_cv(request):
    cv_data = CVStructureMaker()
    return render(request, 'cv/show_cv.html', {'data':CVStructureMaker()})
