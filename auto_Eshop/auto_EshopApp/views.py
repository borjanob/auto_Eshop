from django.shortcuts import render,redirect

from .UserSignUpForm import UserSignUpForm
from django.contrib.auth.models import User
from .models import CustomUser,Post,Vehicle,WishlistItem
from django.contrib.auth import login,authenticate,logout
from .VehicleForm import VehicleForm
from .PostForm import PostForm

def get_custom_user(request):

    if request.user.is_anonymous == False:
        logged_in_user =  request.user
        user_to_send = CustomUser.objects.get(user = logged_in_user)       
    else:
        user_to_send = None
    
    return user_to_send

def home(request):

    user_to_send = get_custom_user(request)

    context = { 'user': user_to_send}

    return render(request,'home.html',context=context)


def signUp(request):

    form = UserSignUpForm()

    if request.method == 'POST':
        form = UserSignUpForm(request.POST, request.FILES)
        print (form.data['username'])
        if form.is_valid():
            custom_user = form.save(commit=False)
            new_user = User.objects.create_user(username=form.data['username'],
                                password=form.data['password'])
            custom_user.user = new_user
            custom_user.save()
            return redirect('/login')
    context = {'form' : form}
   
    return render(request,'signup.html',context=context)



def login_func(request,message=None):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is None:
            context = {'error':'Invalid username or password'}
            return render(request,'login.html',context)

        login(request, user) 
        return redirect('/home')

    context = {'message' : message}

    return render(request,'login.html',context)


def logout_func(request):

    if request.method == 'POST':
        logout(request)
        return redirect('/home')

    return render(request,'logout.html')


def vehicles(request):

    user_to_send = get_custom_user(request)

    posts = Post.objects.all()

    manufacturers = Vehicle.objects.values_list('make', flat=True).distinct()

    if request.method == 'POST':
        manufacturer_filter = request.POST.get('manufacturer')
        if manufacturer_filter != 'all_manufacturers':
            vehicles_from_manufacturer = Vehicle.objects.filter(make = manufacturer_filter)

            print(vehicles_from_manufacturer)

            posts = []

            for vehicle_filter in vehicles_from_manufacturer:
                post_to_add = vehicle_filter.post
                posts.append(post_to_add)

    context = {'user':user_to_send,'posts' : posts,"manufacturers":manufacturers}

    return render(request,'vehicles.html',context=context)


def add_post(request):
    
    vehicle_form = VehicleForm()

    if request.method == 'POST':
        vehicle_form = VehicleForm(request.POST, request.FILES)
        if vehicle_form.is_valid():
            vehicle = vehicle_form.save(commit=False)

            logged_in_user = request.user

            user = CustomUser.objects.get(user = logged_in_user)    
            vehicle.user = user   
            vehicle.save()

            note = request.POST['note']

            post = Post(
                vehicle=vehicle,
                user=user,
                note=note
                )
            post.save()

            return redirect('/home')
    context = {'form' : vehicle_form}

    return render(request,'add_post.html',context)

def details(request,id):

    post = Post.objects.get(pk=id)

    context = {'post':post}

    if request.method == 'POST': 
            custom_user = get_custom_user(request)

            wishlist_item =  WishlistItem(
                user=custom_user,
                post = post
                )
            wishlist_item.save()
            return redirect('/vehicles')


    return render(request,'details.html',context)


def wishlist(request,id = None):

    custom_user = get_custom_user(request)

    if id != None: 
            
            to_delete = WishlistItem.objects.get(pk = id)
            WishlistItem.delete(to_delete)
            return redirect('/wishlist')


    items = WishlistItem.objects.filter(user = custom_user)

    context = {'items' : items}

    return render(request,'wishlist.html',context)
