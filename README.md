# Employee Management System

## Introduction

Portfolio Project 4 for the Code Institute course<br>
<br>
This application is developed for business employee management.<br>
<br>


[The deployed version can be found here!](https://employee-management-072b60f670f5.herokuapp.com/)



## Table of Contents

* [Introduction](#introduction)

* [Important Information](#important-information)
* [Use Case](#use-case)
* [User Experience](#user-experience)
  * [Design](#design)
    * [Color Scheme](#color-scheme)
    * [Typography](#typography)
  * [Features](#features)
    * [UX/UI](#ux/ui)
    * [CRUD](#crud)
    * [Future Features](#future-features)
* [Development](#development)
  * [Database](#database)
  * [Technologies Used](#technologies-used)
    * [Frameworks](#frameworks)
    * [Languages](#languages)
    * [Modules & Libraries](#mudules--libraries)
    * [Programs & Tools](#programs--tools)
  * [Deployment](#deployment)
    * [Version Control](#version-control)
    * [Heroku Deployment](#heroku-deployment)
  * [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Manual Testing](#manual-testing)
    * [Possible Improvements](#possible-improvments)
    * [Fixed Bugs](#fixed-bugs)
    * [Known Unfixes Bugs](#known-unfixed-bugs)
* [Credits](#credits)
  * [Acknowledgements](#acknowledgements)


## Important Information
A great attention has been paid to keep sensible data secure without committing to GitHub, however human errors might occur.<br>



## Use Case

This application is developed for for business employee management.<br>


<br>
In this system, there are three different roles:

- Admin
- Manager
- Employee
<br>
When a user checks in, they are able to view their profile, which includes information about their personal details, such as name, email address etc, their job details, and rating.<br>
<br>




With the help of this system, managers and the admin can change the following:

- Give and edit ranks of employees
- Create roles, departments

This is a simple system fulfilling the role of a smooth system that allows the tracking of various employees and managers working at the company.

## User Experience

### Design

#### Color Scheme

The visuals of the site weren't focused on due lack of time, as the priority has been making the system properly work.<br>




#### Typography

No special typography was used.<br>
The font is the standard font of the browser.<br>
Font-size changes and boldness were used.<br>



### Features

#### UX/UI

The UI of the project has been kept at a simple, easy-to-understand level, as overperforming on this would have made no sense with no other visual "upgrades".<br>
<br>

The simplified UI allows the user to smoothly navigate to their profile, accessing any and every work-related information and personal data.



#### CRUD

Full CRUD functionality is implemented with the following features:

**Employee**
- Create Guest Profile
- Read Guest Profile
- Update Guest Profile
- Delete Guest Profile
<br>

**Manager**
- Give Roles to Employees
- Read Employee information
- Update Roles of Employees
- Delete Employees
<br>

**Admin**
- Create Roles and Departments
- Read Employee information
- Update Roles of Employees
- Delete Employees
<br>


#### Future Features

As the main goal of the proejct was for it to properly work by the deadline, there is definitely room for improvement on the visuals.

**Visually engaging page**<br>
The site should use colors and potentially background images relevant to the company.<br>
Company logo and role images (if exists) should be added.<br>
<br>

**Account management**<br>
Users have no way of receiving any form of password reminder in case they forget their login details, this must be added.<br>
<br>






## Development

### Database

The following image illustrated the database structure and was made using [drawSQL](https://drawsql.app):<br>
<br>

![Database Structure](https://imgur.com/a/sql-Oxp4stj)
<br>





### Technologies Used

#### Languages

- HTML
- CSS
- JavaScrips
- Python
- Django Template Language
- Bootstrap

#### Frameworks

The following frameworks have been used.

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [FontAwesome](https://fontawesome.com/)

#### Modules & Libraries

- asgiref
- crispy bootstrap4
- dj-database-url
- Django
- django-crispy-forms
- gunicorn
- mysql-connector
- packaging
- psycopg
- psycopg2
- psycopg2-binary
- python-decouple
- sqlparse
- typing_extensions
- tzdata
- whitenoise

#### Programs & Tools

During the development of this application, the following programs and tools have been used.

- [Visual Studio Code](https://code.visualstudio.com/) (IDE - Integrated Development Environment)
- [drawSQL](https://drawsql.app) (Creating database visualization)
- [Heroku](https://www.heroku.com/home) (Deployment of final application)
- [Git](https://git-scm.com/) (Version control)
- [GitHub](https://github.com/) (Used as cloud repository)
- [CI Postgres Database](https://dbs.ci-dbs.net/) (Used for database hosting)
- [CI Python Linter](https://pep8ci.herokuapp.com/) (Python testing)
- [JSHint](https://jshint.com/) (JavaScript testing)
- [W3C HTML Validator](https://validator.w3.org/) (HTML testing)
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) (CSS testing)
- [Lighthouse](https://lighthouse-metrics.com/) (Testing of Performance, Accessibility, Best Practices and SEO) 

### Deployment

#### Version Control

This application was developed using Visual Studio Code as the IDE and GitHub for hosting the repository.<br>
<br>
Git was used for version control by using the following comments:

- git add filename - Select the files that should be uploaded and updated to the GitHub repository.
- git commit -m "commit message" - Commenting the commit to better understand the changes in this specific commit.
- git push - Upload the commit to GitHub.




#### Heroku Deployment

**Step 0: Create requirements.txt**
- Create the requirements.txt (pip freeze > requirements.txt)
- Make sure it contains all needed modules and libraries.
- Modify settings.py
    - Add Heroku to ALLOWED_HOSTS
    - Set DEBUG to "False"
- Create Procfile in root directory with the following content: web: gunicorn PP4_Cityfur.wsgi --log-file -
- Use python manage.py collectstatic in the local IDE terminal to collect all static files

**Step 1: Use Account**
- Create a Heroku account
- Log into the Heroku account

**Step 2: Create New App**
- On the dashboard, click "New" in the upper right corner.
- Select "Create new app"
- Select a name for the application - the name should only contain lowercase letters, numbers, and dashes.
- Choose a region. (Europe as we are in Europe)

**Step 3: Define Deployment Method**
- Select GitHub as deployment method
- Connect GitHub account to Heroku
- Select account and search for repository
- Connect to found repository

**Step 4: Settings**
- Switch to the settings page (Menu in the top)
- Click on "Reveal Config Vars"
- The following Key/Value pairs have been added:
    - DB_ENGINE
    - DB_HOST
    - DB_OPTIONS 
    - DB_PASSWORD
    - DB_PORT
    - DB_SSLMODE
    - DB_USER
    - SECRET_KEY
- In the next section, click on "Add buildpack"
- If not already selected, add Python.

**Step 5: Deploy Application**
- Switch to the deploy page (Menu in the top)
- Look under manual deployment
- Select a branch to deploy (Main in my case)
- Click "Deploy Branch"

**Step 6: Use App**
- Heroku will then set up the virtual environment with all packages, modules and libraries needed. (This can take some time)
- When Heroku is done with the deployment, click "View" and start to use the
- Use app
<br>

[The deployed version can be found here!](https://employee-management-072b60f670f5.herokuapp.com/)
<br>


### Testing

#### Validator Testing

<summary>W3C HTML Validation</summary>
<br>

All tests were conducted by copying the HTML code from the Google Chrome developer's tool and pasting into the [W3C HTML Validator](https://validator.w3.org/).
No errors were found when using the W3C HTML Validator.<br>
On three pages, information were shown about closing tags that have been automatically created by Django and don't have any influence on the pages' behavior.<br>




<summary>Jigsaw CSS Validation</summary>
<br>

No errors were found when using the [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/validator).<br>


<summary>JSHint Validator</summary>
<br>

No errors were found when using [JSHint](https://jshint.com).<br>




<summary>CI Python Linter</summary>
<br>

No errors were found when using the [CI Python Linter](https://pep8ci.herokuapp.com/).<br>
<br>





<summary>Lighthouse</summary>
<br>

No errors were found when using the [Lighthouse](https://lighthouse-metrics.com/).<br>

#### Manual Testing

The test where conducted on several different devices and browsers:
- Windows: Opera GX
- Windows: Chrome
- Windows: Firefox
- MacOS: Chrome
- iOS: Chrome



#### Possible Improvements

In a future version, the following improvements should be made:<br>

- Password reminder/reset function.
- Further customization for Employees.
- Further categorizing of selected workers (Employees) for Managers

#### Fixed Bugs

As the project was made step by step, slowly at a time, with constant guides/forums checked and knowledgeable friends helping me understand the procedure, there weren't any bugs taken note of.

#### Known Unfixed Bugs

No bugs witnessed at the time of writing the ReadME.<br>


## Credits

- The Employee Management System was written by me.
- My fellow classmate, Dennis Schenkel for answering my questions on Slack and for the general layout of the ReadME [Dennis Schenkel](https://github.com/DennisSchenkel)

<br>
As I found this topic very difficult, an endless amount of time has been spent on Google searches, various forums such as Reddit, Slack, Discord, ChatGPT (us students were told, using for simple questions AI is allowed, as long as it isn't more complex than looking up a question online).


### Acknowledgements

- Thanks to Kay for they effort as a facilitator of the Code Institute team.
- My real life good friend Thomas
