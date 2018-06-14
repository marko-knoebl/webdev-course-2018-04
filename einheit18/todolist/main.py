#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Todo


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        todos = Todo.query().fetch()

        return self.render_template(
            "main.html",
            {'todos': todos}
        )

class AddHandler(BaseHandler):
    def post(self):
        new_todo_text = self.request.get('new_todo_text')

        todo = Todo(text=new_todo_text, done=False)
        todo.put()

        return self.render_template(
            "add.html",
            {'new_todo_text': new_todo_text}
        )

class DoneHandler(BaseHandler):
    def post(self, todo_id):

        # Eintrag aus datenbank auslesen
        todo = Todo.get_by_id(int(todo_id))
        # Eintrag umaendern
        todo.done = True
        # Eintrag abspeichern
        todo.put()

        return self.render_template('done.html')

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/add', AddHandler),
    webapp2.Route('/done/<todo_id:\d+>', DoneHandler)
], debug=True)
