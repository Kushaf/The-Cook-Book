# The-Cook-Book
**Technical Code Test**

This programts was created using Django 3.0, Python 3.7, with PyCharm as the IDE
  - In case there is an issue, please install:
    - Django 3.0
    - Python 3.7
  
Run *'python manage.py runserver'* on the console (assuming your are on the same directoy as 'manage.py')

On the console, the program should run and you have now created a server
  - On my device, the server domain address was set to: *127.0.0.1:8000*

ADMIN USER
  - Access admin page by adding *'admin/'* to the domain address
  - I logged in as the "admin", you have access to:
    - Creating a User
    - Managing/Editing a User Profile
    - Deleting a User
    - Creating Recipes
    - Deleting Recipes
    - Editing Recipes
  - The current admin credentials:
    - USERNAME: admin
    - PASSWORD: code1234

BASIC USER
  - This user is limited to:
    - Creating Recipes
    - Editing Recipes
    - Deleting Recipes

DATABASE
  - The "Recipe" Database contain:
    - (recipe_title): Char field input
    - (ingredients): text field input
    - (instrution): text field input

**WEBSITE - *"THE COOK BOOK"***

**INDEX PAGE** (Accessed by inputing the domain address EX:'127.0.0.1:8000' )
  - This is the Homepage
    - Access to:
      - Recipe Details
      - Creating Recipes
      - Account Login
      - Account Registration
![HOMEPAGE](https://user-images.githubusercontent.com/47987721/176850693-5b6bc1aa-108b-446e-94be-be1e756dad03.png)

**RECIPE PAGE**
  - This is page contains the details of a Recipe
    - Access to:
      - Editing Recipe
      - Deleting Recipe
![RECIPE](https://user-images.githubusercontent.com/47987721/176850701-a1c79474-cd4e-445c-9505-f5c756484cff.png)

