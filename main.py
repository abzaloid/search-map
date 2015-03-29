import os
import sys
import webapp2
import jinja2

import logging

import handler

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
### Configuration ###
config = {}
config = {
      'webapp2_extras.auth': {
            'user_model': 'models.User',
            'user_attributes': ['name']
            },
      'webapp2_extras.sessions': {
            'secret_key': 'my secret key which you dont know'
      }
}

class MainHandler(handler.Handler):
    def get(self):
        self.render("main.html", message = "Hello!")

    def post(self):
    	self.render("main.html", message = "OK!")


app = webapp2.WSGIApplication([('/', MainHandler)], 
                               config=config, debug=True)

