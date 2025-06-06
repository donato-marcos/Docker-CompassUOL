# Material Kit com Docker

Este projeto containeriza o Material Kit do Creative Tim usando Nginx em um container Docker para fácil implantação e desenvolvimento.

## Visão Geral

A aplicação consiste em:
- Páginas HTML/CSS/JS estáticas do Material Kit
- Servidas pelo Nginx em um container Docker otimizado
- Configuração simplificada com Docker Compose

## Tecnologias Utilizadas

- **Docker** - Para containerização e implantação consistente
- **Nginx (Alpine)** - Servidor web leve e eficiente
- **Material Kit** - Design system moderno para landing pages

# Clone o repositório (se ainda não tiver feito)

```bash
git clone https://github.com/creativetimofficial/material-kit.git
```

## Dockerfile

```dockerfile
FROM nginx:alpine

COPY material-kit /usr/share/nginx/html

RUN chmod -R 755 /usr/share/nginx/html

EXPOSE 80
```
[Dockerfile](Dockerfile)

Este Dockerfile:
1. Utiliza a imagem otimizada do Nginx Alpine como base
2. Copia o conteúdo da pasta `material-kit` para o diretório do Nginx
3. Garante as permissões corretas para os arquivos estáticos
4. Expõe a porta 80 padrão do Nginx

## Docker Compose

```yaml
services:
  material-kit:
    build: .
    ports:
      - "8080:80"
    volumes:
      - ./material-kit:/usr/share/nginx/html
```
[docker-compose.yml](docker-compose.yml)

O arquivo `docker-compose.yml` oferece:
- Build automático da imagem
- Mapeamento de portas (8080 host → 80 container)
- Volume para desenvolvimento (alterações em tempo real)
- Configuração simplificada do serviço

## Estrutura do Projeto

```
09
├── Dockerfile          # Configuração do container
├── docker-compose.yml  # Configuração do compose
├── material-kit        # Pasta com os arquivos estáticos
```

## Como Executar

### Pré-requisitos
- Docker instalado (versão 20.10+ recomendada)
- Docker Compose (opcional, mas recomendado)

### Método Docker CLI

1. Construa a imagem Docker:
   ```bash
   docker build -t material-kit .
   ```

2. Execute o container:
   ```bash
   docker run -d -p 8080:80 --name meu-container material-kit
   ```

### Método Docker Compose (recomendado)

1. Execute o compose:
   ```bash
   docker-compose up -d
   ```

2. Acesse a aplicação:
   - Abra `http://IP_do_Docker:8080` no navegador

## Benefícios desta Implementação

- **Desempenho**: Utiliza Nginx Alpine, uma imagem leve e otimizada
- **Desenvolvimento**: Volume montado permite alterações em tempo real
- **Portabilidade**: Roda consistentemente em qualquer ambiente com Docker
- **Fácil implantação**: Pronto para produção ou desenvolvimento

## Gerenciamento do Container

### Para containers criados via Docker CLI

- Parar o container:
  ```bash
  docker stop meu-container
  ```

- Reiniciar:
  ```bash
  docker start meu-container
  ```

- Remover:
  ```bash
  docker rm meu-container
  ```

### Para containers criados via Docker Compose

- Parar e remover:
  ```bash
  docker-compose down
  ```

- Reiniciar:
  ```bash
  docker-compose restart
  ```

- Visualizar logs:
  ```bash
  docker-compose logs
  ```

## Personalização

Para modificar o conteúdo:
1. Edite os arquivos no diretório `material-kit/`
2. Se estiver usando Docker Compose, as alterações aparecerão automaticamente
3. Para versão sem volume, reconstrua a imagem:
   ```bash
   docker-compose up -d --build
   ```

## Créditos

A página utilizada é o [Material Kit](https://github.com/creativetimofficial/material-kit) do Creative Tim, distribuído sob licença MIT.
