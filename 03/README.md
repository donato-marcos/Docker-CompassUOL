
# Listando e removendo containers

## Listar Containers

**Todos os containers (executando e parados):**
```bash
docker ps -a
```
![image](https://github.com/user-attachments/assets/6018bde1-0eef-4828-9f86-37bf62183f65)

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
![image](https://github.com/user-attachments/assets/fee41f8b-1e79-4c49-923a-7f68de8a9f34)

![image](https://github.com/user-attachments/assets/a95f1938-0413-46c7-9dff-e4024f50b6de)

**Remover um container mesmo se estiver em execução (força a parada):**
```bash
docker rm -f meu_container
```

**Limpar todos os containers parados:**
```bash
docker container prune
```
![image](https://github.com/user-attachments/assets/849a7cf9-a3e9-4b1e-a50d-02867aef64b0)

