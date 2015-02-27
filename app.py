import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode

from google.appengine.api import urlfetch
from google.appengine.ext import ndb
from google.appengine.api import users

import models

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))

class MainPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

class Dashboard(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('dashboard.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

class Interview(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('interview.html')
		
		template_values = {
			'candidates' : models.Candidate.query(),
		}

		self.response.out.write(template.render(template_values))

	def post(self):

		key = self.request.get('candidate')

		candidate = ndb.Key(urlsafe=key).get()

		user = users.get_current_user()

		outcome = models.InterviewOutcome(
			parent=candidate.key,
			interview_type=self.request.get('interview_type'),
			outcome=self.request.get('outcome'),
			interviewers=[user],)

		outcome.put()

		return webapp2.redirect('/candidate/{0}'.format(candidate.key.urlsafe()))

class Candidate(webapp2.RequestHandler):
	def get(self, key):
		template = jinja_environment.get_template('candidates/individual.html')

		candidate = ndb.Key(urlsafe=key).get()
		
		template_values = {
			'candidate': candidate,
			'interviews': [i for i in models.InterviewOutcome.query(ancestor=candidate.key)],
		}

		self.response.out.write(template.render(template_values))

class NewCandidate(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('candidates/add.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

	def post(self):

		candidate = models.Candidate(name=self.request.get('name'),
			role=self.request.get('role'))

		candidate.put()

		return webapp2.redirect('/candidate/{0}'.format(candidate.key.urlsafe()))

class AllCandidates(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('candidates/all.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([
	webapp2.Route(r'/', handler=MainPage),
	webapp2.Route(r'/dashboard', handler=Dashboard),
	webapp2.Route(r'/interview', handler=Interview),
	webapp2.Route(r'/candidate/new', handler=NewCandidate),
	webapp2.Route(r'/candidate/<key>', handler=Candidate),
	webapp2.Route(r'/candidates', handler=AllCandidates),
	], debug=True)