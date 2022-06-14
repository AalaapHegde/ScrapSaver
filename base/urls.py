from django.urls import path
from .views import IngredientList, IngredientDetail, IngredientCreate, IngredientUpdate, DeleteView, CustomLoginView, RegisterPageFormView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPageFormView.as_view(), name='register'),
    path('ingredient/', IngredientList.as_view(), name='ingredient'),
    path('', views.home_page, name='home'),
    path('about_us/', views.about_page, name='about'),
    path('donate/', views.donate_page, name='donate'),
    path('ingredient/<int:pk>/', IngredientDetail.as_view(), name='ingredientDetail'),
    path('ingredient-create/', IngredientCreate.as_view(), name='ingredient-create'),
    path('ingredient-update/<int:pk>/', IngredientUpdate.as_view(), name='ingredient-update'),
    path('ingredient-delete/<int:pk>/', DeleteView.as_view(), name='ingredient-delete'),
    path('user/', views.user, name='user'),
    path('profile/', views.profile_page, name = 'profile')

]
