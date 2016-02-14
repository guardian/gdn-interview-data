import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode

from google.appengine.api import urlfetch
from google.appengine.ext import ndb
from google.appengine.api import users

import data
import queries
import models

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))

class MainPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

class Interviewer(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('interviewers/new.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

	def post(self):

		models.Interviewer(name=self.request.get("name")).put()

		return webapp2.redirect('/interviewers')

class NewCandidate(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('candidates/add.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

	def post(self):

		candidate = models.Candidate(
			name=self.request.get('name'),
			role=self.request.get('role'),
			gender=self.request.get('gender'))

		candidate.put()

		return webapp2.redirect('/candidate/{0}'.format(candidate.key.urlsafe()))

class Outcome(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('outcomes/offer.html')

		template_values = {
			'candidates': models.Candidate.query(models.Candidate.in_progress == True),
			'outcomes': data.outcomes,
		}

		self.response.out.write(template.render(template_values))