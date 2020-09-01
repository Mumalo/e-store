# IASHOP (Online Bidding System)

IASHOP is an e-shopping site where users can post, sell items, bid and advertise items.

## Description

Sellers can post items and either place them on direct sale or on bid. 
Buyers create bid on items or purchase them directly(depending on the state of the item and if owners are willing to sell)
Users can also post their Budget plans (which enlist what they are willing to purchase, when and at what cost)
Apart from the above features, users can rate items, see system notificatons, follow/unfollow other users and perform other functions

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

1. Clone the project from github, into a desired source folder
2. Make sure python and pip are installed on your system 
3. Before installing django and other dependencies, set up virtulenv 
4. create a virtual environment as below
  type python3 -m venv myvenv in the terminal (myvenv is the name of your virtual environment)
5. Install requirements from the requirements.txt file by:
   i. Navigating to the directory containing requirements.txt and 
   ii. Type pip3 install -r requirements.txt in the terminal


### Executing program

1. After the above, set up a local mysql db and connect to the app
2. Run migrations against your local db by: 
    typing **python3 manage.py makemigrations** and **python3 manage.py migrate**
3. Finally, run the app by typing python3 manage.py runserver
  PS: Make sure you are in the directory containing manage.py when typing these commands
  
  
[Check app here](http://iashop.pythonanywhere.com/)