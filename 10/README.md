# Evitar Execução como Root

Este projeto demonstra como configurar um container Docker para executar uma aplicação Python com um usuário não-root, reduzindo riscos de segurança.

## Visão Geral

A aplicação consiste em:
- Um script Python (`script.py`) que verifica e exibe o UID e GID do usuário atual
- Um Dockerfile configurado para criar um usuário não-root e executar o script com esse usuário

## Tecnologias Utilizadas

- **Docker** - Para containerização e implantação segura
- **Python** - Linguagem de programação para o script de exemplo

## Script Python

```python
#!/usr/bin/env python3

import os
import time

while True:
    print("Verificando usuário atual:")
    print(f"User ID (UID): {os.getuid()}")
    print(f"Group ID (GID): {os.getgid()}")
    print("------")
    time.sleep(2)  # Pausa de 2 segundos
```

## Dockerfile

```dockerfile
FROM python:slim

WORKDIR /script

RUN groupadd -r teste && useradd -r -g teste teste && \
    mkdir -p /home/teste && \
    chown -R teste:teste /home/teste

COPY --chown=teste:teste --chmod=744 script.py .

USER teste

EXPOSE 8000

CMD ["python", "script.py"]
```
[Dockerfile](Dockerfile)

Este Dockerfile:
1. Utiliza a imagem oficial Python slim como base
2. Cria um usuário e grupo `teste`
3. Configura permissões adequadas
4. Define o usuário `teste` como padrão para execução
5. Executa o script Python

## Docker Compose

```yaml
name: python

services:
  script:
    build: .
    ports:
      - "8000:8000"
```
[docker-compose.yml](docker-compose.yml)

O arquivo `docker-compose.yml` simplifica a execução com:
- Build automático da imagem
- Mapeamento de portas

## Como Executar

### Pré-requisitos
- Docker instalado (versão 20.10+ recomendada)
- Docker Compose (opcional)

### Estrutura do Projeto

```
10
├── Dockerfile          # Configuração do container
├── docker-compose.yml  # Configuração do compose
├── script.py           # Script Python principal
└── README.md           # Documentação
```

### Passos

#### Método Docker CLI

1. Construa a imagem Docker:
   ```bash
   docker build -t python-script .
   ```

2. Execute o container:
   ```bash
   docker run -d -p 8000:8000 --name meu_container python-script
   ```

3. Verifique o usuário em execução:
   ```bash
   docker exec meu_container whoami
   ```
   Saída esperada: `teste`
   
   ![image](https://github.com/user-attachments/assets/2f34dff3-53f7-4654-9d76-621d16b35510)


#### Método Docker Compose

1. Execute o compose:
   ```bash
   docker-compose up -d
   ```

2. Verifique o usuário em execução:
   ```bash
   docker-compose exec script whoami
   ```
   Saída esperada: `teste`
   
   ![image](https://github.com/user-attachments/assets/a6316648-e2a8-4065-8234-8801680a61b1)


4. Acesse os logs do script:
   ```bash
   docker-compose logs -f
   ```
   ![image](https://github.com/user-attachments/assets/1456cc33-eae8-4b08-ad80-4ac434fe6e87)


## Benefícios da Execução como Não-Root

- **Segurança melhorada**: Minimiza o impacto de possíveis vulnerabilidades
- **Melhores práticas**: Alinha-se com recomendações de segurança do Docker
- **Isolamento**: Limita os privilégios do container no sistema host

## Gerenciamento do Container

### Para containers criados via Docker CLI

- Para parar o container:
  ```bash
  docker stop meu_container
  ```

- Para reiniciar:
  ```bash
  docker start meu_container
  ```

- Para remover:
  ```bash
  docker rm meu_container
  ```

### Para containers criados via Docker Compose

- Para parar e remover:
  ```bash
  docker-compose down
  ```

- Para reiniciar:
  ```bash
  docker-compose restart
  ```

- Para visualizar logs:
  ```bash
  docker-compose logs -f
  ```
