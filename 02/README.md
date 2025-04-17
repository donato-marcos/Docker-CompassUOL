# Criando e Rodando um Container Interativo Ubuntu

Para criar e rodar um container Ubuntu interativo onde você pode testar scripts Bash ou instalar pacotes, siga estes passos:

## Passo 1: Iniciar um container Ubuntu interativo

```bash
docker run -it --name meu_container ubuntu /bin/bash
```

Explicação dos parâmetros:
- `-it`: Cria uma sessão interativa com terminal
- `--name`: Define um nome para o container (opcional)
- `ubuntu`: Imagem base a ser utilizada
- `/bin/bash`: Shell a ser executado

## Passo 2: Dentro do container

Uma vez dentro do container (você verá o prompt mudar para algo como `root@container-id:/#`), você pode:

1. **Atualizar os pacotes**:
   ```bash
   apt update && apt upgrade -y
   ```

2. **Criar e executar um script Bash**:
   ```bash
   echo '
   #!/bin/bash
   echo
   echo "Date: $(date)"
   echo
   echo
   echo "Uso Mem:"
   echo "$(free -h)"
   echo
   echo
   echo "Uso HD:"
   echo "$(df -h)"
   ' > logs.sh
   ```
   ```bash
   chmod +x /meu_script.sh
   ./meu_script.sh
   ```
   Script executado:
   
   ![image](https://github.com/user-attachments/assets/79779bab-7e83-4251-bc3b-aba0c295a7a6)


## Passo 3: Saindo do container

Para sair do container sem pará-lo:
```bash
Ctrl+P seguido de Ctrl+Q
```

Para sair e parar o container:
```bash
exit
```

## Passo 4: Gerenciar o container posteriormente

Para reiniciar e reentrar no container:
```bash
docker start meu_container
docker exec -it meu_container /bin/bash
```

Para remover o container quando não for mais necessário:
```bash
docker rm meu_container
```
