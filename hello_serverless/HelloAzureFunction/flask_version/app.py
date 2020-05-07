from flask import Flask, url_for
from flask import request
from flask_cors import CORS, cross_origin
from markupsafe import escape
import uuid
import hello_core

app_id = str(uuid.uuid4())
app = Flask(__name__);
cors = CORS(app);
app.config['CORS_HEADERS'] = 'Content-Type';

@app.route('/hello', methods=['POST'])
@cross_origin()
def hello():
  input=request.json
   
  return hello_core.hello(input);


app.run(debug=True)
