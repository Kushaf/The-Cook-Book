from django.urls import path
from . import views

app_name = 'cookbook'

urlpatterns = [
    #index page
    path('', views.IndexView.as_view(), name = 'index'),

    #views the recipe page
    path('<pk>/', views.RecipeView.as_view(), name = 'recipe'),

    #creates new recipes
    path('recipe/add/', views.RecipeCreate.as_view(), name = 'recipe-add'),

    #updates existing recipes
    path('<pk>/update/', views.RecipeUpdate.as_view(), name = 'recipe-update'),

    #deletes existing recipes
    path('<pk>/delete/', views.RecipeDelete.as_view(), name = 'recipe-delete'),

    #authentication
        #register a new user
    path('account/register/', views.UserFormView.as_view(), name = 'register'),

        #login
    path('account/login/', views.LoginAccount.as_view(), name = 'login'),

        #logout
    path('account/logout/', views.LogoutAccount.as_view(), name = 'logout'),
]