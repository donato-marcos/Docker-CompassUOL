# Docker GS Ping - Comparação entre Build de Um Estágio e Multi-Estágio

Este projeto demonstra a diferença entre construir uma imagem Docker usando um único estágio versus um build multi-estágio para uma aplicação Go [(GS Ping)](https://github.com/docker/docker-gs-ping).

## Resultados das Imagens

Como podemos ver nos resultados do comando `docker images`:

```
REPOSITORY                   TAG       IMAGE ID       CREATED        SIZE
gs-ping_multi-stage          latest    c3425foc64ae   11 minutes ago 28.3MB
gs-ping_one-stage            latest    14cf38030744   14 minutes ago 1.176GB
```
![image](https://github.com/user-attachments/assets/32713a87-08b6-4d78-867d-99339d9e077b)


## Comparação

- **Build de um estágio**: 1.176GB
- **Build multi-estágio**: 28.3MB

O build multi-estágio resultou em uma imagem aproximadamente **41 vezes menor** que a imagem de estágio único.

## Como Reproduzir

1. Clone o repositório:
   ```bash
   git clone https://github.com/docker/docker-gs-ping.git
   ```

2. Copie para o diretório de trabalho:
   ```bash
   cp -r ~/docker-gs-ping/ ~/06/
   cd ~/06/docker-gs-ping
   ```

3. Construa as imagens:
   ```bash
   docker buildx build -f Dockerfile -t gs-ping_one-stage .
   docker buildx build -f Dockerfile.multistage -t gs-ping_multi-stage .
   ```

## Benefícios do Multi-Estágio

- Redução significativa do tamanho da imagem final
- Imagem final contém apenas o binário necessário, sem ferramentas de compilação
- Mais seguro (menor superfície de ataque)
- Mais eficiente para deploy e transferência
