#Instructions:#

- cd to the project
- virtualenv venv
- source venv/bin/activate
- pip install -r requirements.txt
- cd prototype
- ./manage.py migrate
- ./manage.py runserver

Description:
SMS Serivce is not yet integrated.

2 major urls:
- 1. Home page for a admin to add a phone number for a specific claim id (e.g. Claim Id: 1->HR03AL6246, PHONE: 9569191889)
- 2. Upload url for that phone specific to that claim (/1/9569191889)

