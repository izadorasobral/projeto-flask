from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, Task

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login ou senha incorretos.')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.email)

@main.route('/tasks', methods=['GET', 'POST'])
@login_required
def manage_tasks():
    if request.method == 'POST':
        task_name = request.form['name']
        new_task = Task(name=task_name, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('main.manage_tasks'))
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)

@main.route('/tasks/update/<int:id>', methods=['POST'])
@login_required
def update_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id == current_user.id:
        task.name = request.form['name']
        db.session.commit()
    return redirect(url_for('main.manage_tasks'))

@main.route('/tasks/delete/<int:id>', methods=['POST'])
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('main.manage_tasks'))

@main.route('/tasks/list', methods=['GET'])
@login_required
def list_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    tasks_list = [{'id': task.id, 'name': task.name} for task in tasks]
    return {'tasks': tasks_list}

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.email = request.form['email']
        db.session.commit()
        flash('Perfil atualizado com sucesso.')
        return redirect(url_for('main.profile'))
    return render_template('profile.html')

@main.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            # Enviar email com link de redefinição de senha (implementação necessária)
            flash('Um email com instruções de recuperação de senha foi enviado.')
        else:
            flash('Email não encontrado.')
        return redirect(url_for('main.login'))
    return render_template('reset_password.html')
