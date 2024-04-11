from flask import Flask,redirect,url_for,request,jsonify
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def welcome():
    return "This is welcome page"

@app.route("/hello")
def hello():
    return "This is hello"


# Building Dynami URL 1st type 
@app.route("/success/<int:score>")
def success(score):
    return "This is pass" + str(score)


@app.route("/fail/<int:score>")
def fail(score):
    return "This is fail" + escape(str(score))


@app.route("/result/<int:score>")
def result(score):
    if score < 50: 
        result = "fail"
        # return redirect(url_for)
    else:
        result = "success"
        # return "This is pass " +str(score)
    
    return redirect(url_for(result,score=score))



#* Routes for Digital Ocean Course:

@app.route('/query-example')
def query_example():
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)


'''
You will need to program the part that handles the query arguments. This code will read in the language key by using either 
request.args.get('language') or request.args['language'].

By calling request.args.get('language'), the application will continue to run if the language key doesn’t exist in the URL. In that case, the result of the method will be None.

By calling request.args['language'], the app will return a 400 error if the language key doesn’t exist in the URL.

When dealing with query strings, it is recommended to use request.args.get() to prevent the app from failing.
'''


# http://127.0.0.1:5000/query-example-multiple-variables?language=Python&framework=Flask
# http://127.0.0.1:5000/query-example-multiple-variables?language=Python&framework=Flask&website=DigitalOcean
# http://127.0.0.1:5000/query-example-multiple-variables?framework=Flask&website=DigitalOcean


# Now let's create a URL in which framework field is missing
# ! It will generate error and give 404 Error
# ! http://127.0.0.1:5000/query-example-multiple-variables?language=Python&website=DigitalOcean
@app.route('/query-example-multiple-variables')
def query_example_multiple_variables():
    language = request.args.get('language')

    framework = request.args['framework']

    # if key doesn't exist, returns None
    website = request.args.get('website')

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)
    

'''
Form data comes from a form that has been sent as a POST request to a route. So instead of seeing the data in the URL (except for cases when the form is submitted with a GET request), the form data will be passed to the app behind the scenes. Even though you cannot easily see the form data that gets passed, your app can still read it.

To demonstrate this, modify the form-example route in app.py to accept both GET and POST requests and returns a form:
'''

# allow both GET and POST requests
# http://127.0.0.1:5000/form-example
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    return '''
              <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
              </form>'''

'''

The browser should display a form with two input fields - one for language and one for framework - and a submit button.

The most important thing to know about this form is that it performs a POST request to the same route that generated the form. 
The keys that will be read in the app all come from the name attributes on our form inputs. In this case, language and 
framework are the names of the inputs, so you will have access to those in the app.

Inside the view function, you will need to check if the request method is GET or POST. If it is a GET request, 
you can display the form. Otherwise, if it is a POST request, then you will want to process the incoming data.
'''
# allow both GET and POST requests
# http://127.0.0.1:5000/form-example2?language=Python&framework=flask
@app.route('/form-example2', methods=['GET', 'POST'])
def form_example2():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''




# Run this function or hit this route through client.py file in this directory

@app.route('/process-json-data', methods=['GET', 'POST'])
def process_data():
    # handle the POST request
    if request.method == 'POST':
        data = request.get_json()
        value1 = data.get('value1')
        value2 = data.get('value2')
        print("Value 1 is: {}\nValue 2 is: {}".format(value1,value2))
        return "data processed"





# GET requests will be blocked
@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)












# * ______________________________REALPYTHON_________________________________________________
# * https://www.realpythonproject.com/how-to-send-and-receive-data-in-flask/




# http://127.0.0.1:5000/receiveParameters?language=Python&framework=flask
# http://127.0.0.1:5000/receiveParameters
@app.route('/receiveParameters')
def receiveParameters():
    '''
    Receiving all data, either data exists or not
    '''
    data = request.args
    print(data)
    return {'data': data}, 200




# Flask has a property called request.form that lets it access form data. Below is an endpoint to receive form data

@app.route('/receiveFormData',methods=['POST'])
def receiveFormData():
  name = request.form['name']
  age = request.form['age']
  print(name)
  print(age)
  return{
    'data': {
      'name': name,
      'age': age
    }
  },200


# JSON is something that is common to most programming languages so this might be the most common case.
# We can use request.json to retrieve the data. To convert the json string object to Python Dict , we will use a Flask method called jsonify . 
# This will let you access keys similar to how you would do with a dictionary.

@app.route('/receiveJson',methods=['POST'])
def receivePostData():
  data = jsonify(request.json)
  print(data)
  return  data,200





# request.files returns an FileStorage object, as a result, you can directly use read to get the content of the file. 
# We will need to decode it before sending it as response data.

# Working with files can get somewhat confusing, specifically the following line

# data = file.read().decode('utf-8')
# Depending on the format of the file, you might not have to decode it. Instead, 
# you might have to use something like json.loads(byteData) to convert a byte object to JSON.

@app.route('/receiveFile',methods=['POST'])
def receiveFile():
  file= request.files['textFile']
  data = file.read().decode('utf-8')
  print(data)
  return {
    "data": data
  },200


# SOLUTION 1
# Can Flask have optional URL parameters?
# Stackoverflow
@app.route('/<user_id>', defaults={'username': None})
@app.route('/<user_id>/<username>')
def show(user_id, username):
    pass


# SOLUTION 2
# THIS ONLY FOR FLASK RESTFUL
# If you are using Flask-Restful like me, it is also possible this way:


# api.add_resource(UserAPI, '/<userId>', '/<userId>/<username>', endpoint = 'user')
# a then in your Resource class:
# class UserAPI(Resource):

#   def get(self, userId, username=None):
#     pass







#* ________________________________Flask Offical Doc_________________________________
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do_the_login()"
    else:
        return "show_the_login_form()"
    

# The example above keeps all methods for the route within one function, which can be useful if each part uses some common data.

# You can also separate views for different methods into different functions. Flask provides a shortcut for decorating such routes 
# with get(), post(), etc. for each common HTTP method.

@app.get('/login')
def login_get():
    return "show_the_login_form()"

@app.post('/login')
def login_post():
    return "do_the_login()"









if __name__ == "__main__":
    app.run(debug=True)