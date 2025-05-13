# Project setup guide

## Create virtual enviroment 
py -m venv myenv

## change directory to myenv
cd myenv

## activate venv
### for linux or mac
    source bin/activate
### for windows

## Get project code
clone project git-hub repo

    git clone git@github.com:manishkumar987/guestfirst_gateway_django.git

## Install dependencies
python -m pip install -r requirements.txt

## After installing new package must run this command
pip freeze > requirements.txt