from django.conf import settings
from django.conf.urls.static import static
from django.template.context_processors import media
from django.urls import path
from . import views

urlpatterns = [
    path('home1/', views.home, name="home"),
    path('', views.base, name="base"),
    path('edit_product/<int:product_id>/', views.edit_product, name="edit_product"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('user_dash/', views.user_dash, name="user_dash"),
    path('delete/', views.delete_all_users, name="delete_all_users"),

]
