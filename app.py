

# First we'll need to import Flask, jsonify
# and request from flask to our code
# file.

from flask import Flask,jsonify, request

app = Flask(__name__)

# Then we say app = Flask(__name__).
# And create dummy tasks data with an
# id, title, description and done value
# which would be true or false.

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


# Now, we will create a similar looking
# function as our hello_world(), and we
# would name it as add_data().
# In the add_data() function, we will
# change the route from ‘/’ to ‘add-data’.
# This would mean that this function
# would only be available at route
# localhost:5000/add-data.
# We'll also specify the method that we
# want to have on the route. We can do
# that by adding methods=["POST"] to
# the line.
# Here, we are explicitly telling Flask
# that we want this function on this
# route to only allow POST Request

@app.route("/")
def hello_world():
    return "Hello World!"

# In this post request we'll create an
# add_task() function which will check
# for the data and if it doesn't find any
# then it'll show the 400 error with a
# message to provide data and allow us
# to add data to the API and to the
# tasks array of objects.

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
#     Now that we have to add a task, we'll
# create a skeleton/ structure of how
# the task will look like.
# Our task will be an object/dictionary
# which will have multiple keys such as
# Id, title of the task, description of the
# task and the status of the task.
# We'll automate the id to increment by
# 1 every time a new task is added and
# keep the initial status of the task as
# false.
# Title and description will be provided
# by the user.
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    
#     As the user provides the title and
# description we have to add the task to
# the main list of tasks and then show
# the message - "task added
# successfully".
#     Here we are converting the message
# to a json object and then showing it.
# We are doing it because most of the
# time the data we get is in a Json
# format.
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    
# So now our post method is ready.
# We also have to create a get method
# to see all the available tasks.
# We have already seen how to create
# a GET method, this time we'll add a
# route name to it.
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 
    
# finally we'll code to run our web
# application.
# Here we are keeping debug=True so
# that the server will reload every time
# you make some change to the code.

if (__name__ == "__main__"):
    app.run(debug=True)
    
    
# To test our APIs excluding GET i.e
# (POST, PUT, and DELETE) we need
# to install a software known as
# POSTMAN.

# 1) Once we install it, Now we paste the link in the postman
# and set the method to GET, add
# /get-data to the route and send the
# request.

# 2) Now let's check our POST method.
# We'll set the method to POST and
# add /add-data to the route and send
# the request.