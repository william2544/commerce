from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('createList', views.createListing,name='createListing'),
    path('watclist',views.watlists,name='watchlists'),
    path('category',views.category,name='category'),
    path('categoryNo/<int:id>',views.eachCategory,name='eachCategory'),
    path('details/<int:id>',views.detailed,name='detailed'),
    path('addToWatchlist/<int:id>',views.addToWatchlist,name='addToWatchlist'),
    path('removeFromWatchlist/<int:id>',views.removeFromWatchlist,name='removeFromWatchlist'),
    path('placeBid/<int:pk>',views.placeBid,name="placeBid"),
    path('comment/<int:id>',views.comment,name='comment'),
    path('closeAuction/<int:id>',views.close_auction,name='close_auction'),
]