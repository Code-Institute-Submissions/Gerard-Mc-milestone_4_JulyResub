# Deployment

## Local Deployment

Gitpod, an integrated development environment, was used to code this project. Github was used for version control and storing the project's files remotely.

To run this project you will need to perform the following steps.

### Install Technologies to Your Computer

[PIP](https://pip.pypa.io/en/stable/installing) to install the project's requirements.
[GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning the project and version control.
[Python](https://www.python.org/download/releases/3.0/) to run the project. 

### Clone the Repository

You will need to clone the site's repository.
To do this,  enter `git clone https://github.com/Gerard-Mc/milestone_4.git` into your terminal.
After the repository is cloned, change IDE directory to the one created after cloning by typing `cd <path to project folder>` into yor terminal.
You will find more information on cloning repositories [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)

### Create Accounts

The website requires a Stripe, Gmail, and AWS account.
You will find links to them below.
[Stripe](https://stripe.com/)
[Gmail](https://www.google.com/)
[AWS](https://aws.amazon.com/)

### Set up Environment Variables
* Create a .env file in the root directory.
* If not already included in the .gitignore file, make sure to add it otherwise your environment files will be visible to the public.
* Paste the following code into the .env file and input the values found in your Stripe account.
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"    
```
More information on setting up Stripe keys can be found [here](https://stripe.com/docs).

### Install Required Packages

To install the required packages, input `pip3 install -r requirements.txt`
in your terminal.

### Create Database
* You will need to make migrations by inputting `python3 manage.py makemigrations` into your terminal.

* Migrate this data by inputting `python3 manage.py migrate` into your terminal.

### Create a Super User

To access the website's admin to create objects, you will first have to create an admin account.
* Input `python3 manage.py createsuperuser` into your terminal.
* Follow the steps by inputting a username, email(optional), and a password.
* To open admin, you will need to open the website. To do this type `python3 manage.py runserver` in your terminal and an option to open the website should be available in your IDE.
* After you open the website, add `/admin` to the end of the websites URL to open Admin.
* Click categories and create 4 different categories ensuring all 4 names are used and used only once. You can input whatever you wish into the friendly name and price fields.
The database and website should now work as expected.
