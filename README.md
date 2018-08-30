[![Build Status](https://travis-ci.org/billkabanga/StackOverflow_Lite.svg?branch=API-feature)](https://travis-ci.org/billkabanga/StackOverflow_Lite)
[![Coverage Status](https://coveralls.io/repos/github/billkabanga/StackOverflow_Lite/badge.svg?branch=API-feature)](https://coveralls.io/github/billkabanga/StackOverflow_Lite?branch=API-feature)

# StackOverflow-lite
This is a  python version of StackOverflow. A platform for questions and answers.It allows users to post questions and answers respectively.Users can also read different questions and their answers.

## Getting started
The following instructions will help you setup and run the application on your machine.

## Prerequisites
You will need the following:
* Internet
* GIT
* IDE(preferrably Visual Studio Code)
* Postman
* PostgreSQL
## Project Links.
**API endpoints:** The link to the API-feat branch with the code: (https://github.com/billkabanga/StackOverflow_Lite/tree/API-feature)

## Project Functionality.
* User can create an sign-up and Login.
* User can search for questions.
* User can post a question.
* User can post an answer to a question.
* User can delete his/her question


## Getting the application on the local machine.
Clone the remote repository to you local machine using the following command: `https://github.com/billkabanga/StackOverflow_Lite.git`

You can now access the project on your local machine by pointing to the local repository using `cd` and `code .` if using Visual Studio code.
Create a virtual environment in the local repository using the following code: `python -3 -m venv env`
Activate the virtual environment: `env/Scripts/Activate.bat`



## Installing dependencies.
To install all the required extensions for project, use the following command: `pip install -r requirements.txt`
Run the `psql` command interface and create two databases **apptest_db** and **StackOverflow-lite** using the `CREATE DATABASE {database name}` command.
Application should now be up and ready to test.

## Running tests:
**Testing the API endpoints.**
Run the `run.py` file using the `py run.py` command and test the endpoints in Postman as shown below:

| url/endpoint                        | Verb          | Action                     | Parameters     
| ----------------------------------- |:-------------:|  ------------------------- |----------------------|
| /api/v1/auth/signup                   | POST           | User gets registered          | username,email,password |
| /api/v1/auth/login       | POST           | User login         | username,password |
| /api/v1/questions                   | GET          | fetch all questions              | -   |
| /api/v1/questions/<int:qnId>| GET          | fetch specific question| <any number as id of question> |
| /api/v1/questions                   | POST           | post a question          | question |
| /api/v1/questions/<int:qnId>/answers        | POST           |answer specific question         | answer |
| /api/v1/questions/<int:qnId>                   | DELETE          | delete a question  | <any number as id of question>|

**Running the unit tests**
To run the unit tests use the following command `pytest`
  
  


## Built with:
**API endpoints**
* Python 3
* Flask
* Flask-restful
* PostgreSQL

## Author:
Author of this project-Twinomuhwezi Kabanga Bill, 
a young aspiring software developer utilising each day as one to learn and provide solutions to world problems.

