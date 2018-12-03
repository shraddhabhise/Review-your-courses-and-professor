import flask
from IModel import IModel
from google.appengine.ext import ndb

#referred from lab

class CourseReview(ndb.Model):
#This class is responsible to retrieve data from ndb

	course=ndb.StringProperty()
	term=ndb.StringProperty()
	instructor=ndb.StringProperty()
        rating=ndb.StringProperty()
	review=ndb.StringProperty()
	
class Model(IModel):

	def from_datastore(self,entity):
	# This method is used to access data from entity, wrap it in list and return that list 
		course_review={}
		course_review['course']=entity.course
		course_review['term']=entity.term
		course_review['instructor']=entity.instructor
		course_review['rating']=entity.rating
		course_review['review']=entity.review
		return course_review

	def fetchall(self):
	#fetchall method is responsible to fetch data from CourseReviews class and send it to view after mapping data as list 
	
		query= CourseReview.query()
		entities =query.fetch(None)
		entities=list(map(self.from_datastore,entities))
		return entities

	def AddRecord(self, data):
	#AddRecord method is responsible to add the data that the user inputs on Add review form
	
		course= CourseReview()
		course.course = data['course']
		course.term = data['Term']
		course.instructor = data['Instructor']
		course.rating = data['Rating']
		course.review = data['Review']
		course.put()	
