from google.appengine.ext import ndb

class Todo(ndb.Model):
    text = ndb.StringProperty()
    done = ndb.BooleanProperty()
