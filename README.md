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

### Existing Features

-   __Navbar__
    - The navbar provides a navigation menu for users to easily access different sections of the application. It includes links to the homepage, user profile, workout-related features, and other relevant pages.

-   __Footer__
    - The footer is located at the bottom of the webpage and contains the logo, the social media and a link to the contact page. It provides a consistent location for secondary navigation.

-   __Homepage__
    - The homepage serves as the landing page for my application. A Gif was added on the background of the title. Was set it with css and Bootstrap.

-   __Login/Registration Pages:__
    - The login page allows existing users to log in by entering their credentials (username/email and password). The registration page enables new users to create an account by providing necessary information, such as username, email, and password. The forms has validation check for different case of errors (e.g.: 'User already exist', 'Your password must to contains...', 'Your passwords didn't match', 'Email is not have the correct form')

-   __Contact Page:__
    - The contact page allows users to reach out to the platform administrators. Includes a form with fields for name, email, and message, allowing users to submit inquiries or feedback. If the user is authenticated the email will fill in automatically.

-   __View Details of a Workout:__
    - This feature allows users to view detailed information about a specific workout. Include the workout title, description, type, intensity, calories burned, and image if exist. Users can access this information by clicking on a workout from the list or search results.

-   __My Workouts:__
    - The "My Workouts" page displays a list of workouts created by the logged-in user. It provides a personalized view, allowing users to manage and interact with their own workouts. 

-   __Edit Workout:__
    - Users can edit the details of a workout they created. The "Edit Workout" feature provides a form pre-filled with the existing details, allowing users to make modifications and update the workout.

-   __Delete Workout:__
    - The "Delete Workout" feature allows users to remove a workout they created. This action is irreversible, user will be asked to confirm the deletion with the posiblility to cancel the action of deletion.

-   __Profile Page:__
    - The profile page showcases information about the user, including their username and email and 2 buttons, one for edit and one for delete.

-   __Edit Profile Page:__
    - Users can modify their profile information page. This includes updating the username, email, and password.

-   __Delete Profile Page:__
    - The "Delete Profile" feature allows users to permanently delete their account. User will be required to confirm the decision, as this action is irreversible.

### Future Features

-   __User Ratings and Reviews:__
    - Enable users to rate and leave reviews for workouts. This can provide valuable feedback for both workout creators and users looking for high-quality content.

-   __Workout Challenges:__
    - Implement a feature that allows users to create or participate in workout challenges. Users can set goals, track progress, and compete with others.

-   __Notification System:__
    - Notification system to alert users about new comments, likes. Notifications keep users engaged and informed.

-   __Advanced User Roles:__
    - Introduce the roles "Admin" and  "Trainer" with specific permissions. Admins can manage the platform, while trainers may have the ability to curate and recommend workouts.


## Issues and Bugs


## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5) used for templates
- [CSS3](https://en.wikipedia.org/wiki/CSS) used for style
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) used for interactivity
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) used to develop the backend

- [Bootstrap](https://getbootstrap.com/) used to simplify the style process.
- [Font Awesome](https://fontawesome.com/) used for icons.

- [Django](https://www.djangoproject.com/) used for backend
- [PostgreSQL](https://www.postgresql.org/) used to create the database
- [ElephantSQL](https://www.elephantsql.com/) used to host the databse
- [Cloudinary](https://cloudinary.com/) used to store images
- [Summernote](https://summernote.org/) used to create a rich text editor for the website.
- [gunicorn](https://pypi.org/project/gunicorn/) used to run the website on Heroku.
- [dj_database_url](https://pypi.org/project/dj-database-url/) used to connect database on Heroku.
- [psycopg2](https://pypi.org/project/psycopg2/) used to connect database on Heroku
- [python-dotenv](https://pypi.org/project/python-dotenv/) used to hide sensitive information.


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
2. Add in this file your secret keys.
3. Run `pip3 install -r requirements.txt` to install needed packages.
4. Run `python3 manage.py migrate` to migrate your DB models.
5. Run `python3 manage.py createsuperuser` to create a superuser.
6. Run `python3 manage.py runserver` to start the server.

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