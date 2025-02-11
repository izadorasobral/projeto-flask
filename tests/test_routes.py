import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app, db
from app.models import User, Task

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_register(client):
    response = client.post('/register', data={
        'email': 'test@example.com',
        'password': 'password'
    })
    assert response.status_code == 302  # Redirecionamento após registro

    user = User.query.filter_by(email='test@example.com').first()
    assert user is not None

def test_login(client):
    # Primeiro, registre um usuário
    client.post('/register', data={
        'email': 'test@example.com',
        'password': 'password'
    })

    # Agora faça login com o usuário registrado
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password'
    })
    assert response.status_code == 302  # Redirecionamento após login

def test_create_task(client):
    # Primeiro, registre e faça login com um usuário
    client.post('/register', data={
        'email': 'test@example.com',
        'password': 'password'
    })
    client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password'
    })

    # Agora crie uma nova tarefa
    response = client.post('/tasks', data={
        'name': 'Nova Tarefa'
    })
    assert response.status_code == 302  # Redirecionamento após criação da tarefa

    task = Task.query.filter_by(name='Nova Tarefa').first()
    assert task is not None
