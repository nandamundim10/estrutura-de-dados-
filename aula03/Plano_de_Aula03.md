# Plano de Aula 03: Recursividade e Análise de Algoritmos

**Disciplina:** Estruturas de Dados (IBM3114)
**Data:** 04/03 (Quarta-feira)
**Carga Horária:** 4 tempos de 50 minutos (200 minutos no total)
**Público-alvo:** Estudantes de Ciência de Dados & IA

## 1. Objetivos de Aprendizagem
Conforme definido no cronograma e no plano de ensino, ao final desta aula o estudante será capaz de:
1.  **Diferenciar** abordagens iterativas de abordagens recursivas na resolução de problemas.
2.  **Implementar** funções recursivas em Python, identificando o caso base e o passo recursivo.
3.  **Compreender** o conceito de complexidade de algoritmos e a notação Big O (O).
4.  **Realizar a medição de tempo** de execução de código para comparar eficiência na prática.

## 2. Conteúdos Abordados
*   Definição de algoritmos iterativos vs. recursivos.
*   Funções recursivas, recursão em cauda e pilha de chamadas (Stack).
*   Análise de complexidade: crescimento de funções e Notação O (Big O).
*   Comparação prática de desempenho.

## 3. Recursos Didáticos
*   Computador com ambiente Python configurado (VS Code ou Jupyter Notebook).
*   Projetor para demonstração de código e slides.
*   Quadro branco para desenhar a "Pilha de Execução" (Call Stack).

---

## 4. Cronograma Detalhado da Aula (4 Tempos de 50min)

### **Tempo 1 (00:00 - 00:50): Introdução à Recursividade**

*   **00:00 - 00:10 | Aquecimento (Contextualização):**
    *   Revisão rápida da aula anterior.
    *   *Problema disparador:* Apresentar o cálculo do Fatorial ($n!$) ou a Sequência de Fibonacci. Perguntar: "Como resolveríamos isso com um loop `for` ou `while`?" (Abordagem Iterativa).
*   **00:10 - 00:30 | Exposição Dialogada (Conceitos):**
    *   Definição de Recursão: Uma função que chama a si mesma.
    *   **Componentes essenciais:**
        1.  **Caso Base:** A condição de parada (evita o loop infinito/estouro de pilha).
        2.  **Passo Recursivo:** A chamada da função com um subproblema menor.
    *   *Demonstração no Quadro:* Desenhar a "Pilha de Chamadas" (Call Stack) para `fatorial(3)` mostrando como os contextos são empilhados e desempilhados.
*   **00:30 - 00:50 | Live Coding (Python):**
    *   Implementação conjunta da versão iterativa vs. recursiva do Fatorial.
    *   Exemplo de código baseado em boas práticas Python:
      ```python
      def factorial_recursive(n):
          """Retorna n! de forma recursiva."""
          return 1 if n < 2 else n * factorial_recursive(n - 1)
      ```

### **Tempo 2 (00:50 - 01:40): Análise de Algoritmos e Notação Big O**

*   **00:50 - 01:10 | Teoria (Complexidade):**
    *   Introdução à Análise Assintótica: Por que medir o tempo de relógio não é suficiente? (Dependência de hardware, processos em segundo plano).
    *   O que é a Notação Big O? Foco no "pior caso" e no crescimento da função conforme a entrada ($n$) aumenta.
*   **01:10 - 01:40 | Classes de Complexidade:**
    *   Apresentação visual das curvas de complexidade:
        *   $O(1)$: Constante (acesso a índice de lista).
        *   $O(n)$: Linear (loop simples, busca linear).
        *   $O(n^2)$: Quadrática (loops aninhados, Bubble Sort).
        *   $O(\log n)$: Logarítmica (Busca Binária - *teaser* para aulas futuras).
    *   *Atividade Rápida:* Mostrar snippets de código e pedir para os alunos identificarem se é $O(n)$ ou $O(n^2)$.

*(Intervalo sugerido de 10-15 min, dependendo da logística da instituição)*

### **Tempo 3 (01:40 - 02:30): Laboratório Prático (Atividade do Portfólio)**

*   **01:40 - 01:50 | Instruções da Atividade:**
    *   Conforme o **cronograma.md**, a atividade prática é: **"Fatorial (Recursivo vs Iterativo) e Medição de Tempo"**.
    *   Objetivo: Provar empiricamente as diferenças de desempenho e entender o *overhead* da recursão.
*   **01:50 - 02:30 | Mão na Massa (Coding):**
    *   Os alunos devem criar um notebook/script que:
        1.  Implemente `fatorial_iterativo(n)`.
        2.  Implemente `fatorial_recursivo(n)`.
        3.  Utilize a biblioteca `time` ou `timeit` para medir o tempo de execução para valores crescentes de $n$ (ex: 10, 100, 500, 900).
        4.  **Desafio:** Tentar executar para um $n$ muito grande (ex: 5000) para provocar propositalmente o `RecursionError` (Estouro de Pilha), ilustrando o limite da recursão no Python (geralmente 1000 chamadas).

### **Tempo 4 (02:30 - 03:20): Análise de Resultados e Tópicos Avançados**

*   **02:30 - 02:50 | Discussão dos Resultados:**
    *   Comparar os tempos obtidos pelos alunos.
    *   *Insight Pedagógico:* Discutir por que, em Python, a recursão tende a ser mais lenta (custo de alocação de frames na pilha) do que a iteração simples, apesar de muitas vezes ser mais legível.
*   **02:50 - 03:10 | Recursão em Cauda (Tail Recursion):**
    *   Explicar o conceito de *Tail Recursion* (Item 2 da Ementa): Quando a chamada recursiva é a última ação da função.
    *   *Nota técnica:* Mencionar que o interpretador Python padrão não otimiza recursão em cauda automaticamente (diferente de linguagens como C++ ou Scheme), mas é um conceito vital em Ciência da Computação.
*   **03:10 - 03:20 | Encerramento e Commit:**
    *   Instruções finais para subir o código no GitHub (compondo a Avaliação Continuada AC).
    *   *Gancho para a próxima aula (11/03):* "Agora que sabemos medir a eficiência, como aplicamos isso para armazenar dados? Na próxima aula: Vetores e Matrizes."

---

## 5. Avaliação da Aula
A avaliação será formativa, baseada na conclusão da **Atividade Prática do Portfólio**. O professor deve circular pelo laboratório verificando:
1.  Se a implementação recursiva possui condição de parada correta.
2.  Se a medição de tempo foi implementada corretamente.
3.  Se o aluno compreendeu o erro de estouro de pilha (`RecursionError`).