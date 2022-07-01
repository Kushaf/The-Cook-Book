from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

from .models import Recipe
from .forms import UserForm, UserLogin


    #loads the index page with the list of recipes
class IndexView(generic.ListView):
    template_name = 'cookbook/index.html'
    context_object_name = 'all_recipe'

    def get_queryset(self):
        return Recipe.objects.all()

    #loads the recipe page and its details
class RecipeView(generic.DetailView):
    model = Recipe
    template_name = 'cookbook/recipe.html'

    #loads page to create a new recipe
class RecipeCreate(CreateView):
    model = Recipe
    fields = ['recipe_title', 'ingredients', 'instruction']
    #template_name = 'cookbook/recipe_form.html'

    #loads the editing page
class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['recipe_title', 'ingredients', 'instruction']

    #deletes existing recipes
class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('cookbook:index')

    #registration page
class UserFormView(View):
    form_class = UserForm
    template_name = 'cookbook/registration.html'

    #Displays a Blank Form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #loads if POST is passed
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit = False)

            #normalizes data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #AUTHENTICATION
            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('cookbook:index')

        return render(request, self.template_name, {'form': form})

    #login page
class LoginAccount(View):
    form_class = UserLogin
    template_name = 'cookbook/login.html'

    #Displays a Blank Form
    def get(self, request):
        form = self.form_class(None)
        message = ''
        return render(request, self.template_name, {'form': form, 'message':message})

    #loads if POST is passed
    def post(self, request):
        form = self.form_class(request.POST)

        #checks if form(POST data) is valid
        if form.is_valid():

            #checks if user exists in the database
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('cookbook:index')
        message = 'Login Failed'
        return render(request, self.template_name, {'form': form, 'message':message})

    #logs out the user
class LogoutAccount(View):
    def get(self, request):
        logout(request)
        return redirect('cookbook:index')