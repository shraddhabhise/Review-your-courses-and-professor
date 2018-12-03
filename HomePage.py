import flask
from model import Model

"""
Logic for get and post methods for displaying reviews
This class displays all record

"""

class homePage(flask.views.MethodView):
	def get(self):
		model=Model()
		data= model.fetchall()
		return flask.render_template('Home.html', data=data) 


