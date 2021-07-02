# MS4-PROJECT-GameWork

![alternativetext]()

[View the live project here](https://ms4-social-network.herokuapp.com/)

---

# Table of contents

* [UX](#ux)
* [Features](#features)
* [Screenshots](#screenshots)
* [Design](#design)
* [Technologies](#technologies)
* [DB Schema](#db)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Contact](#contact)

---

## User Experiance (UX)

## User stories

*  First Time Visitor Goals

    * As a First Time Visitor, I want to easily understand the main purpose of the site.
    * As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
    * As a First Time Visitor, I want to be able to visit the website on every device, so that I can look at the website on desktop, mobile and tablet.
    * As a First Time Visitor, I want to it to be easy to register as a new user.
    * As a First Time Visitor, I want to get a professional presentation of the site with no or very little bugs.

* Returning Visitor Goals
    * As a Returning Visitor, I want to be able to edit, delete and create notes.
    * As a Returning Visitor, I want to know if a note is urgent or not.
    * As a Returning Visitor, I want to find the best way to get in contact with the creator with any questions I may have.

*  Frequent User Goals
    * As a Frequent Visitor, I want to make sure that an admin that can reach my notes and make changes if I for some reason cannot.
    * As a Frequent Visitor, I want a profile page that I can edit.
    * As a Frequent Visitor, I want to find community links so that I can join and interact with others.


## Features

* Existing Features

    * Responsive on all device sizes

    * Design
        * An attractive and simple layout.
        * Simple navigation throughout the website by using the navigation bar.
    
    * General
        * There are links to the social media platforms at the bottom of the website.
        * A contactform for people to contact me.
    
    * Register, login and logout
        * User can create a new account on the web application.
        * User can login with their existing accounts.
        * User can easily log out.
        * If a user creates a new account, logs in or logs out, a flashed message will appear with the action the person has done.
        * The password is saved in mongo db with a random password generated which make the password secury for the user.

    * Feature ideas to Implement
        * The user can delete their profile.
        * Display a nice profile page for the user.
        * Make a calender that you can put the notes in.
        * Make a public switch so you can choose if you want your notes to be public or private.

---

## Testing User Stories from UX Section

##  First Time Visitor Goals

* As a First Time Visitor, I want to easily understand the main purpose of the site
    - The name of the website is called "notebook". Indicitaing that this is website is about keeping notes.
    - The background image for the whole page is of a workspace with a headline reading: "Keep an eye on what you should do". This is to signal visitors that the purpose of this site is to centralise and observe ones tasks.
* As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
    - At the top of the page there is a navigation bar, each link describes what the page contents of.
    - If the user feels lost, he/she can always press on the "Home" link in the navigation bar or the "NB" icon to be redirected the homepage.
    - When there is content below the visible page there is a pulsating arrow pointing downwards to indicate there is more to show on this page.
* As a First Time Visitor, I want to be able to visit the website on every device, so that I can look at the website on desktop, mobile and tablet.
    - The website is responsive on mobile, tablet and desktop.
* As a First Time Visitor, I want to it to be easy to register as a new user.
    - For first time users, or users who hasn't yet logged in, there is only three options in the top navigation bar; Home, Log in and Register. There is also a log in and reigster link in the center of the homepage.
* As a First Time Visitor, I want to get a professional presentation of the site with no or very little bugs.
    - I've done a lot of bug testing to make sure that the user is left with a site that is well-working.
    - I went for a clean look that doesn't contain irrelevant information or annoying colors and images.

## Returning Visitor Goals

* As a Returning Visitor, I want to be able to edit, delete and create notes.
    - Notes can easily be created via a page that is reachable from the top navigation bar, called "new note". Here users can set note "name", description, due date and if it's urgent.
    - Each note can be edited or deleted by opening the note via the "notes" page. 
* As a Returning Visitor, I want to know if a note is urgent or not.
    - Each note has the possibility to enable an urgent mark to indicate that this particular note needs to be adressed very soon. The urgent mark will show next to note without having to open it.
* As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.
    - At the bottom of the homepage there is contact form which the user can use to get in contact with the creator of the page.

##  Frequent User Goals

* As a Frequent Visitor, I want to make sure that an admin that can reach my notes and make changes if I for some reason cannot.
    - There is a Admin login that holds all notes created. Here he or she can edit or remove every single note.
* As a Frequent Visitor, I want a profile page that I can edit.
    - There is a profile page that in the future could hold an image as a profile picture.
* As a Frequent Visitor, I want to find community links so that I can join and interact with others.
    - The Facebook, Instagram and Twitter page can be found at the bottom of the homepage. The community links is not enabled since there is no community yet.

## Here is some examples of bugs that I encounterd during testing:


#### This is a selection of screenshots of bugs that are now fixed.

* In this first picture the urgent text and icon was not aligned with the rest. This happened only on smaller screens. By making the form wider and setting the font-size to a smaller one, the aligment issue was fixed. 
    * Screenshot of Bug1 - [View](static/files/bugs/Screen1.jpg)

* In this bug the buttons for the edit screen was misplaced. The issue here was similar to the previous bug. By making the font-size smaller and shorten the "edit note" to only "edit", the buttons aligned better.
    * Screenshot of Bug2 - [View](static/files/bugs/Screen2.jpg)

* In this last bug the arrows that point downwards to indicates more space below, was too far up and merging with the nearby buttons. This was also an issue that was only found in smaller screens. By adding a top margin in css the arrows was properly placed.
    * Screenshot of Bug3 - [View](static/files/bugs/Screen3.jpg)

---

# Technologies

### Languages Used
* [HTML5](https://sv.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JQuery](https://sv.wikipedia.org/wiki/JQuery)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework)))

### Design

* #### Colour Scheme
    * The color i used for background is a gradient, black and blue.

* #### Typography
    * The Orbitron font is the main font used throughout the whole website.

* #### Imagery
    * Imagery is important. The large, background hero image is designed to be striking and catch the user's attention. It also has a modern, energetic aesthetic.

* #### Wireframes
    * Wireframe Landing Page - [View]()
    * Wireframe Post list and Post detail - [View]()
    * Wireframe Profile page - [View]()
    * Wireframe Donation - [View]()

### Frameworks, Libraries & Programs Used

* Bootstrap 5:
    * Bootstrap 5 was used to assist with the responsiveness and styling of the website.
* Photoshop:
    * Photoshop was used to create the picture on the devices.
* Google Fonts:
    * Google fonts were used to import the 'Montserrat' font into the style.css file which is used on all pages throughout the project.
* GitHub:
    * GitHub is used to store the projects code after being pushed from Git.
* Git:
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* Gitpod:
    * GitPod is used to develop the project.
* AWS:
    * AWS is the fully managed cloud database service used for the project.
* Heroku:
    * Heroki is the platform to deploying the app.
* Django:
    * Django is the web framework used to provide libraries, tools and technologies for the app.


---

## DB Schema

Generate DB Image:

`python manage.py graph_models -a > dotfile.dot`
[https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16]()

---

# Testing

### My methods for testing my webpage consisted of:

* Chrome DevTools is used to detect problems and test responsiveness.
* W3C Markup Validation Service
    * The W3C Markup Validation Service is used to check whether there were any errors in the HTML5 code.
* W3C CSS validator
    * The W3C CSS validator is used to check whether there were any errors in the CSS3 code.
* PEP8
    * The PEP8 validator is used to check whether there were any errors in the Python code.

* In the future I plan to implement automated tests.

---

## Deployment
--- 
### Requirements
* Python3
* Github account
* AWS account
* Heroku account

### Clone the project
To make a local clone, follow the steps:

1. Log in to GitHub and go to the repository.
2. Click on the green button with the text “Code”.
3. Click on “Open with GitHub Desktop” and follow the prompts in the GitHub Desktop Application or follow the instructions from [this link](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to see how to clone the repository in other ways.

### Working with the local copy

1. Install all the requirements: Go to the workspace of your local copy. In the terminal window of your IDE type: pip3 install -r requirements.txt.
2. Create a database in MongoDB
    * Signup or login to your MongoDB account.
    * Create a cluster and a database.
    * Create four collections in the db: categories, recipes, subscribers, users.
    * Add string values for the collections.
3. Create the environment variables
    * Create a .gitignore file in the root directory of the project.
    * Add the env.py file in the .gitignore.
    * Create the file env.py. This will contain all the envornment variables.
    
            Import os
            os.environ.setdefault("IP", "Added by developer")
            os.environ.setdefault("PORT", "Added by developer")
            os.environ.setdefault("SECRET_KEY", "Added by developer")
            os.environ.setdefault("MONGO_URI", "Added by developer")
            os.environ.setdefault("MONGO_DBNAME", "Added by developer")
    
4. Run the app: Open your terminal window in your IDE. Type python3 app.py and run the app.

### Heroku Deployment

1. Set up local workspace for Heroku
    * In terminal window of your IDE type: pip3 freeze -- local > requirements.txt. (The file is needed for Heroku to know which filed to install.)
    * In termial window of your IDE type: python app.py > Procfile (The file is needed for Heroku to know which file is needed as entry point.)
2. Set up Heroku: create a Heroku account and create a new app and select your region.
3. Deployment method 'Github'
    * Click on the Connect to GitHub section in the deploy tab in Heroku.
        * Search your repository to connect with it.
        * When your repository appears click on connect to connect your repository with the Heroku.
    * Go to the settings app in Heroku and go to Config Vars. Click on Reveal Config Vars.
        * Enter the variables contained in your env.py file. it is about: IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME
4. Push the requirements.txt and Procfile to repository.

        $ git add requirements.txt
        $ git commit -m "Add requirements.txt"

        $ git add Procfile 
        $ git commit -m "Add Procfile"
5. Automatic deployment: Go to the deploy tab in Heroku and scroll down to Aotmatic deployments. Click on Enable Automatic Deploys. By Manual deploy click on Deploy Branch.

- Heroku will receive the code from Github and host the app using the required packages. Click on Open app in the right corner of your Heroku account. The app wil open and the live link is available from the address bar.
---

# Credits

## Content

* On the home page i found a nice arrow with shows the visitors that theres more content on the page when you scroll down
    * [Link - Codepen]()
* The background image that i have on all pages
    * [Picture - Pixabay]()
* On the Profile page Profile picture
    * [Picture - Pixabay]()
* To display error handlers pages in a nice way i choose this picture
    * [Picture - Pixabay]()
* The video i looked at to get it right with the error handling
    * [Video - Youtube]()
* Icon i use in the header
    * [Icon - Iconfinder]()
* The 3D text i used for the error handling page.
    * [3D text - Codepen]()
* I used this site to transform scss to css from the link above.
    * [Css to Scss - Cssportal]()

## Acknowledgements

Thanks to the following people and organizations who helped or inspired me for the project:

* My Mentor for continuous helpful feedback.
* Tutor support at Code Institute for their support.
* The lessons and knowledge of [Code Institute](https://codeinstitute.net/).
---

## Contact

E-mail: Linus.loof96@gmail.com






