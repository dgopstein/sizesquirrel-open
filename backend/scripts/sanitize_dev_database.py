# Utility script that takes a db and sanitizes it of personal information for development
from backend import app, db
from backend.models import Item, User_Item, User

import urllib.request
import random

# Get a random list of names
word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()
upper_words = [word for word in words if word[0].isupper()]
lower_words = [word for word in words if word[0].islower()]
name_words  = [word for word in upper_words if not word.isupper() and len(word) > 3 and "'" not in word]
username_words = [word for word in lower_words if len(word) > 5 and "'" not in word]

def sanitize_dev_database():
    # Trim size of database to 1500 uses
    users = User.query.all()
    for user in users:
        if user.id > 1500:
            db.session.delete(user)

    all_user_items = User_Item.query.all()
    for user_item in all_user_items:
        if user_item.user_id > 1500:
            db.session.delete(user_item)

    # Randomize user name, username, emails and provider_id
    users = User.query.all()
    for user in users:
        mailSuffixes = ['@gmail.com', '@outlook.com', '@hotmail.com', '@mail.com']
        first_name = name_words[random.randint(0, len(name_words))-1] 
        last_name = name_words[random.randint(0, len(name_words))-1] 
        rand_email = str.lower(last_name) + str(random.randint(0,100)) + mailSuffixes[random.randint(0, len(mailSuffixes))-1]
        username = username_words[random.randint(0, len(username_words))-1] + str(random.randint(0,100));
        user.username = username;

        if 'sizesquirrel' in user.provider_id:
            user.provider_id = 'sizesquirrel$' + rand_email;
            user.email = rand_email;
            user.name = ' '.join([first_name, last_name]);

        if 'facebook' in user.provider_id:
            user.provider_id = 'facebook$' + str(random.randint(0,10000000000000000));
            user.email = rand_email;
            user.name = ' '.join([first_name, last_name]);

    db.session.commit();
    print('Database sanitized')
    