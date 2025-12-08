from django.shortcuts import render

def index(request):
    return render(request, '../../theme/templates/base.html')
    

