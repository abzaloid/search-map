import webapp2
import logging

from google.appengine.ext.webapp import template

from google.appengine.api import users
from webapp2_extras import sessions

from webapp2_extras import auth
from webapp2_extras import sessions

from webapp2_extras.auth import InvalidAuthIdError
from webapp2_extras.auth import InvalidPasswordError

import main


### BASE HANDLER CLASS ###
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = main.jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, params=None, **kw):
        self.write(self.render_str(template, **kw))

    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        try:
            webapp2.RequestHandler.dispatch(self)
        finally:
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        return self.session_store.get_session()
