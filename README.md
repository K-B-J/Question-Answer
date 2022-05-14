# Question Answer

This is a project made by [Kevin Joshi](https://github.com/KevinJ-hub) & [Kaushal Binjola](https://github.com/KaushalBinjola).  
It is hosted on [Heroku](https://www.heroku.com), you can check it out [here](https://oose-question-answer.herokuapp.com). Database used is PostgreSQL which is hosted on Heroku as well and various dependencies like [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) & [Django Rest Framework](https://www.django-rest-framework.org/) have been used.  
It is a web app where users can ask and answer questions as well as up vote the answers. This is just one functional module of the whole web app where the business model is running ads and the revenue generated is then used to pay the users who have answered the questions based on the activity on the question as well as the relative up votes received for the answer.

> **NOTE:** Since the app is hosted for free on heroku it goes to sleep on 30 mins of inactivity so there might be a possibility that the app takes a few seconds to load INITIALLY so please be patient.  

## Tech Used

- Python
- Django
- PostgreSQL
- Javascript
- Bootstrap5
- Font Awesome

## Running this project

You can head over to [https://oose-question-answer.herokuapp.com](https://oose-question-answer.herokuapp.com) to try out the app in your browser.  

OR  

1. Clone the repository
2. Create a ".env" file in the root of the project and add the DB credentials and django project secret key in it (DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, SECRET_KEY)
3. Run the following command from the root of the project

```bash
pip install -r requirements.txt
```

```bash
py manage.py makemigrations
```

```bash
py manage.py migrate
```

4. Create a super user to access django admin panel (optional)

```bash
py manage.py createsuperuser
```

5. Run the server

```bash
py manage.py runserver
```

> **NOTE:** You can also create a virtual environment, activate it and follow the above steps.

## Images

### Desktop

![Desktop Login Page](screenshots/ss7.png)
---

![Desktop Register Page](screenshots/ss9.png)
---

![Desktop Home Page](screenshots/ss5.png)
---

![Desktop Ask Question Page](screenshots/ss3.png)
---

![Desktop Question Answer Page](screenshots/ss11.png)
---

![Desktop Answer Question Page](screenshots/ss1.png)

### Mobile Devices

| ![Mobile Login Page](screenshots/ss8.png) | ![Mobile Register Page](screenshots/ss10.png) | ![Mobile Home Page](screenshots/ss6.png) |
|---|---|---|
| ![Mobile Ask Question Page](screenshots/ss4.png) | ![Mobile Question Answer Page](screenshots/ss12.png) | ![Mobile Answer Question Page](screenshots/ss2.png) |  
