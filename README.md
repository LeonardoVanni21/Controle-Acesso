# ControleAcesso

## Descrição

Aplicação para simular um controle de acesso de usuários com permissões.

## Tecnologias

- Python
- PostgreSQL
- Flask (Framework Python)

## Instalação
pip install flask psycopg2-binary

## Configuração
1. Criar um banco de dados no PostgreSQL nome "BaseControleAcesso"
2. Executar o script: 
```bash
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE permissions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE user_permissions (
    user_id INT REFERENCES users(id),
    permission_id INT REFERENCES permissions(id),
    PRIMARY KEY (user_id, permission_id)
);
```

## Inserir dados
```bash
INSERT INTO users (username, password) VALUES 
('admin', 'Test1234'),
('user1', 'Test123');

INSERT INTO permissions (name) VALUES 
('teste_tela_comum'),
('teste_link_admin');

INSERT INTO user_permissions (user_id, permission_id) VALUES 
(1, 1),
(1, 2),
(2, 1);
```

## Executar
```bash
python app.py
```

## Acessar
http://127.0.0.1:5000/login

Login: admin

Senha: Test1234

* Nesse caso, o usuário admin tem permissão para ver o link da tela comum e o link da tela de admin.

Login: user1

Senha: Test123

* Nesse caso, o usuário user1 tem permissão para ver apenas o link da tela comum.

 
