from flask import Flask, render_template, redirect
from data.db_session import global_init, create_session
from data.users import User
from forms import RegisterForm

app = Flask(__name__)

global_init('db/database.sqlite')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        f = create_session()
        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.email = form.email.data
        user.hashed_password = form.password.data
        f.add(user)
        f.commit()
        return redirect('/register')
    return render_template('register.html', title='Регистрация', form=form)



if __name__ == '__main__':
    app.run()