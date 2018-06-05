#!/usr/bin/env python
import os
import jinja2
import webapp2

from random import randint

from models import Message, GuestBookEntry


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
        return self.render_template("hello.html")

class RandomHandler(BaseHandler):
    def get(self):
        return self.render_template(
            'random.html',
            params={'number': randint(1, 10)}
        )

todos = ['Gartenarbeit', 'Einkaufen', 'Steuererklaerung']

class TodoHandler(BaseHandler):
    def get(self):
        return self.render_template(
            'todo.html',
            params={'todos': todos}
        )

class ShoutHandler(BaseHandler):
    def get(self):
        return self.render_template('shout.html')

class ShoutResultHandler(BaseHandler):
    def post(self):
        # lies den HTTP-Parameter 'text' aus und
        # speichere ihn in der Python-Variable mit dem gleichen Namen
        text = self.request.get('text')
        text_upper = text.upper()
        return self.render_template('shout-result.html', {'text': text_upper})

class ConverterHandler(BaseHandler):
    def get(self):
        return self.render_template('converter.html')

class ConverterResultHandler(BaseHandler):
    def post(self):
        distance_mi = float(self.request.get('distance-mi'))
        distance_km = distance_mi * 1.61
        return self.render_template(
            'converter-result.html',
            {'distance_km': distance_km, 'distance_mi': distance_mi}
        )


class TodoResultHandler(BaseHandler):
    def post(self):
        new_todo = self.request.get('new-todo')
        return self.render_template(
            'todo-result.html',
            {'new_todo': new_todo}
        )

class MessagesHandler(BaseHandler):
    def get(self):
        # frage alle Messages aus der Datenbank ab
        messages = Message.query().fetch()
        return self.render_template(
            'messages.html',
            {'messages': messages}
        )

class NewMessageHandler(BaseHandler):
    def post(self):
        message_text = self.request.get('message-text')

        # Erstellt einen neuen Message-Eintrag
        msg = Message(message_text=message_text)
        # Speichert den neuen Eintrag in der Datenbank
        msg.put()

        return self.render_template(
            'new-message.html',
            {'message_text': message_text}
        )

class GuestBookHandler(BaseHandler):
    def get(self):
        return self.render_template('guestbook.html')

class NewGuestBookEntryHandler(BaseHandler):
    def post(self):
        entry_text = self.request.get('entry-text')
        email = self.request.get('email')
        name = self.request.get('name')

        # Erstellt einen neuen Guestbook-Eintrag
        gbe = GuestBookEntry(
            text=entry_text,
            email=email,
            name=name
        )
        # Speichert den neuen Eintrag in der Datenbank
        gbe.put()

        return self.render_template(
            'new-guestbook-entry.html',
            {
                'entry_text': entry_text,
                'email': email,
                'name': name
            }
        )


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/random', RandomHandler),
    webapp2.Route('/todo', TodoHandler),
    webapp2.Route('/todo-result', TodoResultHandler),
    webapp2.Route('/shout', ShoutHandler),
    webapp2.Route('/shout-result', ShoutResultHandler),
    webapp2.Route('/converter', ConverterHandler),
    webapp2.Route('/converter-result', ConverterResultHandler),
    webapp2.Route('/messages', MessagesHandler),
    webapp2.Route('/new-message', NewMessageHandler),
    webapp2.Route('/guestbook', GuestBookHandler),
    webapp2.Route('/new-guestbook-entry', NewGuestBookEntryHandler)
], debug=True)
