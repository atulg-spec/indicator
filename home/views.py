from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.http import HttpResponse

@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        # Add more rules here
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def indicators(request):
    return render(request,'home/indicators.html')

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('valid')
            obj = form.save(commit=False)
            obj.user = request.user  # Associate the current user with the Contact instance
            obj.save()
            messages.success(request,'Contact request submitted')
            messages.success(request,'We will connect to you as soon as possible.')
            return redirect('/contact')
    return render(request,'home/contact.html')

def privacypolicy(request):
    return render(request,'home/privacypolicy.html')

def refundpolicy(request):
    return render(request,'home/refundpolicy.html')

def about(request):
    return render(request,'home/about.html')

def disclaimer(request):
    return render(request,'home/disclaimer.html')

def termsofuse(request):
    return render(request,'home/termsofuse.html')

def careers(request):
    return render(request,'home/careers.html')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)
