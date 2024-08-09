from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import Settings

from .api import UserRegister,UserProfile,UserLogin


urlpatterns = [

    path('',views.index,name='index'),
    path('account/',views.account,name='account'),
    path('cart/', views.cart,name='cart'),
    path('products/', views.products,name='products'),
    path('details-page/<int:pk>/', views.product_details,name='details-page'),
    path('logout/', views.sign_out,name='logout'),
    path('addtocart/', views.addtocart,name='addtocart'),
    path('removeitem/<pk>',views.removeitem,name='removeitem'),
    path('orderform/',views.orderform,name='orderform'),
    path('checkout/',views.checkout,name='checkout'),
    path('orders/',views.orders,name='orders'),
    path('api/user/register',UserRegister.as_view(),name='user-register'),
    path('api/user/login',UserLogin.as_view(),name='user-login'),
    path('api/profile/me',UserProfile.as_view(),name='user-profile'),
]


urlpatterns_api = [

]

urlpatterns += urlpatterns_api