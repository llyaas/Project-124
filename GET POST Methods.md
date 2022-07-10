API is Application
Programming interface, which is a
software intermediary that allows two
applications to talk to each other. All
the websites, mobile apps, etc. that
you may use, or instant messaging
apps to send messages, use an API.
All APIs use an HTTP method. Let’s
see what they are:
The GET Method -
GET is used to request data from a
specified resource. When you access
a website’s page, your browser
makes a get request to your API and
your API is returning the front-end
that is displayed in the browser.
All the APIs that you create in Flask,
by default, use GET Request. If you
start your hello_world server and go
to localhost:5000, you can see in your
terminal that the browser made a
GET request on the server/API.
The POST Method -
POST is used to send data to the
server to create/update a resource.
A user wants to sign up from the
signup page? A user wants to change
their password? That would be a post
request.
The PUT Method -
PUT is used to send data to a server
to create / update a resource.

The basic difference between PUT
and POST is that a POST request is
when you can create multiple copies
of the same resource.
A PUT request, on the other hand
means that you want to create only
one copy of the resource, i.e. Signing
Up a unique user.
The DELETE Method -
DELETE is used to delete a resource.
The default method used by flask is
GET.
