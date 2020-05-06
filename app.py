from flask import Flask, url_for
from flask import request
from flask_cors import CORS, cross_origin
from markupsafe import escape
import uuid

app_id = str(uuid.uuid4())
app = Flask(__name__);
cors = CORS(app);
app.config['CORS_HEADERS'] = 'Content-Type';

@app.route('/hello', methods=['POST'])
@cross_origin()
def hello():
  input=request.json
  hello=""
  if input['lang'] == 'fr':
    hello="bonjour"
  elif input['lang'] == 'de':
    hello="hallo"
  elif input['lang'] == 'es':
    hello="hola"
  else:
    hello="hello"
    
  return hello+" "+input['name']+" :: "+app_id;


app.run(debug=True)
