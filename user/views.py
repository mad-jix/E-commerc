from django.shortcuts import render,get_list_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from prodect.models import Products
from customers.models import Customer
from orders.models import Cart,CartItems
from orders.forms import OrderForm



def index(request):
    products_list={'products':Products.objects.all()}
    return render(request,'index.html', products_list)

def account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            phone=request.POST.get('phone number')
            address=request.POST.get('adress')
            #create user account
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            #creates customer account
            customer=Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )   
            return redirect('account') 
        except Exception as e:
            error_message="please check your data"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False
        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'user not existing please register')
    return render(request,'account.html',context)


def sign_out(request):
    logout(request)
    return redirect('index')

def cart(request):
    user=request.user
    customer=user.profile
    cart_obj,created=Cart.objects.get_or_create(
            owner=customer,
            orederstatus=Cart.CART_STAGE
        )
    context={'cart':cart_obj}

    return render(request,'cart.html',context)

def addtocart(request):
    if request.POST:
        user=request.user
        customer=user.profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Cart.objects.get_or_create(
            owner=customer,
            orederstatus=Cart.CART_STAGE
        )
        product=Products.objects.get(pk=product_id)
        ordere_item,created=CartItems.objects.get_or_create(
            product=product,
            owner=cart_obj,
        )
        if created:
            ordere_item.quantity=quantity
            ordere_item.save()
        else:
            ordere_item.quantity=ordere_item.quantity+quantity
            ordere_item.save()
    return redirect('cart')

def removeitem(request,pk):
    item=CartItems.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

#Part 3.1 view to display all products
def products(request):
    products_list={'products':Products.objects.all()}
    print('details is :',product_details)
    return render(request,'products.html',products_list)

#Part 3.2 detailed view of products
def product_details(request,pk):
    product = get_list_or_404(Products,pk=pk)
    print('iage',product)
    return render(request,'product_details.html',{'product':product})   
#Part 4.1 order form
def orderform(request):
    form = OrderForm()
    order = {
        'form' : form
    }
    return render(request,'orderform.html',order)


def checkout(request):
    if request.POST:
        try:
            user=request.user
            customer=user.profile
            order_obj=Cart.objects.get(
                owner=customer,
                orederstatus=Cart.CART_STAGE

            )
            if order_obj:
                form = OrderForm(request.POST, instance=order_obj)
                if form.is_valid():
                    form.save(commit=False)
                    order_obj.orederstatus = Cart.ORDER_CONFORMED
                    order_obj.save()
                status_message="Your order is conformed"
                messages.success(request,status_message)
            else:
                status_message="Your order not confomed"
                messages.error(request,status_message)
        except Exception as e:
            status_message="Your order is not confomed"
            messages.error(request,status_message)
    return redirect('orders')
# Part 6.2 order history
def orders(request):
    user = request.user
    cousomer = user.profile
    allorders = Cart.objects.filter(owner=cousomer).exclude(orederstatus=Cart.CART_STAGE)
    context = {
        'orders' : allorders
    }
    return render(request,'orders.html',context)
