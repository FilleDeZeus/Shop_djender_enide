from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/body/main/pages/home/home.html')

def shoe(request):
    return render(request, 'app/body/main/pages/shoe/shoe.html')

def shoe_details(request):
    return render(request, 'app/body/main/pages/shoe_details/shoe_details.html')

def blog(request):
    return render(request, 'app/body/main/pages/blog/blog.html')

def contact(request):
    return render(request, 'app/body/main/pages/contact/contact.html')

def cart(request):
    return render(request, 'app/body/main/pages/cart/cart.html')

def checkout(request):
    return render(request, 'app/body/main/pages/checkout/checkout.html')

def error_404(request):
    return render(request, 'app/body/main/pages/error_404/error_404.html')

def blog_details(request):
    return render(request, 'app/body/main/pages/blog_details/blog_details.html')

def trackorder(request):
    return render(request, 'app/body/main/pages/trackorder/trackorder.html')

def about(request):
    return render(request, 'app/body/main/pages/about/about.html')

def wishlist(request):
    return render(request, 'app/body/main/pages/wishlist/wishlist.html')

def login(request):
    return render(request, 'app/body/main/pages/login/login.html')

def logout(request):
    return render(request, 'app/body/main/pages/logout/logout.html')

def signup(request):
    return render(request, 'app/body/main/pages/signup/signup.html')