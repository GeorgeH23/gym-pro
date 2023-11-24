<h1 align="center">Gym Pro Fitness</h1>

[View the live project here](https://gym-pro-fitness-d84818eee5ff.herokuapp.com/)

## Table of Contents
  * [Table of Contents](#table-of-contents)
  * [Introduction](#introduction)
  * [User Stories](#user-stories)
  * [UX](#ux)
    + [Typography](#typography)
    + [Wireframes](#wireframes)
  * [Accessibility](#accessibility)
  * [Database Design](#database-design)
  * [Features](#features)
  * [Existing Features](#existing-features)
  * [Future Features](#features-features)
  * [Issues and Bugs](#issues-and-bugs)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Local Deployment](#local-deployment)
    + [Heroku Deployment](#heroku-deployment)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)


## Introduction

## User Stories

## UX

## Accessibility

## Database Design

## Features

## Existing Features

## Future Features

## Issues and Bugs

## Technologies Used


## Testing

### User Tests

### User Authentication Tests

| Test Case | Description |
| --- | --- |
| User Registration | Test user registration with valid credentials. Ensure a user is created in the database. |
| User Login | Test user login with valid credentials. Ensure the user is logged in. |
| Protected View | Test access to a protected view without authentication. Ensure the user is redirected to the login page. |

### Profile Tests

| Test Case | Description |
| --- | --- |
| Update Profile | Test updating user profile information. Ensure changes are saved in the database. |
| Change Password | Test changing the user password. Ensure the password is updated in the database. |

### Workouts Tests

| Test Case | Description |
| --- | --- |
| Add Workout | Test adding a workout through the form. Ensure the workout is saved in the database. |
| View Workout | Test viewing a workout. Ensure the workout has the same details as it is in the database |
| Edit Workout | Test editing an existing workout. Ensure changes are reflected in the database. |
| Delete Workout | Test deleting a workout. Ensure the workout is removed from the database. |

### Navigation and Menu Tests

| Test Case | Description |
| --- | --- |
| Navigate through the Menu | Test navigating through different sections of the application's menu. Ensure the navigation works as expected. |


## Deployment

- This project was developed using [CodeAnyWhere](https://codeanywhere.com/).
- I have used the terminal to commit changes in my GitHub repository.
- In the GitHub I have created User Stories and Epics, the commits are related to them based on the id that gitHub generated for each issue that was created.

### Prepare before Deploy
1. Create an `.env` file in your project, at root level.
2. Add this file your secret keys.
3. Run `pip3 install -r requirements.txt` to install needed packages.
4. Run `python3 manage.py migrate` to migrate your DB models.
5. Run `python3 manage.py createsuperuser` to create a superuser.
6. Run `python manage.py runserver` to start the server.

### Deploying on Heroku Pages
To deploy this web app to Heroku Pages from GitHub repository, the following steps were taken:

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/GeorgeH23/gym-pro-fitness "Link to GitHub Repo").
3. Create an account on [Heroku:](https://dashboard.heroku.com/apps).
4. Create a new Heroku app.
5. Set the BuilPacks and the Config Vars.
6. Link the Heroku app to the git hub repository.
7. Click on Deploy.


## Credits

### Content 
- The ReadME file was inspired from my first project [Travel Addict](https://github.com/GeorgeH23/travel-addict/blob/main/README.md) and [Books4Life](https://github.com/tomdu3/books4life/)
- All other content was written by the developer