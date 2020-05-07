import uuid

app_id = str(uuid.uuid4())

def hello(input):
  hello=""
  if input['lang'] == 'fr':
    hello="bonjour"
  elif input['lang'] == 'de':
    hello="hallo"
  elif input['lang'] == 'es':
    hello="hola"
  else:
    hello="hello"
    
  return hello+"-v3,core "+input['name']+" :: "+app_id
