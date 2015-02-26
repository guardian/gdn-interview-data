import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode
from google.appengine.api import urlfetch

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
		
		template_values = {}

		self.response.out.write(template.render(template_values))

class Candidate(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('candidates/individual.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

class NewCandidate(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('candidates/new.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

class AllCandidates(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('candidates/all.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([
	webapp2.Route(r'/', handler=MainPage),
	webapp2.Route(r'/dashboard', handler=Dashboard),
	webapp2.Route(r'/interview', handler=Interview),
	webapp2.Route(r'/candidate', handler=Candidate),
	webapp2.Route(r'/candidates', handler=AllCandidates),
	webapp2.Route(r'/candidate/new', handler=NewCandidate),
	], debug=True)