
# Listando e removendo containers

### Listar Containers

**Todos os containers (executando e parados):**
```bash
docker ps -a

**Apenas containers em execução:**
```bash
docker ps
```

## Parar um Container

Para parar um container em execução:
```bash
docker stop meu_container
```

## Remover um Container

Para remover um container (deve estar parado primeiro):
```bash
docker rm meu_container
```

## Comandos Úteis

Se quiser parar e remover todos os containers de uma vez, pode usar:

```bash
docker stop $(docker ps -aq)  # Para todos os containers
docker rm $(docker ps -aq)    # Remove todos os containers
```

**Remover um container mesmo se estiver em execução (força a parada):**
```bash
docker rm -f meu_container
```

**Limpar todos os containers parados:**
```bash
docker container prune
```
