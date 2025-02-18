Feature: Operações CRUD na API de Login

  Scenario: Criar um novo usuário
    Given que eu crio um novo usuário com nome "testuser" e senha "senha123"
    When eu envio uma requisição POST para "/user"
    Then devo receber uma resposta 200

  Scenario: Buscar detalhes do usuário
    Given que tenho um usuário existente com nome "testuser"
    When eu envio uma requisição GET para "/user/testuser"
    Then devo receber uma resposta 200

  Scenario: Atualizar detalhes do usuário
    Given que tenho um usuário existente com nome "testuser"
    When eu envio uma requisição PUT para "/user/testuser" com nova senha "novaSenha123"
    Then devo receber uma resposta 200

  Scenario: Deletar usuário
    Given que tenho um usuário existente com nome "testuser"
    When eu envio uma requisição DELETE para "/user/testuser"
    Then devo receber uma resposta 200
