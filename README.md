# Classrooms

It's time to take your classroom noob management tool to the next level.

Start by creating a `virtual environment`. Fork and Clone the project from [here](https://github.com/JoinCODED/ClassroomsAPI/).

You’ll get a Django project with an app `classes`. Create a new app for your API views.

Start by installing and setting up Django Rest Framework.

Add a field called `teacher` to the `Classroom` model, which is a `ForeignKey` to the `User` model.

Create a login API endpoint. Make sure the URL name is `api-login`.

Create a registration API endpoint. Make sure the URL name is `api-register`.

You have to create the necessary API views for the `Classroom` model

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

Don't forget to push your code.
