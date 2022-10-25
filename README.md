# Vacancies analyse aggregator
This is implementation of api client, which purpose aggreate and get analyse statistic by several programming languages.
### before start you have to:
 - register app on https://api.superjob.ru/ and get personal token.
 - create .env file on project directory
 - make a record formatted as "API_SUPERJOB=YUORTOKEN"

### How to install
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### How to use
```
python main.py
```
## main.py
Main application in package. Print two tapbles - for superjob an headhunter.

## hh.py
module provide three function for receive and handle date from [head hunter api](https://api.hh.ru/)

## sj.py
module provide three function for receive and handle date from [head hunter api](https://api.superjob.ru/)
