# Volunteer Force
​
Welcome to the Volunteer Force, an online platform dedicated to connecting volunteers and organizations. Our website serves as a central space for individuals seeking to make a difference and organizations in need of passionate volunteers.

With Volunteer Force, you can discover a multitude of volunteer opportunities, ranging from local community events to global initiatives. Whether you're an enthusiastic volunteer eager to contribute your time and skills or an organization looking for dedicated individuals, our platform is here to bridge that gap.

Join us in creating positive change, empowering communities, and fostering a culture of giving back. Explore, engage, and make an impact with Volunteer Force.
  
![Am i responsive image](readme_img/responsive/responsive.png)  
​
[Click Here To Visit Live Site](https://blog-hike.herokuapp.com/)  
​
## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)
    * [Agile Methodology](#agile-methodology)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)
    
2. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [Footer](#footer)
    * [Home page](#home-page)
    * [Post page](#post-page)
    * [Single post page](#single-post-page)
    * [Profile page](#profile-page)
    * [Login page](#profile-page)
    * [Sign up page](#signup-page)
​
3. [Future Features](#future-features)
4. [Technologies Used](#technologies-used)
5. [Libraries](#libraries-used)
6. [Testing](#testing)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)
​
## Design & Planning:
​
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

  
### Agile Methodology
The Agile Methodology was used to plan this project. I found it hard to work parallel on agile and on my coding as I was team of 1 and was aware of the changes so I found that to be confusing. I had to add a few things at the end of my project in github repository. I did learn more towards the end of the project about the use of the agile develepment, and why it's important and usefull to keep track of the whole process and to implement as much as you can. 
I've used Github and the Project Board with use of the Kanban board.
​
I devided project board into 3 sections:
​
  -  To-Do- (All the User stories were initially entered in the 'To Do' column)
  -  In Progress- (then during development story they were moved into the 'In Progress' column)
  -  Done- (and then finally they get moved into 'Done' once the development completes)
​
<details><summary>Project board</summary>
<img src="readme_img/test/project_board.png">
</details>
​
- I've planned 5 itterations for this project. Four were completed as planned and fifth one is for future development of the webiste, which is described more in feature features in this document
​
<details><summary>Milestones</summary>
<img src="readme_img/test/milestone.png">
</details>
​
- Each milestone consist of user stories, which are displayed either open or closed depends on the progress.
Each user story is labeled either as 'must-have', 'should-have' or 'could-have'depending of the needs of the project with estimated story points attached.
​
<details><summary>Milestone detail</summary>
<img src="readme_img/test/mls_det.png">
</details>
​
- Each user story have acceptance criteria and tasks that needed to be done to accomplish  that criteria
 
​
<details><summary>User story detail</summary>
<img src="readme_img/test/user_story_detail.png">
</details>
​
### Typography
I chose to use "Dosis" font family beacuse it's easily readable on both small and large screens, making it a great option for websites and digital interfaces. It's clean with moder apperance. As a backdrop font I've used 'Sans-serif'.
​
### Colour Scheme
For this website, I decide to keep the main color scheme very simple.Text was either  white or black with background of certain cards and the footer beeing light red/orange color while the rest of the background is white.
I kept consistant colours for buttons and links on the website. All buttons have hover effect of "Robin egg blue" except 'Delete & Update' button which are standard red and blue colored.
  
<details><summary>Color palette</summary>
<img src="readme_img/page_screen/palete.png">
</details>
​
​
### DataBase Diagram
Below is the database diagram that I created using LucidCharts.
​
<details><summary>DataBase diagram</summary>
<img src="readme_img/wireframes/dtb.jpeg">
</details>
​
## Features:
​
### Navigation Bar
- The Navigation bar sits at the very top of each page, and it's sticky navbar which means when page is longer and user has to scroll down the navbar will stay on top of the page all the time! The logo is at the left side and the navigation links are in the middle with login/signup buttons on the right.
- Logo is clickable and redirects user back to the home page
- When logged in new link is displayed to the user: "Profile" ,and login/signup button is replaced with Logout button. Also user name is displayed next to the logo.
- The Navbar background is white with opacity set to 75%.
- On large to xx-large screens the navigation bar is in the center of the page and is sized by the bootstrap class.
- The active page (page that the user is currently on) is displayed in coloured text, this makes it stand out much more and is clear to the user which page they are on.
- When on medium to small screens the navigation menu changes to burger menu which shows all the nav links when clicked on.
  
<details><summary>Navbar</summary>
<img src="readme_img/test/navbar_login.png">
</details>
​
<details><summary>Navbar medium screens</summary>
<img src="readme_img/test/navbar_mob.png">
</details>
​
### Footer
- The footer is found at the bottom of every page and is responsive for tablet and mobile too in its orange color.
- It displays the logo in the left corner, social links (Youtube, Facebook, Twitter & Youtube) are in the middle of the footer and, the Subscription field is on the right side of the footer.
- When any of the icons are clicked the social media site opens on a separate tab, this way the user still has the main website open, also by clicking on thelogo the user is redirected to the home page.
- Copyright text sits at the bottom of the footer
  
<details><summary>Footer</summary>
<img src="readme_img/test/footer.png">
</details>
​
### Home Page
- The home page has a dark hero image with text gradually displaying and deleting indicating site purpose
- Bellow hero image there are two sections which describe the owner of the page and his reach to the community with icons and numbers
- map?
<details><summary>Home page</summary>
<img src="readme_img/home_page.png">
</details>
​
​
### Posts page
- On this page the user have option to use "search bar" to find specific posts or he can scroll down to search for post that he would like to get more information about it
- If input on search box is not empty the user will be redirected to the new page which will eaither displayed match post or display message to the user 
- Posts are displayed in 2 columns with 3 posts per row, each post contains of: image, author, date, indicator of likes and comments and title and brief description 
- Posts card are scaling up as the user hovers over them and clickable title and ecerpt are transforming to capitalize letter
- When clicked on title/excerpt user is redirected to another page which will give a user more information about the post
​
<details><summary>Posts page</summary>
<img src="readme_img/test/post_page.png">
</details>
​
  
### Single post page
- On this page, the user can have a brief description of the certain post that he clicked on and get all relevant information about it
- Bellow post section register user can like/unlike post
- User can leave comment
- After the user posts his comment he will be prompted with the message that says "comment is waiting for approval"
- If user has already left comment he has option to either update his comment or delete it by simply clicking either of displayed buttons
- By clickin "Delete" button user will be asked to confirm his choice,...