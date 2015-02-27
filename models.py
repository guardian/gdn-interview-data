from google.appengine.ext import ndb

class Configuration(ndb.Model):
	key = ndb.StringProperty(required=True)
	value = ndb.StringProperty(required=True)


class Candidate(ndb.Model):
	name = ndb.StringProperty(required=True)
	role = ndb.StringProperty(required=True)
	in_progress =ndb.BooleanProperty(required=True,default=True)

class InterviewOutcome(ndb.Model):
	interview_type = ndb.StringProperty(required=True)
	outcome = ndb.StringProperty(required=True)
	recorded = ndb.DateProperty(auto_now_add=True)
	interviewer = ndb.UserProperty(repeated=True)