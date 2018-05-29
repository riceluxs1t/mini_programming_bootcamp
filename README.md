This is a simple website for the python class taught by nk15@rice.edu, jl51@rice.edu, sn28@rice.edu, kk49@rice.edu  for the Korean international
students for Spring 2017. Built on top of Django for easy use. Nothing fancy.

Currently running on Heroku at
http://www.namgunkim.com

How To Set Up Development Environment:
- install python 2.7
- install pip
- install virtualenvwrapper ($pip install virtualenvwrapper)
- setup virtualenv
  1. create virtual environment setup file
  	$mkdir ~/.python_virtual_envs

  2. $nano ~/.bashrc 

  3. copy below two lines to ~/.bashsrc
	export WORKON_HOME=~/.python_virtual_envs
	source /usr/local/bin/virtualenvwrapper.sh #it will set several paths to initiate virtualenv.

- create a virtualwrapper and work on it. (type "makevirtualenv SOME_WRAPPER_NAME" to create a virtualwrapper, where SOME_WRAPPER_NAME is some name you choose)
	ex) $makvirtualenv ricelux.

	useful commands:
		Launch virtual environment: $workon ricelux
		Deactivate the environment: $deactivate

- establish project dependencies by
	$pip install -r "requirements.txt"

- submit a pull request. and we will code-review it and merge if looks good.


# How Grader Module works

The grader module takes as input 1) a homework submission 2) the corresponding solutions module and runs all the
test cases against the submission code.

These are the following components for grading of homework X.

- HOMEWORK_NAME : supplied as one of the arguments of the "grade" django command. USER_NAME: supplied as one of
the arguments of the "grade" django command. "grade" django command exists in path "grader.management.commands.grade.py"
An example use case is "python manage.py grade homework2 nate". homework2 corresponds to HOMEWORK_NAME and nate to
USER_NAME

- a solution module at path "grader.solutions.HOMEWORK_NAME.PY".
This file contains a class named Grader, which supplies a method
called "run_tests". Any solution file that implements these two things works with the underlying system. It is easier,
however, to implement one that subclasses the supplied "base_grader" class which provides some utility functions such
as a timeout feature for some test case.


- one or more student submission modules (the multi module support is not quite there, but should be added soon)
in path "submissions.HOMEWORK_NAME.USER_NAME.MODULE1.py", "submissions.HOMEWORK_NAME.USER_NAME.MODULE2.py", etc.
This file must implement all the functions specified by the homework.
If doesn't, the grading fails and the student receives a zero (TODO: make this a little more graceful).

- a Django Lectures model instance that has 1) the comma separated string of all the expected modules names
 2) the comma separated string of all the expected function names 3) a name field equal to HOMEWORK_NAME

TODO: config options are specified from multiple sources. make it more manageable.

The grading is done individually for each student by running the django command of the form
"python manage.py grade HOMEWORK_NAME USER_NAME". this should be done either manually or by Jenkins or other simple
cron job.

The command firstly checks if the solution module exists. Then checks if the student modules have expected functions
implemented. If both were successful, runs the test cases against the student code. At the end, writes a score
to a file in path "grader.grades". The score is computed by (# of passed test cases / # of all test cases)

# AWS CONFIG
import from settings.py for the access key and secret key

# TODO:
- add a feature so that graded files actually show the test cases that failed.
- add a multi module submission support for the grader module. i.e. students submit multiple .py files for one homework
- add support to run test cases by slack command (setting up a slack bot is easy but the ui takes some effort)
- add support to check floating point items in a list by the epsilon method

# FIXME:
- most text are editable even if contenteditable set to false.
- FIX all the static issues with javascript / css / html (i.e. Chrome javascript console doesn't display any error)


Main Page Image
![The main page screenshot is unavailable](https://cloud.githubusercontent.com/assets/10087079/21211491/92b13fe2-c249-11e6-8748-45462600ff62.png)

![The main page screenshot is unavailable](https://cloud.githubusercontent.com/assets/10087079/21211497/9b537958-c249-11e6-901e-bd90b1c57995.png)

Lectures currenlty at : HOSTNAME/lectures/1,   HOESTNAME/lectures/2, etc.

Lecture Image
![The lecture screenshot is unavailable](https://cloud.githubusercontent.com/assets/10087079/21213540/a4b34972-c25a-11e6-9d00-6d99e9bd945e.png)

