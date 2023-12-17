from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/doLogin',methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    if username== "sujan" and password == "sujan123":
        return redirect('/')
    else:
        return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)

