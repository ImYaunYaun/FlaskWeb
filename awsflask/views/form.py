from flask import Flask, Blueprint, request, render_template, redirect, url_for
form = Blueprint('form', __name__)
 
@form.route('/form')
def formPage():
    return render_template('form.html')

@form.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        print("post : user => ", user)
        return redirect(url_for('success', name=user, action="post"))
    else:
        user = request.args.get('user')
        print("get : user => ", user)
        return redirect(url_for('success', name=user, action="get"))

@form.route('/success/<action>/<name>')
def success(name, action):
    return '{} : Welcome {} ~ !!!'.format(action, name)