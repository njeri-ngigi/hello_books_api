# Hello Books API
Hello books API is a RESTful Flask application for a simple application that helps manage a library and its processes like stocking, tracking and renting books. Books can be added, deleted, retrieved and edited through endpoints. A user can login in, logout, reset password and borrow a book through the endpoints too. 

## Prerequisites
      pip
      virtualenv
      python 3 or python 2.7
      

## Installation
   create a virtual environment using 
   ```
   virtualenv <environment name>
   ```
   activate the environment using:
   ```
   $source <path to env name>/Scripts/activate (in bash)
   ```
   install dependencies using 
   ```
   $pip install -r requirements.txt
   ```
      

## Running the tests
  The tests for this API are written using the python module unittests. The tests can be found within the folder api under the folder tests.
  Python unit test framework nose that extends from unittest is used to run the tests.<br>
  To run the tests use the command:
      
   ```
   nosetests test_models.py
   nosetests test_api.py
  ```
   
## Badges  
### Continuous Integration
###### Travis CI [![Build Status](https://travis-ci.org/njeri-ngigi/hello-books-api.svg?branch=master)](https://travis-ci.org/njeri-ngigi/hello-books-api)
### Test Coverage
###### Coveralls [![Coverage Status](https://coveralls.io/repos/github/njeri-ngigi/hello-books-api/badge.svg?branch=master)](https://coveralls.io/github/njeri-ngigi/hello-books-api?branch=master)
###### Code Climate [![Maintainability](https://api.codeclimate.com/v1/badges/7c9b7ea6c931b923ab83/maintainability)](https://codeclimate.com/github/njeri-ngigi/hello-books-api/maintainability)
### Deployment
Application deployed to HEROKU
## Built with 
   Flask, a python framework
   
## Authors
[Njeri Ngigi](https://github.com/njeri-ngigi)

