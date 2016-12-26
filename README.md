This is the simple website for the python class taught by nk15@rice.edu and jl51@rice.edu for the Korean international
students for Spring 2017. Built on top of Django for easy use. Nothing fancy.

Currently running on Heroku at
https://lit-reaches-57982.herokuapp.com/

How To Set Up Development Environment:
- install pip
- run             pip install -r "requirements.txt"
- install virtualenvwrapper
- create a virtualwrapper and work on it.
- submit a pull request. and we will code-review it and merge if looks good.


TODO:
- add more features
- add a model so that the lectures are tracked in some form.
- add some more tests.
- add tests for the grading system
- refactor the code for all the TODOs
- refactor the code so that the configuration and the Homework modules match up more nicely.
- add a feature so that graded files actually show the test cases that failed.
- add a django command that gets homework submission files off some remote storage (e.g. subversion or some s3 bucket)

FIXME:
- the lecture slides must be scrollable
- most text are editable even if contenteditable set to false.
- FIX all the static issues with javascript / css / html (i.e. Chrome javascript console doesn't display any error)
- fix the issue of pycogpg2 not being installed on my local machine.


Main Page Image
![The main page screenshot is unavailable](https://cloud.githubusercontent.com/assets/10087079/21211491/92b13fe2-c249-11e6-8748-45462600ff62.png)

![The main page screenshot is unavailable](https://cloud.githubusercontent.com/assets/10087079/21211497/9b537958-c249-11e6-901e-bd90b1c57995.png)

Lectures currenlty at : HOSTNAME/lectures/1,   HOESTNAME/lectures/2, etc.

Lecture Image
![The lecture screenshot is unavailable](https://cloud.githubusercontent.com/assets/10087079/21213540/a4b34972-c25a-11e6-9d00-6d99e9bd945e.png)
