# README - Comunicação entre Containers Docker (Node.js e MongoDB)

## Objetivo
Este projeto demonstra como criar uma rede Docker personalizada para permitir a comunicação entre dois containers: um servidor Node.js/Express e um banco de dados MongoDB, utilizando o projeto React Express + Mongo do repositório [`awesome-compose`](https://github.com/docker/awesome-compose/tree/master).

## Pré-requisitos
- Docker instalado na máquina
- Git instalado (para clonar o repositório)

## Passos realizados

1. **Clonar o repositório awesome-compose**:
   ```bash
   git clone https://github.com/docker/awesome-compose.git
   ```

2. **Copiar o projeto react-express-mongodb**:
   ```bash
   cp -r ~/awesome-compose/react-express-mongodb ~/07/
   ```

3. **Iniciar os containers**:
   ```bash
   docker compose -f react-express-mongodb/compose.yaml up -d
   ```

## Observações

- O Docker Compose já configura automaticamente uma rede para os containers se comunicarem
- Não foi necessário criar um Dockerfile personalizado, pois o projeto já contém toda a configuração necessária
- Os containers estão configurados para se comunicar usando os nomes de serviço definidos no arquivo compose.yaml

## Acessando a aplicação

Após iniciar os containers, você pode acessar:
- Frontend React: http://IP_do_Docker:3000


