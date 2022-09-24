from . import views
from django.urls import path
urlpatterns = [
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('adminhome',views.home,name='home'),
    path('',views.user_homepage,name='user_homepage'),
    path('create_user/',views.create_user,name='create_user'),
    path('create_department/',views.create_department,name='create_department'),
    path('delete_dep/<int:id>',views.delete_dep,name='delete_dep'),
    path('update_dep/<int:id>',views.update_dep,name='update_dep'),

]
