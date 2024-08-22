
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/',views.login_view,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('accounts/logout/', views.logout_user, name='logout'),
    path('list/',views.list,name='list'),
    path('delete/',views.delete,name='delete')

]
