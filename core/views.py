from django.shortcuts import render, HttpResponse

def home(request):
	return render(request, 'core/pages/home.html')

def about(request):
	return render(request, 'core/pages/about.html')

def services(request):
	return render(request, 'core/pages/services.html')

def contact(request):
	return render(request, 'core/pages/contact.html')

def store(request):
	return render(request, 'core/pages/store.html')

def blog(request):
	return render(request, 'core/pages/blog.html')

def sample(request):
	return render(request, 'core/pages/sample.html')
