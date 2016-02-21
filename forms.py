
from wtforms import form
from wtforms import validators
from wtforms import fields

class OutcomeForm(form.Form):
	candidate_key = fields.StringField(validators=[validators.DataRequired()])
	outcome_type = fields.StringField(validators=[validators.DataRequired()])
	complete = fields.BooleanField(default=False, validators=[])
