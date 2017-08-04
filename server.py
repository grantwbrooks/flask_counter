from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

# our index route will handle rendering our form
@app.route('/')
def index():
    session['count'] += 1
    print session['count']
    return render_template("index.html")

@app.route('/counter', methods=['POST'])
def counter():
    if request.form['page_visit'] == "1":
        session['count'] += int(request.form['page_visit'])
        return redirect('/')
#question asks for another route but I wanted to try to use value field from button to determine what to add to counter with if statment
    elif request.form['page_visit'] == "0":
        session['count'] = 0
        return redirect('/')

app.run(debug=True)