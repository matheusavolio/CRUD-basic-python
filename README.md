# Estrutura do Projeto

este projeto está organizado de forma modular, com o código dividido em três partes principais:

- **main.py**: contém o ponto de entrada e a lógica de controle do programa, além do menu de opções.
- **crudFunctions**: implementa as operações CRUD (create, read, update, delete) que manipulam uma lista de registros.
- **colors**: define cores para mensagens de sucesso, erro e avisos no terminal, facilitando a identificação visual.

---

## main.py - ponto de entrada e menu interativo

este é o script principal do programa, onde o usuário interage com um menu que permite realizar operações de cadastro, visualização, atualização e exclusão de registros. abaixo está uma descrição detalhada das funcionalidades implementadas no loop principal:

### Estrutura do Menu

o programa exibe opções numéricas para que o usuário escolha a ação desejada:

- `[0]` - sair do programa
- `[1]` - novo cadastro (create)
- `[2]` - ler cadastros (read)
- `[3]` - editar cadastros (update)
- `[4]` - remover cadastros (delete)

### Tratamento de Erros

- utiliza `try-except` para capturar exceções, como `ValueError` para entradas inválidas e `KeyboardInterrupt` para interrupções manuais, exibindo mensagens de erro de acordo com o tipo de problema.
- mensagens coloridas de erro e sucesso são exibidas, tornando a experiência de uso mais amigável.

---

## crudFunctions/__init__.py - implementação das funções CRUD

este módulo contém funções que realizam operações de criação, leitura, atualização e exclusão de registros em uma lista chamada `registerList`. cada função realiza uma tarefa específica e fornece feedback ao usuário. aqui está uma visão detalhada das funções principais:

- `newRegister(id, name, email, password)`: cria um novo registro na lista `registerList` utilizando um dicionário para armazenar os dados do usuário. após adicionar o registro, exibe uma mensagem de sucesso.
- `viewRegisters()`: exibe todos os registros presentes em `registerList`, com o id, name, email e password de cada usuário. se a lista estiver vazia, informa o usuário para adicionar registros antes de tentar visualizá-los.
- `updateRegister(idFound, nameUpdate, emailUpdate, passwordUpdate)`: atualiza as informações de um registro existente, identificando-o pelo id. caso o id não seja encontrado, exibe uma mensagem de erro para informar o usuário.
- `deleteRegister(id)`: remove um registro da lista com base no id fornecido pelo usuário. caso o registro não exista, exibe uma mensagem de erro.

---

## colors/__init__.py - personalização de mensagens com cores

este módulo define variáveis de cores para facilitar a exibição de mensagens formatadas no terminal. as cores incluem verde para mensagens de sucesso, vermelho para erros e azul para mensagens de aviso. essas variáveis tornam o código mais legível e ajudam a melhorar a usabilidade da interface de linha de comando.

---

## Reflexão e Aprendizado

este projeto demonstra como estruturar um sistema de cadastro simples com funcionalidades CRUD, utilizando boas práticas de programação em Python:

- **modularização**: a divisão do código em módulos específicos ajuda na manutenção e na legibilidade do projeto.
- **tratamento de erros**: o uso de `try-except` para capturar erros comuns é essencial para criar uma experiência de usuário robusta.
- **feedback visual**: mensagens coloridas melhoram a UX (experiência do usuário) no terminal, tornando o programa mais intuitivo.
