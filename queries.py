import models

def candidates_in_progress():
	return models.Candidate.query(models.Candidate.in_progress == True)

def all_interviewers():
	return models.Interviewer.query()