# Projeto Flask 🚀

Este projeto configura e implementa uma aplicação Flask com funcionalidades de registro de usuário, login, gerenciamento de tarefas e redefinição de senha via email.

## Visão Geral

A aplicação é composta pelos seguintes componentes principais:
- **Flask**: Microframework para desenvolvimento web em Python.
- **SQLAlchemy**: ORM para interação com banco de dados.
- **Flask-Login**: Gerenciamento de sessões de usuário.
- **SendGrid**: Envio de emails para redefinição de senha.
- **Pytest**: Framework para testes automatizados.

## Estrutura do Projeto

├── .github/workflows/ │ └── ci.yml# Workflow de CI para testes automatizados ├── app/ │ ├── init.py # Inicialização da aplicação Flask │ ├── models.py# Definição dos modelos de banco de dados │ ├── routes.py# Definição das rotas da aplicação │ ├── templates/ # Templates HTML para a aplicação │ │ ├── dashboard.html│ │ ├── home.html│ │ ├── login.html│ │ ├── profile.html│ │ ├── register.html│ │ ├── reset_password.html │ │ └── tasks.html│ ├── static/ │ └── styles.css# Arquivo de estilo CSS ├── instance/ │ └── database.db# Banco de dados SQLite ├── tests/ │ └── test_routes.py # Testes automatizados para as rotas ├── venv/ # Ambiente virtual ├── .gitignore # Arquivos e pastas ignorados pelo Git ├── README.md# Documentação do projeto └── requirements.txt# Dependências do projeto


## Configuração e Implementação

### 1. Configuração Inicial

1. Clone este repositório:
   ```sh
   git clone https://github.com/izadorasobral/projeto-flask.git
   cd projeto-flask
Crie e ative um ambiente virtual:

sh
python -m venv venv
source venv/bin/activate   # No Windows use: .\venv\Scripts\Activate
Instale as dependências:

sh
pip install -r requirements.txt
Configure a variável SENDGRID_API_KEY no arquivo app/routes.py com sua chave de API do SendGrid.

2. Deploy da Aplicação
Inicie a aplicação:

sh
flask run
Acesse a aplicação em http://127.0.0.1:5000.

3. Testes
Para rodar os testes, execute:

sh
pytest

## Contribuição
Se quiser contribuir, sinta-se à vontade para abrir uma issue ou enviar um pull request!
