# Instruções para Criar e Utilizar Volumes para Persistência de Dados com MySQL

Este projeto utiliza uma configuração pronta do Docker Compose para executar uma aplicação que utilizad o banco de dados MySQL simples. O repositório original [`awesome-compose`](https://github.com/docker/awesome-compose/tree/master) da Docker já fornece um ambiente funcional sem a necessidade de criar manualmente um Dockerfile.

## Passo a Passo

1. **Clonar o repositório awesome-compose**:
   ```bash
   git clone https://github.com/docker/awesome-compose.git
   ```

2. **Copiar o projeto react-express-mysql**:
   ```bash
   cp -r ~/awesome-compose/react-express-mysql ~/05/
   ```

3. **Iniciar os containers com Docker Compose**:
   ```bash
   docker compose -f react-express-mysql/compose.yaml up -d
   ```

## Verificação

Para confirmar que o volume foi criado e está sendo utilizado, execute:
```bash
docker volume ls
```

Você verá um volume listado, que está sendo usado pelo container MySQL para persistir os dados.
   
## Observações

- O arquivo `compose.yaml` já está configurado para utilizar volumes, garantindo a persistência dos dados do MySQL.
- Não é necessário criar ou modificar nenhum Dockerfile.
- Os dados do banco MySQL serão armazenados no volume criado automaticamente pelo Docker.
- A aplicação estará disponível no endpoint configurado (geralmente `http://IP_do_Docker:3000`).


