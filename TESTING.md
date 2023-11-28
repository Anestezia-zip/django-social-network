# Volunteer Force - Testing

[Return to the README](README.md)

## Table of Contents
- [Performance](#performance)
  - [Google's Lighthouse Performance](#googles-lighthouse-performance)
- [Browser Compatibility](#browser-compatibility)
- [Responsiveness](#responsiveness)
  - [Smaller screens](#smaller-screens)
  - [Medium screens](#medium-screens)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [PEP8 Validation](#pep8-python)
  - [Javascript Validation](#javascript-validation)
- [Testing](#testing)
  - [Manual Testing](#manual-testing-bdd)
  - [Automated Testing](#automated-testing)
  - [Features Testing](#features-testing)

## Performance

### Google's Lighthouse Performance

Google Lighthouse was used to test the performance of the website.

#### Desktop Results:
<details><summary>Desktop</summary>
<img src="readme_img/validation/mobile_performance.png">
</details>

#### Mobile Results:
<details><summary>Mobile</summary>
<img src="readme_img/validation/mobile_performance.png">
</details>

## Browser Compatibility
|  Browser | Links  | Pages  | Responsivnes  | Form fields  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Microsoft Edge  | Works as expected| Loading pages no issue  |  Responsivness works as expected |  Works as expected |
|  Chrome | Works as expected  |  Loading pages no issue | Responsivness works as expected  | Works as expected  |
| Opera  |  Works as expected | Loading pages no issue  | Responsivness works as expected  |  Works as expected |

[Back to the table](#table-of-contents)

## Responsiveness
|   | Galaxy Fold  | Iphone SE   | iPhone12 Pro  | iPad mini  | desktop 1024px  |  desktop > 1200px | notes  |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
|  site is responsive >= 700px |  n/a | n/a  |  n/a | Good  | Good  | Good  |   |
| site is responsive < 700px  |  Good | Good  | Good  |  n/a | n/a  |  n/a |   |
| Links/URLs work  | Yes  | Yes   | Yes   |  Yes  | Yes   | Yes   |   |
|  Images work |  Yes  |  Yes  |  Yes  | Yes   | Yes   | Yes   |   |
| Forms work  |  Yes  |  Yes  | Yes   | Yes   | Yes   | Yes   |   |  

#  

<details><summary>Smaller screens Home</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700486061/volunteer/readme/aqbwsefqpg5bibhvcey3.jpg">
</details>
<details><summary>Smaller screens Post</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700486364/volunteer/readme/rtwgjiwmwpczug4mpm0k.jpg">
</details>
<details><summary>Smaller screens Profile</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700487059/volunteer/readme/er7euwpjebh5q9ar7acs.jpg">
</details>
<details><summary>Smaller screens Edit Profile</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700487101/volunteer/readme/rxfrjjpj6d9ammqb3m56.jpg">
</details>
<details><summary>Smaller screens Add new post</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700487134/volunteer/readme/fibnd8gbzpwaogkl9oug.jpg">
</details>
<details><summary>Smaller screens Edit post</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700488132/volunteer/readme/qh0klrhfuvykmebn73wu.jpg">
</details>
<details><summary>Smaller screens Deletion confirmation</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700487177/volunteer/readme/ojvrq1m2vbfx8p7kgy4k.jpg">
</details>
<details><summary>Smaller screens Donate</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700487296/volunteer/readme/t0m5nrc0lcqwtzk4odns.jpg">
</details>
<details><summary>Smaller screns Login</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700487985/volunteer/readme/q6ln36eh7y9qhu21jwgy.jpg">
</details>
<details><summary>Smaller screns Register</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700487940/volunteer/readme/z3n73msvlggpzhoh5weo.jpg">
</details>  


[Back to the table](#table-of-contents)

## Code Validation

### HTML Validation
The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.
Only profile page, I had to copy and paste code as I couldn't test as url page. Any error that is shown in validation test is cause of the Django templates. One particular that is shown accrosss website is **username** as username is displayed on navigation bar upon user login.

<details><summary>Login page</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700492237/volunteer/readme/g8vfhudhwh920n2f84pj.jpg">
</details>

<details><summary>Logout page</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700492074/volunteer/readme/qiolem93ydgxkcekvlna.jpg">
</details>

<details><summary>Signup page</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700492237/volunteer/readme/g8vfhudhwh920n2f84pj.jpg">
</details>

<details><summary>Home page</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700490822/volunteer/readme/ebwtd3s3losxat2np6eq.jpg">
</details>

<details><summary>Post detail page</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700491952/volunteer/readme/v8tkeovqcxoon51cnuds.jpg">
</details>

<details><summary>Profile page</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700493650/volunteer/readme/ft0q4zxhyfmxwp2jg66x.jpg">
</details>

<details><summary>Donate page</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700493804/volunteer/readme/jmx3ynzkqikrt5kvxdk9.jpg">
</details>

### CSS Validation 
[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) was used for validating the CSS stylesheet. CSS file was tested by manually copying the CSS codes into the manual input option.

<details><summary>CSS Validation</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700494217/volunteer/readme/nqtbcjcborsomhvvpsm1.jpg">
</details>  

### PEP8 Python
[PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) was used to check that the Python code meets PEP8 standards.

<details><summary>Admin</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1701181748/volunteer/readme/mfl9qqyxn6otdqsmykho.jpg">
</details>

<details><summary>Forms</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1701182024/volunteer/readme/hbw7sbhgisncmgx6ckuy.jpg">
</details>

<details><summary>Views</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700566387/volunteer/readme/r5risaf5fgxrwown6y6m.jpg">
</details>

<details><summary>Models</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700562120/volunteer/readme/bammrmn98y5kxkbpmiet.jpg">
</details>

### JavaScript Validation

[JSHint Static Code Analysis Tool](https://jshint.com/) for JavaScript was used to validate the Javascript file. There was 1 warning for a variable named 'new' and 1 undefined variable. As that code was copied from other websites, I didn't change it as it would affect the code itself. No other errors or warnings are shown.

<details><summary>JS</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700494457/volunteer/readme/iwzhii2z7jzx5mfuksfc.jpg">
</details>  

[Back to the table](#table-of-contents)

# Testing

## Manual Testing

User Story |  Test | Pass
--- | --- | :---:
As a **first-time visitor**, I want to understand the purpose of the website and easily navigate through | Once on the homepage, I see a large navigation bar with links, and below the navigation is a large image with hero text and "I can help" and "I need help" buttons Without scrolling further down the page, I can understand the purpose of this site | &check;
As a **first-time visitor**, I can scroll down the page and see an interactive map | Scrolling down to the bottom of the main page, I see a large interactive map, where I can visit the red icons of houses and see a modal with information about the destruction. Also by clicking on one of them - you can view full-size photos | &check;
As a **first-time visitor** I want to be able to view the posts so that I would get quick access to relevant information and get a better understanding of the content| I can easily scroll down the page and find posts on different topics. If I want to get more information about a post, I just need to click on its photo or title, which will redirect me to the post_detail page |&check;
As a **first-time visitor** I want to be able to register an account to have more access to the website | In the navigation bar there is a button 'Register' which will lead me to the register page on which I have to fill in all information to register for the website | &check;
As a **registered user** I can add, update or delete my posts so that have more control over my content in case of errors, and to have better engagemant with other users | If my post already exists update and delete button should be displayed top right of the card! Clicking on the update icon new template is displayed to update post. Clicking on delete button modal is shown to the user to confirm his actions. Once deleted that post no longer exist.  |&check;
As a **registered user** I want to be able to update my profile information so that I could change my username, bio, role and add a profile picture | After logging in to the website I can click on the "Profile" in the navbar which will lead me to a profile page. Page is divided into two sections, one is displaying current information for the user and the other gives the user the option to implement CRUD functionality | &check;
As a **site owner**, I want to be able to create, update and delete posts so that I can control my website content. |After logging in to the admin panel of the website I can navigate myself to Post model and perform CRUD functionality for the posts| &check;
As a **site owner**, I want to be able to delete users so that I can receive several benefits such as: managing my data, reducing liability & resource optimization| After logging in to the admin panel of the website I can navigate myself to Users which is Django all auth model in which are displayed all registered users, from that model I can either update or delete specific users| &check;

## Automated Testing

I performed several automated tests for views, models and forms. Running all the tests seemed to me a time-consuming and difficult task, although now I understand what testing is and why it is important to create test cases for code.

<details><summary>Admin</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700563887/volunteer/readme/h6zu2bdcm2fedgec3omo.jpg">
</details>

<details><summary>Forms</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700563247/volunteer/readme/nl8giafbwk4yxsrt8run.jpg">
</details>

<details><summary>Views</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1701182222/volunteer/readme/v2if9c4vypellpbp9lsk.jpg">
</details>

<details><summary>Models</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1701182222/volunteer/readme/v2if9c4vypellpbp9lsk.jpg">
</details>

<details><summary>Coverage Report</summary>
<img src="https://res.cloudinary.com/dyadwedsy/image/upload/v1700571714/volunteer/readme/xajkqalhbprqgsjkwmdt.jpg">
</details>

[Back to the top](#table-of-contents)