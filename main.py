from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_info.html')

@app.route("/", methods=['post', 'get'])
def user_info():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    z = 0
    y = 0
    x = 0

    for text in username:
        if text == ' ':
            username_error = "That's not a valid username"
    if len(username)>=20 or len(username)<=3:
        username_error = "That's not a valid username"
    if username == '':
        username_error = "You need to put something here, donchaknow"
    
    if len(password)<=3 or len(password)>=20:
        password_error = "That's not a valid password"
        password = ''
    if password == 'password':
        password_error = 'Really?'
    if password == 'P@22w0rd':
        password_error = 'Jesus! No! Do I need a rolled up newspaper? Try again'
    
    if password != verify:
        verify_error = "Passwords don't match"
        verify = ''
    
    if email != '':
        if len(email)>=20 or len(email)<=3:
            email_error = "That's not a valid email"
        for text in email:
            if text == '@':
                z+=1
            if text == '.':
                y+=1
            if text == ' ':
                x+=1
        if z!=1 or y!=1 or x>0:
            email_error
            email = ''


    if not username_error and not password_error and not verify_error and not email_error:
        return redirect("/welcome?username={0}".format(username))
    else:
        return render_template('user_info.html', username_error=username_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error, 
        username=username, password=password, verify=verify, email=email)

@app.route("/welcome", methods=["get"])
def welcome():
    username = request.args.get('username')
    return '<h1>Welcome, {0}</h1>'.format(username)


app.run()