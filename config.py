
CSRF_ENABLED = True
SECRET_KEY = "you'll never-guess"

OPENID_PROVIDERS = [
    {'name': 'Wordpress', 'url': 'http://www.wordpress.com'},
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

from os.path import abspath, join, dirname

basedir = abspath(dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = join(basedir, 'db_repository')
