# "Database code" for the DB Forum.

import datetime
import psycopg2
import sys

DBNAME = "forum"

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
    """Return all posts form the database, most recent first"""
    db = psycopg2.connect(database=DBNAME, user='vagrant', password='vagrant', host='localhost', port='5432')
    c = db.cursor()
    c.execute("select content, time from posts order by time desc")
    posts = c.fetchall()
    db.close()
    return posts


def add_post(content):
    """Ass a post to the 'database' with the current timestamp"""
    db = psycopg2.connect(database=DBNAME, user='vagrant', password='vagrant', host='localhost', port='5432')
    c = db.cursor()
    c.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
    db.commit()
    db.close()
