# Algoritmo Genético (Genetic Algorithm) — Otimização de Funções

Este projeto implementa um **Algoritmo Genético (AG)** simples para **minimização** de funções matemáticas contínuas, com suporte a duas funções de teste clássicas:

- **Sphere**
- **Rastrigin**

A execução é feita via um menu interativo no terminal, onde você escolhe a função e define parâmetros como dimensão, limite, número de gerações e tamanho da população.

---

## Estrutura do projeto

- `src/main.py`  
  Interface de execução (menu) e rotina para rodar várias execuções e calcular métricas.

- `src/algoritmo.py`  
  Implementação do algoritmo genético (`algoritmo_genetico`).

- `src/funcoes.py`  
  Funções objetivo (Sphere e Rastrigin).

---

## Como o algoritmo funciona (resumo)

O AG implementado segue esta lógica:

1. **Inicializa uma população** de vetores reais (valores aleatórios em `[-limite, limite]`).
2. Para cada geração:
   - Faz **seleção por torneio** (3 candidatos) para escolher dois pais (`pai1` e `pai2`).
   - Gera um filho por **recombinação convexa** (blend) entre os pais:
     - `filho = fator * pai1 + (1 - fator) * pai2`
   - Aplica **mutação gaussiana** em cada gene:
     - `gene = gene + N(0,1) * 0.1`
3. Ao final, retorna o **melhor indivíduo** encontrado, seu valor na função, e o total de avaliações (NFE).

---

## Requisitos

- Python 3.x

Bibliotecas usadas são apenas da biblioteca padrão (`random` e `math`).

---

## Como executar

Entre na pasta `src` e rode o programa:

```bash
cd src
python main.py
```

Você verá um menu como:

- `1 - Sphere`
- `2 - Rastrigin`

E será solicitado:

- **Número de execuções**
- **Dimensão do problema**
- **Limite dos valores** (intervalo `[-limite, limite]`)
- **Número de gerações**
- **Tamanho da população**

---

## Saídas / Métricas

Para cada conjunto de execuções, o programa imprime:

- **NFE médio**: média do número de avaliações de função (no código, conta 1 avaliação por filho gerado).
- **Taxa de sucesso**: número de execuções em que `|melhor_valor| < 0.01`.

Exemplo de saída:

```
Função: Sphere
NFE médio: 5000.0
Taxa de sucesso: 8/10
```

---

## Funções objetivo disponíveis

### Sphere
Minimização de:

\[
f(x) = \sum_{i=1}^{n} x_i^2
\]

Ótimo global: `f(x)=0` em `x = (0,0,...,0)`.

### Rastrigin
Minimização de:

\[
f(x) = 10n + \sum_{i=1}^{n} (x_i^2 - 10\cos(2\pi x_i))
\]

Ótimo global: `f(x)=0` em `x = (0,0,...,0)`.
