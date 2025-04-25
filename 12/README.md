# Análise e Correção de Vulnerabilidades em Imagens Docker

Este projeto demonstra a importância de corrigir vulnerabilidades em imagens Docker e como escolher imagens base mais seguras pode reduzir significativamente os riscos de segurança.

## Análise das Vulnerabilidades

O Trivy foi utilizado para analisar diferentes versões da imagem Python:

| Imagem                     | Total Vulnerabilidades | Críticas | Altas | Médias | Baixas |
|----------------------------|-----------------------|----------|-------|--------|--------|
| python:3.9 (Debian)        | 5343                  | 1        | 2     | 31     | 71     |
| python:3.9-slim (Debian)   | 411                   | 1        | 2     | 31     | 71     |
| python:3.9-alpine          | 31                    | 0        | 0     | 1      | 0      |
| python-alpine (atualizada) | 0                     | 0        | 0     | 0      | 0      |

## Melhorias Aplicadas

1. **Imagem Base Mais Segura**:
   - Substituição da imagem `python:3.9` (Debian) por `python:3.9-alpine`
   - Atualização para a versão mais recente da imagem Alpine

2. **Redução de Privilégios**:
   - Criação de usuário não-root para execução da aplicação

3. **Atualização de Dependências**:
   - Atualização das versões do Flask e Requests para corrigir vulnerabilidades conhecidas

## Dockerfile Melhorado

```dockerfile
FROM python:3.9-alpine
RUN apk update && apk upgrade --no-cache
WORKDIR /app
COPY requirements_alpine.txt .
RUN pip install --no-cache-dir -r requirements_alpine.txt
RUN adduser -S -h teste teste
COPY . .
USER teste
CMD ["python", "./app.py"]
```

## requirements.txt Atualizado

```
flask==2.2.5
requests==2.32.0
```

## Como Executar

1. Construa a imagem:
   ```bash
   docker buildx build -t meu-container-seguro .
   ```

2. Execute o container:
   ```bash
   docker run -p 5000:5000 meu-container-seguro
   ```

## Conclusão

Ao utilizar uma imagem base mais enxuta (Alpine) e atualizada, reduzimos o número de vulnerabilidades de 5343 para 0. Além disso, a implementação de usuário não-root e a atualização das dependências aumentam significativamente a segurança da aplicação.
