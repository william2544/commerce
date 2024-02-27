from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ListingForm,BidForm
from .models import *
from django.contrib import messages


def index(request):
    products=Listing.objects.filter(status=True)
    return render(request, "auctions/index.html",{
        'products':products
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def createListing(request):
    if request.method == 'POST':
        form=ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request,"auctions/createList.html",{
            'form':form
        })
    else:
        form=ListingForm()
        return render(request,'auctions/createList.html',{
            'form':form
        })
    


def watlists(request):
    user=request.user
    products=user.watchlists.all()
    return render(request,'auctions/watchlist.html',{
        'products':products,
        'user':user
    })


def category(request):
    categories=Category.objects.all()
    return render(request,'auctions/category.html',{
        'categories':categories
    })

def eachCategory(request,id):
    each_cat=Category.objects.get(id=id)
    products=Listing.objects.filter(category=each_cat)
    return render(request,'auctions/cateogryResult.html',{
        'products':products,
        'category':each_cat.type
    })

def detailed(request, id):
    user=request.user
    product=Listing.objects.get(id=id)
    isTrue=product in user.watchlists.all()
    allcomments=Comment.objects.filter(listing=product)
    return render(request,'auctions/detailed.html',{
        'product':product,
        'isTrue':isTrue,
        'allcomments':allcomments
    })

def addToWatchlist(request,id):
    user=request.user
    product=Listing.objects.get(id=id)
    user.watchlists.add(product)
    # isTrue=product in user.watchlists.all()
    return redirect('index')


def removeFromWatchlist(request,id):
    user=request.user
    product=Listing.objects.get(id=id)
    user.watchlists.remove(product)
    # isTrue=product in user.watchlists.all()
    return redirect('watchlists')

def placeBid(request, pk):
    product = get_object_or_404(Listing, id=pk)
    
    if request.method == 'POST':
        form = BidForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detailed',id=pk)
        else:
            print('The form was not valid!!')
    else:
        form=BidForm(instance=product)
        product = get_object_or_404(Listing, id=pk)
        return render(request, 'auctions/placebid.html',{
            'form':form,
            'product':product
        })



def comment(request,id):
    product=Listing.objects.get(id=id)
    if request.method == 'POST':
        comment=request.POST['comment']
        con=Comment(listing=product,message=comment,author=request.user)
        con.save()
    else:
        print('The post method did not work')
    return redirect('detailed',id=id)
 


def close_auction(request,id):
   listingData=Listing.objects.get(id=id)
   listingData.status=False
   listingData.save()
   messages.success(request, 'The auction was closed!!!')
   owner=listingData.creator == request.user.username
   products=Listing.objects.filter(status=True)
   return render(request, "auctions/index.html",{
        'products':products,
        'owner':owner
    })

