<div align="center">
<h1>Client Feedback</h1>
</div>

<br>

This Web App was created to complete the third Milestone Project for the Code Institute's Full Stack Developer course.
This is a Client Feedback webapp.
The MVP is based in Python using Flask framework to create all migrations and deployed in Heroku's.


Link to the web-application available [HERE.](https://feedback-dgroup.herokuapp.com/)

<br>
<div align="center">

![Home Page](https://github.com/rodrigodadam/PP3/blob/main/dgroup/static/dgrouplogo.png)

</div>
<br>

# Table of Contents

- [UX]()
  * [Project Goals](#Project-Goals)
  * [Users Experience Plan](#Users-Experience-Plan)
  * [Developer Strategy Plan](#Developer-Strategy-Plan)
  * [Front-End](#Front-end)


- [Features](#Features)

- [Technologies Used](#Technologies-Used)

- [Resources](#Resources)

- [Project Barriers & Solutions](#Project-Barriers-&-Solutions)

- [Deployment](#Deployment)

- [Credits](#Credits)


## Project Goals

The D Group Trade is an e-commerce company with their own website that also sells on ebay and amazon marketplaces. On eBay and Amazon they have the Feedback service provided from the marketplaces, however they haven't this pos-sale functionality in their own website.
So to help the company to better understand the customers I decided to create this WebApp in Python to link, in the future, to D Group's official website and ask our clients to give us feedback about the services and products that D Group sells.
 
The initial project is a MVP without complete CRUD, this is just a MVP with Create function to show to company directors how this will work and for Code Institute to complete the Milestone of Python essentials project.


## Users Experience Plan

The WebApp is designed for all D Group Customers who would like to give feedback about the company's product or services. This WebApp is consisted in a homepage and a success page. The homepage has a form with some fields to be completed and after the client submit the form, he'll be redirected to a success page to confirm that the form was submitted.

<div align="right"><a href="#top">🔝</a></div>


## Structure Plan


### Front-end

The WebApp consists in **Home** page, where the client can find the form with the follow fields to be completed, **Client Name**, **Rating** and **Comments**. The **success** page is a feedback return to the client to confirm that the form was sent to us.

<br>

- **Home Page** (`index.html`)

<br>

![Home Page](https://github.com/rodrigodadam/PP3/blob/main/dgroup/static/homepage.png)

<br>

The main page of the website. There is a form, and 1 submit button. 

<br>

- **Success Page** (`success.html`)

<br>

![Home Page](https://github.com/rodrigodadam/PP3/blob/main/dgroup/static/success.png)

<br>

This is a feedback page to confirm to the customer that the message has been sent and to thank them for their time.

<br>


<br>

<div align="right"><a href="#top">🔝</a></div>

<br>


### Design Plan


- **Colors**

For the background color I used (#F1ECEC) to avoid the white disturbment with the forms. To submit was used a similar color os D Group Logo (#FF7F00).

<br>


## FEATURES

### Existing Features

This project is well-structured to work efficiently, the current DataBase is postgres DB from Heroku's.

### Features Left To Implement

Build a complete CRUD and inset to D Group Admin panel to control all CRUD cicle.
Insert a pop up to give confirmation about the message sent.
Change to official D Group Database after aprovation.
Insert a new field with a list of all produts that D Group sells.


<div align="right"><a href="#top">🔝</a></div>

## TECHNOLOGIES USED

- [HTML5](https://en.wikipedia.org/wiki/HTML) 
- [CSS3](https://en.wikipedia.org/wiki/CSS) 
- [Google Fonts](https://fonts.google.com/) 
- [Font Awesome](https://fontawesome.com/) 
- [Gitpod](https://www.gitpod.io/) 
- [Git](https://git-scm.com/) 
- [GitHub](https://github.com/) 


<div align="right"><a href="#top">🔝</a></div>

## RESOURCES

### General Resources

- Code Institute Course Materials
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)

### Tools

- [ImageResizer](https://imageresizer.com/)
- [PostImages](https://postimages.org/)
- [Canva](https://www.canva.com/)
- [Balsamiq](https://balsamiq.com/)
- [ColorZilla](https://chrome.google.com/webstore/detail/colorzilla/bhlhnicpbhignbdhedgjhgdocnmhomnp)
- [Arty Click](https://colors.artyclick.com/)
- [AMI Website Mockup Generator](http://ami.responsivedesign.is/)
- [W3C Markup Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [Jshint](https://jshint.com/)
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)

<div align="right"><a href="#top">🔝</a></div>

## PROJECT BARRIERS & SOLUTIONS

- **DB-Link GitPod**

Was difficult to understand how to link the DB with gitpod. After a long time I checked that every time I needed to use set_pg before running the app. This was really complicated at first.

- **Deploy to Heroku**

In my first try the deployment had an error and failed a lot of times. However after a help from Code Institute Tutor that ask me about some item in my pipfile, I checked it with more care and I found the problem that my pipfile was starting with psql and not [[Source]]

### Test Strategy

Testing is required on all features and user stories documented in this README. All clickable links must redirect to the correct pages. 

 - HTML Code must pass through the [W3C HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffeedback-dgroup.herokuapp.com%2F)

 - CSS Code must pass through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ffeedback-dgroup.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=pt-BR)

- **Full Python test results can be found [here](https://github.com/rodrigodadam/PP3/blob/main/tests.md)**


## Deployment

### Project Creation

To create this project I used the CI Gitpod Full Template by navigating here and clicking the 'Use this template' button.

I was then directed to the create new repository from the template page and entered in my desired repo name, then clicked Create repository from template button.

Once created, I navigated to my new repository on GitHub and clicked the Gitpod button which built my workspace.

The following commands were used for version control throughout the project:

git add filename - This command was used to add files to the staging area before committing.

git commit -m "commit message explaining the updates" - This command was used to to commit changes to the local repository.

git push - This command is used to push all committed changes to the GitHub repository.


### Deployment to Heroku

Create application:

Navigate to Heroku.com and login.
Click on the new button.
Select create new app.
Enter the app name.
Select region.
Set up connection to Github Repository:

Click the deploy tab and select GitHub - Connect to GitHub.
A prompt to find a github repository to connect to will then be displayed.
Enter the repository name for the project and click search.
Once the repo has been found, click the connect button.
Set environment variables:

Click the settings tab and then click the Reveal Config Vars button and add the following:

key: DATABASE_URL, (postgress uri)
key: DEBUG, False
key: IP, 0.0.0.0
key: PORT, 5000
key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).
Enable automatic deployment:

Click the Deploy tab
In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.
Run Locally
Note: The project will not run locally with database connections unless the user sets up an env.py file configuring IP, PORT, DATABASE_URL and SECRET_KEY. You must have the connection details in order to do this. These details are private and not disclosed in this repository for security purposes.

Navigate to the GitHub Repository.
Click the Code drop down menu.
Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
Open your developement editor of choice and open a terminal window in a directory of your choice.
Use the 'git clone' command in terminal followed by the copied git URL.
A clone of the project will be created locally on your machine.
Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:

pip install -r requirements.txt

  <div align="right"><a href="#top">🔝</a></div>

## CREDITS

### ACKNOWLEDGEMENTS

My Dear Friend Rimom Costa for all support.
My Mentor Anthony for continuous helpful feedback.
All Code Institute Tutor Support.


<div align="right"><a href="#top">🔝</a></div>