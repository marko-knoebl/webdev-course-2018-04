#!/usr/bin/env python
import os
import jinja2
import webapp2

import json
from google.appengine.api import urlfetch

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
        data = open("people.json", "r").read()
        json_data = json.loads(data)

        params = {"people_list": json_data}

        self.render_template("hello.html", params)

class WeatherFormHandler(BaseHandler):
    def get(self):
        self.render_template("weather_form.html")

class WeatherResultHandler(BaseHandler):
    def post(self):

        city = self.request.params['city']

        base_url = "http://api.openweathermap.org/data/2.5/weather?appid=9d3ae54b4b75a62bd73707396325726e&q="

        result = urlfetch.fetch(base_url + city)

        weather_info = json.loads(result.content)

        params = {"weather_info": weather_info}

        self.render_template("weather.html", params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/weather', WeatherFormHandler),
    webapp2.Route('/weather-result', WeatherResultHandler)
], debug=True)
