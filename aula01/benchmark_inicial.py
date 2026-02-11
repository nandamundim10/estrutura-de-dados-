import time
import random

def main():
    print("Iniciando Benchmark de Ordenação...")
    
    # 1. Gerar Dados (Simulação de carga)
    n = 1_000_000
    print(f"Gerando uma lista com {n} números aleatórios...")
    dados = [random.randint(0, n) for _ in range(n)]
    
    # 2. Processamento (O Algoritmo)
    print("Ordenando...")
    inicio = time.time()
    dados.sort() # Timsort (O(n log n))
    fim = time.time()
    
    # 3. Resultado (Informação)
    tempo = fim - inicio
    print(f"Concluído! Tempo de execução: {tempo:.4f} segundos.")
    print(f"Primeiro elemento: {dados[0]}")
    print(f"Último elemento: {dados[-1]}")
    print("-" * 30)
    print("Desafio: Tente aumentar N para 10 milhões e veja o que acontece com a memória/tempo!")

if __name__ == "__main__":
    main()
