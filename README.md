markdown
# Projeto Flask 🚀

Este projeto configura e implementa uma aplicação Flask com funcionalidades de registro de usuário, login, gerenciamento de tarefas e redefinição de senha via email.

## Visão Geral

A aplicação é composta pelos seguintes componentes principais:
- **Flask**: Microframework para desenvolvimento web em Python, usado para construir a estrutura principal da aplicação.
- **SQLAlchemy**: ORM para interação com banco de dados, utilizado para gerenciar os dados dos usuários e das tarefas.
- **Flask-Login**: Gerenciamento de sessões de usuário, responsável por manter os usuários logados e proteger as rotas que requerem autenticação.
- **SendGrid**: Serviço utilizado para o envio de emails de redefinição de senha, garantindo que os usuários possam recuperar suas contas.
- **Pytest**: Framework para testes automatizados, utilizado para garantir que todas as funcionalidades da aplicação estejam funcionando corretamente.


## Configuração e Implementação

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

4. Funcionalidades da Aplicação
-Registro de Usuário
Permite que novos usuários se registrem na aplicação fornecendo um email e uma senha.

-Login de Usuário
Permite que usuários registrados façam login na aplicação fornecendo suas credenciais.

-Gerenciamento de Tarefas
Permite que usuários autenticados criem, atualizem e excluam tarefas. As tarefas são associadas ao usuário que as criou.

-Redefinição de Senha via Email
Permite que usuários recuperem suas contas através de um email de redefinição de senha enviado pelo SendGrid.

5. Monitoramento e Alertas
Configuração de alertas para eventos importantes na aplicação.

Dashboard de monitoramento para acompanhar o desempenho em tempo real.

## Contribuição
Se quiser contribuir, sinta-se à vontade para abrir uma issue ou enviar um pull request!
