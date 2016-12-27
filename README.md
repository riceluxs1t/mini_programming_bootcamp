This is the simple website for the python class taught by nk15@rice.edu and jl51@rice.edu for the Korean international
students for Spring 2017. Built on top of Django for easy use. Nothing fancy.

Currently running on Heroku at
https://lit-reaches-57982.herokuapp.com/

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

- create a virtualwrapper and work on it. (type "makevirtualenv SOME_WRAPPER_NAME" to create a virtualwrapper, where SOME_WRAPPER_NAME is some name)
	ex) $makvirtualenv ricelux
	useful commands:
		Launch virtual environment: $workon ricelux
		Deactivate the environment: $deactivate

- establish project dependencies by
	$pip install -r "requirements.txt"

- submit a pull request. and we will code-review it and merge if looks good.


TODO:
- add more features.
- add some more tests for python code.
- add specifically tests for the grader module
- fix for all the inline TODO comments
- refactor the code so that all config files are managed in one place.
- add a feature so that graded files actually show the test cases that failed.
- add a django command that gets homework submission files off some remote storage (e.g. subversion or some s3 bucket)

FIXME:
- the lecture slides must be scrollable (left/right and up and down)
- most text are editable even if contenteditable set to false.
- FIX all the static issues with javascript / css / html (i.e. Chrome javascript console doesn't display any error)
- FIX some font inconsistency (minor)
- FIX next lecture out of bounds issue. if it is the latest lecture, disable the next lecture UI.
- fix the issue of pycogpg2 not being installed on my local machine. (a very minor issue)


Main Page Image
![The main page screenshot is unavailable](https://cloud.githubusercontent.com/assets/10087079/21211491/92b13fe2-c249-11e6-8748-45462600ff62.png)

![The main page screenshot is unavailable](https://cloud.githubusercontent.com/assets/10087079/21211497/9b537958-c249-11e6-901e-bd90b1c57995.png)

Lectures currenlty at : HOSTNAME/lectures/1,   HOESTNAME/lectures/2, etc.

Lecture Image
![The lecture screenshot is unavailable](https://cloud.githubusercontent.com/assets/10087079/21213540/a4b34972-c25a-11e6-9d00-6d99e9bd945e.png)
