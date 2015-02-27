from google.appengine.ext import ndb

class Configuration(ndb.Model):
	key = ndb.StringProperty(required=True)
	value = ndb.StringProperty(required=True)


class Candidate(ndb.Model):
	name = ndb.StringProperty(required=True)
	role = ndb.StringProperty(required=True)