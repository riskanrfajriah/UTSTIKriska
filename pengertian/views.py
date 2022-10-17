from django.shortcuts import render

# Create your views here.
def pengertian(request):
    return render(request, 'indexpengertian.html')