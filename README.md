# django-boards
An exercise following guide at http://t.cn/Rmj8pmp

## Running the Project Locally

First, clone the repository to your local machine:

`git clone git@github.com:sibtc/django-beginners-guide.git`

Install the requirements:

`pip install -r requirements.txt`

Setup the local configurations:

`touch .env`

    SECRET_KEY=rqr_cjv4igscyu8&&(0ce(=sy=f2)p=f_wn&@0xsp7m$@!kp=d
    DEBUG=True
    ALLOWED_HOSTS=.localhost,127.0.0.1

Create the database:

`python manage.py migrate`

Finally, run the development server:

`python manage.py runserver`

The project will be available at 127.0.0.1:8000.

## License

The tutorials, documentations, comics are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
