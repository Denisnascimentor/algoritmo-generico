# Algoritmo Genético (Python)

Projeto em Python que implementa um **Algoritmo Genético (AG)** para **minimização** de funções de teste. O programa permite escolher uma função objetivo via menu e executar múltiplas rodadas, exibindo **NFE médio** (número de avaliações da função) e **taxa de sucesso**.

## Estrutura do projeto

A organização (conforme o projeto está hoje) é:

```
.
└── src
    ├── algoritmo.py
    ├── funcoes.py
    └── main.py
```

## O que o projeto faz

- Gera uma **população inicial** de indivíduos (vetores reais) com valores aleatórios no intervalo `[-limite, limite]`.
- Avalia a aptidão (**fitness**) de cada indivíduo usando a **função objetivo** escolhida.
- Executa por um número de **gerações**, criando uma nova população com:
  - **Seleção por torneio (k = 3)**: escolhe o melhor entre 3 indivíduos aleatórios (duas vezes) para formar 2 pais.
  - **Crossover aritmético**: combina os pais com um fator `beta` aleatório.
  - **Mutação gaussiana**: aplica ruído gaussiano `N(0,1) * 0.1` a cada gene.
- Ao final, retorna o melhor indivíduo encontrado e contabiliza o **total de avaliações da função (NFE)**.

## Arquivos

### `src/algoritmo.py`
Contém a função principal do AG:

- `algoritmo_genetico(funcao, dimensao=3, limite=5, geracoes=100, tamanho_pop=50)`
  - Retorna: `(melhor_cromossomo, melhor_fitness, total_nfe)`

### `src/funcoes.py`
Funções objetivo disponíveis:

- `camel_back_3d(vetor)`  
  Função Camel Back (na prática, esta implementação usa **2 variáveis**: `x` e `y`).

- `alpine(vetor)`  
  Função Alpine (soma para todas as dimensões do vetor).

### `src/main.py`
Interface via terminal:
- Menu para escolher a função (Camel Back 3D ou Alpine)
- Coleta de parâmetros (execuções, dimensão, limite, gerações, tamanho da população)
- Imprime:
  - **NFE médio**
  - **Taxa de sucesso** (conta sucesso quando `abs(melhor_valor) < 0.01`)

## Como executar

### Requisitos
- Python 3.8+ (recomendado)

### Rodando o programa
Na raiz do projeto:

```bash
python src/main.py
```

Siga o menu no terminal e informe os parâmetros solicitados.

## Parâmetros (o que significam)

- **execuções**: quantas vezes o AG roda do zero (para estimar taxa de sucesso e NFE médio).
- **dimensão**: número de variáveis do problema (tamanho do vetor).
- **limite**: valores iniciais (e faixa esperada) em `[-limite, limite]`.
- **gerações**: quantidade de iterações evolutivas.
- **tamanho da população**: número de indivíduos em cada geração.

## Saída esperada (exemplo)

O programa exibirá algo como:

- Função escolhida
- NFE médio
- Taxa de sucesso (ex.: `7/10`)

## Observações importantes

- A função `camel_back_3d(vetor)` usa apenas **dois valores** (`x` e `y`).  
  Portanto, ao escolhê-la, use **dimensão = 2** para evitar erro de desempacotamento (`x, y = vetor`).
