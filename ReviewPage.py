import flask
from model import Model, CourseReview


"""
Logic for get and post methods for adding reviews
This class adds/inserts the record and after editing redirects on same add review page 
"""

class reviewPage(flask.views.MethodView):
	def get(self):
	
		return flask.render_template('ReviewForm.html')

	def post(self):
		course_review= CourseReview()
		model=Model()		

		if 'Submit' in flask.request.form:
                
			if flask.request.form:
				data=flask.request.form.to_dict(flat=True)
				model.AddRecord(data)
				msg= "Record Added Successfully"
				return flask.render_template("ReviewForm.html",msg=msg)
