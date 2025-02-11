import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app, db
from app.models import User, Task

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_home(client):
    response = client.get('/')
    assert b'Welcome to the Home Page' in response.data

def test_register(client):
    response = client.post('/register', data={
        'email': 'test@example.com',
        'password': 'password'
    })
    assert response.status_code == 302  # Redireciona após registro bem-sucedido

def test_login(client):
    client.post('/register', data={
        'email': 'test@example.com',
        'password': 'password'
    })
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password'
    })
    assert response.status_code == 302  # Redireciona após login bem-sucedido
