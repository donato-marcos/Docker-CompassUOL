# Landing Page Dockerizada

Este projeto é uma landing page simples empacotada em um container Docker para fácil implantação.

## Visão Geral

A aplicação consiste em:
- Uma página HTML estática (`index.html`)
- Uma imagem (`hero.png`)
- Servida pelo Nginx em um container Docker

## Tecnologias Utilizadas

- **Docker** - Para containerização e implantação consistente
- **Nginx** - Servidor web leve e eficiente
- **Tailwind CSS** - Framework CSS utilitário

## Dockerfile

```dockerfile
FROM nginx

RUN mkdir -p /usr/share/nginx/html && \
    chown -R nginx:nginx /usr/share/nginx/html && \
    chmod -R 755 /usr/share/nginx/html

COPY --chown=nginx:nginx --chmod=644 ./tailwind/ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```
[Dockerfile]()

Este Dockerfile simples:
1. Utiliza a imagem oficial do Nginx como base
2. Copia o conteúdo da pasta `tailwind` (que deve conter `index.html` e `hero.png`)
3. Expõe a porta 80 padrão do Nginx

## Docker Compose

```yaml
name: web_landing

services:
  landing-page:
    build: .
    ports:
      - "8080:80"
    restart: unless-stopped
```
[docker-compose.yml]()

O arquivo `docker-compose.yml` simplifica o gerenciamento do container com:
- Build automático da imagem
- Mapeamento de portas
- Política de reinício automático

## Como Executar

### Pré-requisitos
- Docker instalado (versão 20.10+ recomendada)
- Docker Compose (se estiver usando o método compose)

## Estrutura do Projeto

```
01
├── Dockerfile          # Configuração do container
├── docker-compose.yml  # Configuração do compose
├── tailwind
│   ├── index.html      # Página principal
│   └── hero.png        # Imagem do cabeçalho
```

### Passos

1. Construa a imagem Docker:
   ```bash
   docker build -t landing-page .
   ```

2. Execute o container:
   ```bash
   docker run -d -p 8080:80 --name minha-landing landing-page
   ```

3. Acesse a aplicação:
   - Abra `http://IP_do_Docker:8080` no navegador

## Benefícios do Docker

- **Portabilidade**: Roda consistentemente em qualquer ambiente com Docker
- **Isolamento**: Não interfere com outras aplicações no host
- **Fácil implantação**: Pode ser implantado em qualquer serviço de nuvem que suporte containers
- **Versionamento**: Cada build pode ser versionado com tags

## Gerenciamento do Container

- Para parar o container:
  ```bash
  docker stop minha-landing
  ```

- Para reiniciar:
  ```bash
  docker start minha-landing
  ```

- Para remover:
  ```bash
  docker rm minha-landing
  ```


