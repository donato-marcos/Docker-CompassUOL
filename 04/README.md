# Projeto Flask com Docker Compose

Este projeto utiliza uma configuração pronta do Docker Compose para executar uma aplicação Flask simples. O repositório original `[awesome-compose]`(https://github.com/docker/awesome-compose/tree/master) da Docker já fornece um ambiente funcional sem a necessidade de criar manualmente um Dockerfile.

### Como executar o projeto

1. Clone o repositório `awesome-compose`:
   ```bash
   git clone https://github.com/docker/awesome-compose.git
   ```

2. Copie a pasta do projeto Flask para o seu diretório de trabalho:
   ```bash
   cp -r awesome-compose/flask ~/04/
   ```

3. Execute o serviço usando Docker Compose:
   ```bash
   docker compose -f flask/compose.yaml up -d
   ```

### Observações
- O arquivo `compose.yaml` já contém toda a configuração necessária, incluindo a construção da imagem Docker e a exposição da aplicação Flask.
- A aplicação estará disponível no endpoint configurado (geralmente `http://localhost:8000`).
