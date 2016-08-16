import pathlib
import random
from xml.sax import parse, ContentHandler
import falcon
import json
import sys
from io import StringIO


DIR = pathlib.Path('sonets')


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
        buf = StringIO()
        buf.write('<pre>')
        parse(str(filename), Parser(buf))
        buf.write('</pre>')
        resp.content_type = 'text/html'
        resp.body = buf.getvalue()


app = falcon.API()
app.add_route('/', Main())
