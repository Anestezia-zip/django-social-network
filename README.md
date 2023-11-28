# Volunteer Force
​
Welcome to the Volunteer Force, an online platform dedicated to connecting volunteers and organizations. Our website serves as a central space for individuals seeking to make a difference and organizations in need of passionate volunteers.

With Volunteer Force, you can discover a multitude of volunteer opportunities, ranging from local community events to global initiatives. Whether you're an enthusiastic volunteer eager to contribute your time and skills or an organization looking for dedicated individuals, our platform is here to bridge that gap.

Join us in creating positive change, empowering communities, and fostering a culture of giving back. Explore, engage, and make an impact with Volunteer Force.
  
![Am i responsive image](https://res.cloudinary.com/dyadwedsy/image/upload/v1701200804/volunteer/readme/z2n5rwyydjxpp7is66ql.jpg)  
​
[Click Here To Visit Live Site](https://django-volunteer-force-daec5f5fae54.herokuapp.com/)  
​
## Table Of Contents:
1. [Planning](#planning)
    * [User Stories](#user-stories)
    * [Agile Methodology](#agile-methodology)

2. [Features](#features)
    * [Navigation](#navigation-bar)
    * [Footer](#footer)
    * [Home page](#home-page)
    * [Single post page](#single-post-page)
    * [Profile page](#profile-page)
    * [Login page](#profile-page)
    * [Sign up page](#signup-page)
​
3. [Technologies Used](#technologies-used)
4. [Libraries](#libraries)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
​
## Planning:

### User Stories
#### First time visitor
- As a first-time visitor, I want to understand the purpose of the website and easily navigate through
- As a first-time visitor, I want to be able to view the posts so that I would get quick access to relevant information and get a better understanding of the content
- As a first-time visitor, I want to be able to register an account to have more access to the website
#### Registered User
- As a registered user I can update or delete my posts so that have more control over my content in case of errors, and to have better engagemant with other users
- As a registered user I want to be able to update my profile information so that I could change my username, add a profile picture, bio
#### Site owner
- As a site owner, I want to be able to create, update and delete posts, regions and users so that I can control my website content

[Back to the table](#table-of-contents)
  
### Agile Methodology
Agile methodology was used in the planning of this project. I found it difficult to work on agile and coding in parallel as I was on team 1 and was aware of the changes, so I found it confusing. Afterwards, however, I developed the habit of adding tasks before directly doing them. 
I used Github and Project Board using Kanban board:

![Project Board](https://res.cloudinary.com/dyadwedsy/image/upload/v1700406352/volunteer/readme/board_w2emid.jpg)  

[Back to the table](#table-of-contents)

## Features:

### Navigation Bar
- The navigation bar is located at the very top of each page, and it is a "sticky" navigation bar, i.e. if the page is longer and the user has to scroll down, the navigation bar stays at the top of the page the whole time! The logo is on the left, the navigation links are on the right.
- The logo is clickable and redirects the user to the home page.
- When logging in, the user is shown their username and the login/register button is replaced with an exit button. A dropdown menu also appears with a link to "Profile" and "Add New Post".
- On large and xx-large screens, the navbar is centered on the page and is sized by the bootstrap class.
- On medium and small screens, the navigation menu is changed to a hamburger menu, which displays all navigation links when clicked.  

  <details><summary>Navbar</summary>
  <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700407527/volunteer/readme/navbar_wcg2pj.jpg">
  </details>

### Footer
- The footer is at the bottom of each page and is in a dark blue-orange color, responsive for tablets and mobile devices.

### Home Page
- The home page has a section with a parallax effect and two buttons that lead to registration. When a user is registered - the buttons disappear. The section is adaptive: it changes the font to a smaller one, as well as the text that was in a row - becomes in a column.  

  <details><summary>Home page</summary>
  <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700408097/volunteer/readme/hero_mldiqt.jpg">
  </details>
​

    Posts section

- There are adapted cards with user posts, which are arranged in 3 columns on large screens, in 2 columns on medium screens and full width on mobile devices.
- On this page the user have option to use "search bar" to find specific posts or he can scroll down to search for post that he would like to get more information about it
- If input on search box is not empty the user will be redirected to the new page which will eaither displayed match post or display message to the user 
- Posts are displayed in 2 columns with 3 posts per row, each post contains of: image, author, date, indicator of likes and comments and title and brief description 
- Posts card are scaling up as the user hovers over them and clickable title and ecerpt are transforming to capitalize letter
- When clicked on title/excerpt user is redirected to another page which will give a user more information about the post.  

  <details><summary>Posts section</summary>
  <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700408396/volunteer/readme/posts_cxpjto.jpg">
  </details>
​

    Map section

- Interactive map of Ukraine, where pointing at the red houses - with the help of hover effect the user sees a modal window with a description of each destruction, and clicking on the modal - will be able to see full-size photos

  <details><summary>Map of Ukraine</summary>
  <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700411956/volunteer/readme/map_dq8awy.jpg">
  </details>

### Single post page
- A user can go to this page by clicking on a photo or title and get a description of a particular post and all the necessary information about it. And also see the date when the post was created.  

  <details><summary>Post detail page</summary>
  <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700408565/volunteer/readme/posts_vs5zn9.jpg">
  </details>

### Profile page
- The profile page consists of 2 sections:
    - The first section at the top of the screen displays the user's current information, their avatar and the role they chose when registering. If we click the "Edit profile" button, we see a standard django form that allows the user to change their information about themselves, as well as add a "bio" and profile picture if they want to.


        <details><summary>Profile page - User Info</summary>
        <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700408994/volunteer/readme/posts_flncaq.jpg">
        </details>  

    - The bottom section displays the posts that belong to the registered user, as well as the "Add new post" button to add a new post.

         <details><summary>Profile page - User Posts</summary>
        <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700409043/volunteer/readme/profile_xt1i9j.jpg">
        </details>  

### Login page
- The login page is a basic django allauth form, containing 2 input fields for username and password with a "Login" button below it. There is also an option below to log in using google provider.
- The user also has a link above the form to register on the site if they don't have an account, which redirects the user to the "Register" page.

    <details><summary>Login page</summary>
    <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700409951/volunteer/readme/profile_vbvusy.jpg">
    </details>

### Signup page
- The registration page is also a standard django form with all the required fields for user input.
- The user must enter all information (username, first name, last name, e-mail and password). 
- After entering all fields and clicking the registration button, the user will be automatically logged in and redirected to the main page of the site.
- It is also possible to register with the help of Google provider

    <details><summary>Sign up page</summary>
    <img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700409973/volunteer/readme/signup_vmssf6.jpg">
    </details>

[Back to the table](#table-of-contents)

## Technologies Used
- [HTML](https://en.wikipedia.org/wiki/HTML) was used for the mark up.
- [CSS](https://en.wikipedia.org/wiki/CSS)  was used to style the site.
- [Django](https://www.djangoproject.com/) was the framework that was used.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), django is a python framework.
- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)) was also used to style the site.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for interactiveness.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) is used to host this site.
- [Github](https://en.wikipedia.org/wiki/GitHub) was used to store the code.
- [Git](https://en.wikipedia.org/wiki/Git) was used for version control.
- [Cloudinary](https://cloudinary.com/) was used to store the images.
- [ElephantSQL](https://www.elephantsql.com/) was used to store the database.

[Back to the table](#table-of-contents)

## Libraries
- asgiref - A standard Python library to allow for asynchronous web apps and servers to communicate with each other.
- cachetools - Library providing caching tools and decorators for Python functions.
- cloudinary - A Python package allowing integration between the application and Cloudinary.
- coverage - Is a third-party package that helps developers measure code coverage in their Python codebase.
- debugpy - A debugger for Python that can be used to debug code during execution.
- dj-database-url - A Django utility to utilise the DATABASE_URL environment variable to configure the Django application. Used with PostgreSQL.
- dj3-cloudinary-storage - A Django package that facilitates integration with Cloudinary storage.
- Django - A python package for the Django framework.
- django-allauth - An integrated set of Django applications addressing user authentication, registration and account management.
- django-autoslug - Django library for automatically generating slugs for URL-friendly titles.
- django-ckeditor - Is a third-party package that provides a rich text editor widget for Django web applications.
- django-debug-toolbar - helps you understand how your application functions and to identify problems. It does so by providing panels that provide debug information about the current request and response.
- django-js-asset - Django integration for managing JavaScript assets.
- gunicorn - A Python WSGI HTTP Server for UNIX.
- oauthlib - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.
- psycopg2 - A PostgreSQL database adapter for Python.
- pytz - A Python package for world timezone definitions, modern and historical.
- Pillow - A Python Imaging Library adds image processing capabilities
- sqlparse - A non-validating SQL parser for Python.
- Unidecode - Transliterates Unicode characters to ASCII, useful for handling non-ASCII characters in text.

[Back to the table](#table-of-contents)

## Testing
The testing section can be found [here](TESTING.md).

## Bugs
| **Bug** | **Fix** |
| ----------- | ----------- |
| The site loads faster than the photo appears in src, so when you first sign up, you see alt text instead of the avatar | Moved default link in model and added condition **{% if user_profile.avatar.url %}** to profile |
| The registration form defied stylization| Found the id of each input in devtools and stylized them |
| Inputs were popping out of shape on small screens| Created a media query where I changed the width to a percentage. |
| The user image wasn't uploading after updating profile| Added code in the form = 'enctype="multipart/form-data"'|
| Changed the folder to Cloudinary to separate the files and there was an image error | Instead of creating a new folder, created a new preset and added it to settings and models | 
| No css style on Heroku | Before every deployment set debug to false and run "python3 manage.py collectstatic" |

[Back to the table](#table-of-contents)


## Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Create a database On ElephantSQL
- Log into the [ElephantSQL](https://www.elephantsql.com/) website and click **Create new Instance**
- Enter a **Name** and keep the plan as **Tiny Turtle Free**, then **tags** field can be left blank, Select a region closest to you, I selected **EU-West-1(Ireland)** as I'm in Ireland. Then click **Review** and afterward click **create an instance**.
- On The Dashboard click on your database instance name.
- You will see the details for your database instance, in the URL section click on the copy icon to copy the database URL.
- Head over to gitpod and create a **Database URL** environment variable in your env.py file and set it equal to the copied URL.

#### Deploying to Heroku.
- Head back over to [heroku](https://www.heroku.com/) and click on your **app** and then go to the **Settings tab**
- On the **settings page** scroll down to the **config vars** section and enter the **DATABASE_URL** which you will set equal to the elephantSQL URL, create **Secret key** this can be anything,
**CLOUDINARY_URL** this will be set to your cloudinary url and finally **Port** which will be set to 8000.
- Then scroll to the top and go to the **deploy tab** and go down to the **Deployment method** section and select **Github** and then sign into your account.
- Below that in the **search for a repository to connect to** search box enter the name of your repository that you created on **GitHub** and click **connect**
- Once it has been connected scroll down to the **Manual Deploy** and click **Deploy branch** when it has deployed you will see a **view app** button below and this will bring you to your newly deployed app.
- Please note that when deploying manually you will have to deploy after each change you make to your repository.
- - -

[Back to the table](#table-of-contents)

## Credits
- [W3schools](https://www.w3schools.com/) this was great for looking up forgotten **CSS** syntax and how to use it.
- [CodeInstitute](https://learn.codeinstitute.net/) for their walkthrough project, which guided me with website build especially for publishing posts, comments and likes section which I code along with the video with few adjustments.
- [Allauth](https://django-allauth.readthedocs.io/en/latest/) for their documentation which was helpfull in creating user authentication.

[Back to the top](#volunteer-force)