import pathlib
import random
from xml.sax import parse, ContentHandler
import falcon
import json
import redis
import sys
from io import StringIO


DIR = pathlib.Path('sonets')
redis_conn = redis.StrictRedis()


class Parser(ContentHandler):
    def __init__(self, buf):
        self.__buf = buf
    def characters(self, text):
        if text.strip():
            self.__buf.write(text+'\n')


class Main:
    def on_get(self, req, resp):
        """Handles GET requests"""
        filename = random.choice(list(DIR.iterdir()))
        visitor_no = redis_conn.incr('visitors')
        buf = StringIO()
        buf.write("<p>You're visitor #{}</p>".format(visitor_no))
        buf.write('<pre>')
        parse(str(filename), Parser(buf))
        buf.write('</pre>')
        resp.content_type = 'text/html'
        resp.body = buf.getvalue()


app = falcon.API()
app.add_route('/', Main())
