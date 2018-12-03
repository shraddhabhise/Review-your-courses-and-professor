import flask, flask.views
from main import Main
from HomePage import homePage
from ReviewPage import reviewPage


app = flask.Flask(__name__)

"""Routes for Landing page, display review page, add view , Edit Review, Delete view """
app.add_url_rule('/', view_func=Main.as_view('index'),methods=["GET","POST"])
app.add_url_rule('/Home', view_func=homePage.as_view('Home'),methods=["GET","POST"])
app.add_url_rule('/ReviewPage', view_func=reviewPage.as_view('ReviewForm'),methods=["GET","POST"])

app.debug=True

if __name__=='__main__':
	app.run(host='0.0.0.0', port=8000,debug=True)
 
