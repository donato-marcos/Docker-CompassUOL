# Docker Compose para Aplicação com PostgreSQL e pgAdmin

Este projeto utiliza uma configuração pronta do Docker Compose para executar uma aplicação que utilizad o banco de dados PostgreSQL com pgAdmin simples. O repositório original [`awesome-compose`](https://github.com/docker/awesome-compose/tree/master) da Docker já fornece um ambiente funcional sem a necessidade de criar manualmente um Dockerfile.


## Instruções para configurar o ambiente

1. **Clone o repositório awesome-compose**:
   ```bash
   git clone https://github.com/docker/awesome-compose.git
   ```

2. **Copie o diretório do projeto PostgreSQL + pgAdmin**:
   ```bash
   cp -r ~/awesome-compose/postgresql-pgadmin/ ~/08/
   ```

3. **Execute o Docker Compose**:
   ```bash
   docker compose -f postgresql-pgadmin/compose.yaml up -d
   ```

## Serviços configurados

O arquivo `compose.yaml` configura dois serviços:

1. **PostgreSQL**:
   - Imagem: `postgres:latest`
   - Porta: 5432
   - Variáveis de ambiente para configuração (usuário, senha, banco de dados)

2. **pgAdmin**:
   - Imagem: `dpage/pgadmin4`
   - Porta: 80 mapeada para 5050 no host
   - Variáveis de ambiente para configuração (email, senha)

## Acesso aos serviços

- **pgAdmin**: Acesse `http://IP_do_Docker:5050` no seu navegador
  - Email: `your@email.com`
  - Senha: `changeit`

- **PostgreSQL**: Pode ser acessado via pgAdmin ou diretamente na porta 5432

## Valores Padrão

Caso não modifique o `.env`, os valores padrão serão:

- **PostgreSQL**:
  - Usuário: `yourUser`
  - Senha: `changeit`
  - Banco de dados: `postgres`

- **pgAdmin**:
  - Email: `your@email.com`
  - Senha: `changeit`

## Recomendações de Segurança

1. Altere as senhas padrão antes de usar em produção
2. Não comite o arquivo `.env` com senhas reais no versionamento

## Observações

- Não é necessário construir imagens customizadas (Dockerfile) para esta configuração
- Todos os serviços serão executados em containers Docker
- Os dados do PostgreSQL são persistidos em volume Docker
