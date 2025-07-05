from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'main_page.html')

def about_view(request):
    return render(request, 'about_us.html')

def contact_view(request):
    return render(request, 'contact.html')

def blog_view(request):
    return render(request, 'blog.html')

def services_view(request):
    return render(request, 'services.html')