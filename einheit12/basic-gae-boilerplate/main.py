#!/usr/bin/env python

import webapp2
import random
import time


class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello World!')

class ByeHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Bye')

class RandomHandler(webapp2.RequestHandler):
    def get(self):
        random_number = random.randint(1, 6)
        return self.response.write('Random number: ' +
                                   str(random_number))

class DateHandler(webapp2.RequestHandler):
    def get(self):
        date = time.strftime('%d.%m.%Y')
        return self.response.write(date)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/hello', MainHandler),
    webapp2.Route('/bye', ByeHandler),
    webapp2.Route('/random', RandomHandler),
    webapp2.Route('/date', DateHandler)
], debug=True)
