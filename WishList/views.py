from django.shortcuts import render, redirect
from .models import User, Item, Wish
# Create your views here.
def index(request):
    if 'f_name' in request.session:
        index = {
            'title' : 'Welcome to Wish World',
            'users' : User.objects.all(),
            'myitems' : Item.objects.all().filter(create_by = request.session['user_id']).order_by('-id'),
            'mycount' : Item.objects.all().filter(create_by = request.session['user_id']).count(),
            'allitems' : Item.objects.all().filter().order_by('-id'),
            'allcount' : Item.objects.all().filter().count(),
        }
    else:
        index = {
            'title' : 'Welcome to Wish World',
        }
    return render(request, 'WishList/index.html', index)

def register(request):
    # print request.POST
    if request.method == 'POST':
        user = User.objects.create(f_name = request.POST['f_name'], l_name = request.POST['l_name'])
        user.save()
        request.session['user_id'] = user.id
        request.session['f_name'] = user.f_name
        return redirect('WishList:dashboard')
    else:
        register = {
            'title' : 'Welcome to Register',
        }
        return render(request, 'WishList/register.html', register)

def logIn(request):
    # print request.POST
    if request.method == 'POST':
        user = User.objects.filter(f_name = request.POST['f_name'])
        if user:
            request.session['user_id'] = user[0].id
            request.session['f_name'] = user[0].f_name
            return redirect('WishList:dashboard')
        else:
            return redirect('WishList:logIn')
    else:
        logIn = {
            'title' : 'Welcome to LogIn',
        }
        return render(request, 'WishList/logIn.html', logIn)

def addWish(request):
    # print request.POST
    if request.method == 'POST':
        Item.objects.create(create_by = User.objects.get(id = request.POST['create_by']), name = request.POST['name'])
        return redirect('WishList:dashboard')
    else:
        addWish = {
            'title' : 'Welcome to make a Wish',
        }
        return render(request, 'WishList/addWish.html', addWish)

def delWish(request):
    # print request.POST
    if request.method == 'POST':
        Item.objects.filter(id = request.POST['id']).delete()
        return redirect('WishList:dashboard')

def mvWish(request):
    # print request.POST
    if request.method == 'POST':
        Item.objects.filter(id = request.POST['id']).update(create_by = request.session['user_id'])
        return redirect('WishList:dashboard')

def logOut(request):
    request.session.clear()
    return redirect('WishList:index')
