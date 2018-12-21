from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/join', methods=['POST'])
def join():
    print(request)
    userid = request.form['userid']
    password = request.form['password']
    name = request.form['name']
    phone = request.form['phone']
    
    user = {'userid': userid, 'password': password, 'name': name, 'phone': phone}
    
    return render_template('test.html', user=user)

@app.route('/m/<menu>')
def m(menu):
    return render_template(menu+'.html')

if __name__ == '__main__':
    app.run(port=8888, host='0.0.0.0')