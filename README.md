# Classrooms

It's time to take your classroom management tool to the next level.

## Setup

1. Fork and clone the project from [here](https://github.com/JoinCODED/ClassroomsAPI/).
2. Create a `virtual environment`, activate it, and install the dependencies using `pip install -r requirements.lock`.

## Steps

1. You’ll get a Django project with an app `classes`.
2. Start by installing and setting up `Django Rest Framework`.
3. Add a field called `teacher` to the `Classroom` model, which is a `ForeignKey` to the `User` model.
4. Create a login API endpoint. Make sure the URL name is `api-login`.
5. Create a registration API endpoint. Make sure the URL name is `api-register`.
6. You have to create the necessary API views for the `Classroom` model

   - `API List View` with url name `api-classroom-list` and the following fields:
     - `subject`
     - `name`
     - `year`
     - `teacher`
   - `API Detail View` with all the fields of the Classroom model and url name `api-classroom-detail`.
   - `API Create View` with url name `api-classroom-create`
     - Keep in mind that the logged in user should be assigned as the teacher
   - `API Update View` with url name `api-classroom-update` which can update the following fields:
     - `subject`
     - `year`
     - `name`
   - `API Delete View` with url name `api-classroom-delete`

7. Don't forget to push your code.
