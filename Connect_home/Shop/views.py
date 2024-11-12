from sqlite3 import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, Category


# Create your views here.

def home(request):
    # return HttpResponse("Welcome to my django Project")
    products = Product.objects.all()  # Retrieve all products from the database
    categorys = Category.objects.all()
    print(products)  # Print the products to the console
    return render(request, 'Home1.html', {'products': products, 'cat': categorys})


def base(request):
    # return HttpResponse("Welcome to my django Project")
    context = {
        "First_name": "Arjun",
        "Second_name": "PM",
    }
    return render(request, 'base.html')


#
# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['txt_username']  #[TEXTNAME NAME]
#         password = request.POST['txt_password']
#         pass2 = request.POST['txt_con']
#         name = request.POST['txt_name']
#         phone = request.POST['txt_mob']
#
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists.')
#         else:
#             # Create user if username is unique
#             try:
#                 myuser = User.objects.create_user(username, password, phone)
#                 messages.success(request, 'Username available.')
#                 myuser.user_name = name
#                 myuser.save()
#                 print(myuser)
#                 messages.success(request, 'Thank you, You are Successfully Registered')
#                 return redirect('signin')
#             except IntegrityError:  # Handle duplicate username error
#                 # Display error message to user
#                 context = {'error_message': 'Username already exists! Please choose a different one.'}
#                 messages.error(request, "invalid credentials")
#                 return render(request, 'login.html', context)
#     return render(request, 'login.html')

#
# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['txt_username']
#         print("username", username)
#         password = request.POST['txt_pass']
#         print("password", password)
#         my_user = authenticate(username=username, password=password)
#         print("test", my_user)
#         if my_user is not None:
#             login(request, my_user)
#             f_name = my_user.get_full_name() or my_user.username
#             print(my_user)
#             return render(request, 'home1.html', {'fname': f_name})
#         else:
#             messages.error(request, "invalid credentials")
#             print(my_user)
#             return redirect('signin')
#     return render(request, 'login.html')


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.SUCCESS(request, "Successfully added new Product")
        product_form = ProductForm()
        return render(request, 'add_product.html', {'form': product_form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')
        product_form = ProductForm(instance=product)
        return render(request, 'edit_product.html', {'form': product_form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'delete_product.html', {'product': product})


def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'user_list.html', context)


def delete_all_users(request):
    User.objects.all().delete()
    return render(request, 'user_delete.html')


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        # Additional cleanup logic (e.g., delete related data)
        return redirect('login')  # Redirect to login page after deletion
    return render(request, 'user_delete.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['txt_username']
        password = request.POST['txt_pass_1']
        pass2 = request.POST['txt_pass_2']
        email = request.POST['txt_username']
        f_name = request.POST['txt_name']
        phone_no = request.POST['txt_mob']
        if username and password and pass2:
            if password != pass2:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'login.html')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'login.html')
            try:
                user = get_user_model().objects.create_user(username, password)
                user.get_full_name = f_name  # Assuming first_name exists in your User model
                user.mobi = phone_no
                user.email = email
                user.save()
                messages.success(request, 'You are successfully registered!')
                return redirect('signin')
            except IntegrityError as e:
                # Handle specific integrity errors (e.g., duplicate username)
                messages.error(request, 'Username already exists. Please choose a different one.')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'login.html')
    return render(request, 'login.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['txt_username']  # Consistent variable name
        password = request.POST['txt_pass']
        user = authenticate(username=username, password=password)
        print("user-", user)
        if user is not None:
            login(request, user)
            full_name = user.get_full_name() or user.username
            return render(request, 'user_dash.html', {'full_name': full_name})
            # return redirect('user_dash')
        else:
            messages.error(request, "Invalid credentials")
            # Consider adding more error handling here
            return redirect('signin')
    return render(request, 'login.html')



def signout(request):
    logout(request)
    return render(request, 'login.html')

def user_dash(request):
    # return HttpResponse("Welcome to my django Project")
    products = Product.objects.all()  # Retrieve all products from the database
    categorys = Category.objects.all()
    return render(request, 'User_Home.html', {'products': products, 'cat': categorys})
