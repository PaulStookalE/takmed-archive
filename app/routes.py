from . import app, login_manager
from flask import render_template, redirect, flash, request, url_for
from flask_login import current_user, login_user



# Створення роуту для головної сторінки.
@app.route('/')
def main():
    return render_template('main.html')


# # 
# @app.route('/login', methods=['POST', 'GET'])
# def log_in():
#     if current_user.is_authentificated:
#         return redirect(url_for('main'))
    
#     else:
#         login_form = LoginForm

#         if login_form.validate_on_submit():