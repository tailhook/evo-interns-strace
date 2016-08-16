import pathlib
import random
from xml.sax import parse, ContentHandler
import falcon
import json
from io import StringIO


DIR = pathlib.Path('sonets')


class Parser(ContentHandler):
    def __init__(self, buf):
        self.__buf = buf
    def characters(self, text):
        text = text.strip()
        if text:
            self.__buf.write('<p>')
            self.__buf.write(text)
            self.__buf.write('</p>')


class Main:
    def on_get(self, req, resp):
        """Handles GET requests"""
        filename = random.choice(list(DIR.iterdir()))
        buf = StringIO()
        parse(str(filename), Parser(buf))
        resp.content_type = 'text/html'
        resp.body = buf.getvalue()


app = falcon.API()
app.add_route('/', Main())
