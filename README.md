# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version

### How do I get set up? ###

**Software Required**
* PyCharm
* Python 2.7.12
* Git

**Steps to run the developer environment**

* login to your github account
* navigate to the repository
* fork the main repository
* copy the forked repository url
* create new directory in your local machine, example- repo
* navigate to repo
* type git clone and paste your copied url
* press enter
* it will prompt for your password to authenticate
* after cloning
* open pycharm with your repo
* go to File -> Settings -> Project:test_project -> Project Interpreter
* click on settings icon
* select Create Virtualenv
* type name of your virtual env and select the base python interpreter
* click ok
* click on Terminal Tab
* activate your virtual env using source /path/to/your_env/bin/activate if not activated
* navigate to /repo/test_project/
* run pip install --upgrade pip
* run pip install -r requirement.txt
* run cd brains
* run python manage.py migrate
* run python manage.py runserver
* now you are done with the local dev env setup
* open http://localhost:8000/admin/ to view your local web server
* Now your application will appear on - http://localhost:8000/
* To open the admin panel:-
Username- admin
Password- demomode

* To appear in exam:
Username- sunny
password- demomode



### Contribution guidelines ###

* Application Developed by - Sunny Kumar

### Who do I talk to? ###

* Repo owner

### Copyright 2017 Sunny Kumar
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

* http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
