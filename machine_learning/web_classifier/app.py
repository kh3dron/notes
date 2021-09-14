from flask import Flask
import json
from flask import render_template
from flask import request


#AI components
import pickle
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

filename = "digit_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))

def predict():
    print("Made it here")
    result = loaded_model.predict(f)
    return(result)






#Flask stuff
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def hello_world():
    return render_template('draw.html')

@app.route('/classify', methods = ['GET'])
def get_post_javascript_data():
    jsdata = str(request.form)
    print("CHECK ME OUT")
    print(jsdata)
    return(str(3))

