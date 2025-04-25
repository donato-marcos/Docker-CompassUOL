# Análise de Vulnerabilidades em Imagens Docker Python

Este projeto analisa vulnerabilidades em imagens Docker Python usando a ferramenta Trivy, comparando as versões `python:3.9-slim` (Debian) e `python:3.9-alpine` (Alpine).

## Resultados da Análise

### Imagem `python:3.9-slim` (Debian)
- **Total de vulnerabilidades**: 108
  - 105 em pacotes do sistema operacional
  - 3 em pacotes Python
- **Principais problemas**:
  - `zlib1g`: CVE-2023-45853 (CRITICAL)
  - `perl-base`: CVE-2023-31484 (HIGH)
  - `setuptools`: CVE-2022-40897 (HIGH) e CVE-2024-6345

### Imagem `python:3.9-alpine` (Alpine)
- **Total de vulnerabilidades**: 4
  - 1 em pacotes do sistema (MEDIUM)
  - 3 em pacotes Python (1 MEDIUM + 2 HIGH)
- **Principais problemas**:
  - `sqlite-libs`: CVE-2025-29087 (MEDIUM)
  - `setuptools`: CVE-2022-40897 (HIGH) e CVE-2024-6345

## Recomendações

1. **Para Dockerfiles existentes**:
   ```dockerfile
   FROM python:3.9-alpine
   
   RUN apk update && apk upgrade --no-cache
   
   RUN pip install --upgrade pip==23.3 setuptools==70.0.0
   ```

2. **Melhorias de segurança**:
   - Prefira a imagem Alpine pela menor superfície de ataque
   - Mantenha sempre os pacotes atualizados
   - Execute verificações regulares com Trivy

## Como Executar a Análise

1. Analise uma imagem:
   ```bash
   trivy image python:3.9-alpine
   ```

## 📌 Conclusão

A imagem Alpine apresenta significativamente menos vulnerabilidades e é a melhor escolha para ambientes de produção quando se usa Python 3.9. As vulnerabilidades em pacotes Python podem ser resolvidas com atualizações simples.

Atualizações frequentes e varreduras regulares são essenciais para manter a segurança dos containers.
