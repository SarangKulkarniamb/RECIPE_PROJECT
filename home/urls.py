from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutpage,name="logout"),
    path('register/',views.register,name='register'),
    path('add_recipe/',views.add_recipe,name='add_recipe'),
    path('update_recipe/<str:pk>/',views.update_recipe,name='update_recipe'),
    path('delete_recipe/<str:pk>/',views.delete_recipe,name='delete_recipe'),
    path('all_recps/',views.all_recps,name="all_recps"),
    path('view_recp/<str:pk>/',views.view_recp,name="view_recp"),
    path('dashboard/join/',views.dashboard_join,name="dashboard_join"),
    path('dashboard/user_recipes/',views.dashboard_userrecps,name="dashboard_view"),
] 
