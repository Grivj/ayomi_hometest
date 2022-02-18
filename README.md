# Ayomi's test
My submission for Ayomi's home test

## The objective was to:
1. Create a login page for the user
2. Once connected, redirect the user to a page where his info are displayed
3. A popup can be opened via a button on the page
4. Inside the popup, the user can find a form to update his email address.  
***When sending the form, the page shouldn't refresh!***
5. A database should be included
6. Use Django, Python & Bootstrap
7. Use Docker & GitHub


# Quickstart the project

Open terminal in the folder

```
docker-compose up -d
docker-compose run web python manage.py migrate
```
On ARM macbooks, both these commands may fail, running:
```
DOCKER_BUILDKIT=0
```
in front of the commands may do the trick.

## 
