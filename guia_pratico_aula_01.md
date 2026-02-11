# Guia Prático - Aula 01: Setup & Benchmark

**Objetivo:** Configurar seu ambiente de desenvolvimento e realizar o primeiro exercício de análise de desempenho da disciplina.
**Tempo Estimado:** 40 minutos

---

## Parte 1: Preparação do Ambiente (Setup)

### 1. Instalação do Python
1. Baixe o instalador mais recente em [python.org](https://www.python.org/downloads/).
2. **IMPORTANTE:** Durante a instalação, marque a caixinha:  
   `[x] Add Python to PATH`
3. Instale.
4. Abra o Terminal (Prompt de Comando ou PowerShell) e digite:
   ```bash
   python --version
   ```
   *Se aparecer a versão (ex: Python 3.12.0), sucesso!*

### 2. Instalação do VS Code
1. Baixe e instale o [Visual Studio Code](https://code.visualstudio.com/).
2. Abra o VS Code.
3. No menu lateral esquerdo, clique em **Extensions** (ícone de quadrados).
4. Procure por `Python` (Microsoft) e instale.

### 3. Configuração do Git
1. Se não tiver, baixe o [Git](https://git-scm.com/downloads).
2. Configure seu nome e e-mail (usado para assinar seus commits):
   ```bash
   git config --global user.name "Seu Nome"
   git config --global user.email "seu.email@exemplo.com"
   ```

---

## Parte 2: O Desafio de Performance (Benchmark)

### 1. Clone o Repositório Template
1. Crie uma pasta `IBEMEC` no seu computador.
2. Abra essa pasta no terminal e clone o repositório da atividade:
   ```bash
   git clone [URL_DO_REPO_DO_PROFESSOR]
   ```
   *(Ou baixe o ZIP se preferir, mas Git é melhor)*

### 2. Analise o Código
Abra o arquivo `aula01/benchmark_inicial.py` no VS Code. O código faz o seguinte:
- Gera uma lista com **1 milhão** de números aleatórios.
- Ordena essa lista usando o algoritmo `Timsort` (padrão do Python).
- Mede o tempo exato que isso levou.

**Snippet do Código:**
```python
import time
import random

# ... código omitido ...

# 2. Processamento (O Algoritmo)
print("Ordenando...")
inicio = time.time()
dados.sort() # Timsort (O(n log n))
fim = time.time()

tempo = fim - inicio
print(f"Concluído! Tempo de execução: {tempo:.4f} segundos.")
```

### 3. Execute o Script
No terminal do VS Code (`Ctrl + '`), execute:
```python
python aula01/benchmark_inicial.py
```

### 4. Registre seu Resultado
1. Anote o tempo de execução (ex: `0.1543 segundos`).
2. Abra o arquivo `README.md`.
3. Adicione uma linha com o modelo da sua CPU e o tempo obtido. Exemplo:
   > **Meu Benchmark:**
   > - **Processador:** Intel Core i7 10th Gen
   > - **Tempo:** 0.1420s

### 5. (Opcional) Crash Test 💥
Se sua máquina for rápida, tente aumentar o número de elementos para **10 milhões** na linha 8:
```python
n = 10_000_000
```
Rode novamente. O tempo aumentou linearmente (10x) ou exponencialmente? E a memória?

---

## Parte 3: Envio da Atividade

1. Adicione os arquivos ao Git:
   ```bash
   git add .
   ```
2. Salve as alterações (Commit):
   ```bash
   git commit -m "Atividade Aula 01: Setup e Benchmark"
   ```
3. Envie para o seu repositório (Push):
   *Nota: Aqui você precisará criar seu próprio repo no GitHub e apontar o remote.*
   ```bash
   git remote set-url origin [URL_DO_SEU_NOVO_REPO]
   git push -u origin main
   ```

**Parabéns!** Você configurou seu ambiente. 🚀

