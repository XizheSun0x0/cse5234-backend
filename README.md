# cse5234-lab7

## About Learn and Lend (LAL)
 Learn and Lend, abbreviated as LAL, is dedicated to recycling used items whenever possible. 
 Users can donate items they no longer need, and we post them online for other students to pick up.

## Before Running This App
To set up this application, run the following command in your terminal:
‘$ pip install -r requirements.txt’
This will install all the required packages.
Recommended Python version is 3.11.

## About the Database
This project uses SQLite3 as the database management system.
The database is stored in '/instance/lal.db'.

## Test locally
```bash
    gunicorn wsgi_handler:app
```
