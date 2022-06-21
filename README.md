# Neighbourhood

This is a web application that allows users to be in the loop about everything happening in their neighbourhood. From contact information of different businesses to announcements and alerts.

### Dependencies

In order for you to use the content on this repo ensure you have the following:

- A computer that runs on either of the following; (Windows 7+, Linux, Mac OS)
- Python 3.x+

https://github.com/JKLLR

## BDD
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login to admin  | **username**: moringa , **password** : moringa1234 | view and make changes to the admin | 
Signup to the application | Click on `Signup` | A sign up page appears with a sign up form |
|  Login to the site | Click on `Log in`  | Redirected to the login page with a login form |

### Installing

To get the code..

1. Cloning the repository:

```bash
git clone https://github.com/JKLLR/Neighbourhood.git
```

2. Navigate to the folder and install requirements. 

```bash
cd Neighbourhood
python3 -m venv virtual
source virtual/bin/activate
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
```

4. Running the application

```bash
python3 manage.py runserver
```

Open the application on localhost `127.0.0.1:8000`.


## Running the tests

Testing the application

```bash
python3 manage.py test hoods
```

## Live link

https://jeffhoods.herokuapp.com/login/?next=/

## Built With

* [Python3.8.10](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

## Known Bugs

- No known bugs yet

## Authors

[Jeff Huria](https://github.com/JKLLR)

## Support and contact details

If you run into any issues or have questions, ideas or concerns, reach out to me via e-mail, at jeffhuria@gmail.com

## License

https://choosealicense.com/licenses/mit/ 
Copyright (c) {2022} **Jeff Huria**

