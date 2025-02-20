from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from Website import views
def is_admin(user):
    return user.is_superuser

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('login/',views.login_user  ,name='login'),  # Using built-in LoginView
    path('logout/',views.logout_user,name='logout'),
    path('add_tesk/',views.add_tesk,name='add_tesk'),
    path('delete_account/',views.delete_user_account,name='delete_account'),
    path('delete_tesk/<int:pk>/',views.delete_tesk,name='delete_tesk'),
    path('admin/', admin.site.urls),
    path('admin/', user_passes_test(is_admin)(admin.site.urls)),
]



#auth_views.LoginView.as_view(template_name='registration/login.html'),