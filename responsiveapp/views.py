from django.shortcuts import render

# Create your views here.
def responsiveproducts(request):
    context = {}
    return render(request, 'responsiveapp/responsive.html', context)