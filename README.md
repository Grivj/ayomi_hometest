<img width="900" alt="image" src="https://user-images.githubusercontent.com/4151401/154772567-95d85c9e-94b9-4968-a46e-2faddd0ae986.png">
<img width="900" alt="image" src="https://user-images.githubusercontent.com/4151401/154772683-801fbfd1-1640-4d12-ad9c-9366cb43503c.png">


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
On ARM macbooks, both these commands may fail, what worked for me was running:
```
DOCKER_BUILDKIT=0
```
in front of the commands.

# URLs

- /            [default page](same as /register)
- /login       [redirects to /profile once logged]
- /register    [redirects to /profile once the user is created (and logged)]
- /profile     [requires logged]

# Users app

- The app settings and files can be found under ./users/   
- The somewhat tricky part was for the email's update using Ajax.
    - The frontend's logic for the request is in ./users/static/users/main.js
    - The backend's logic is in the view at ./users/views.py
  
