
# Calculadora Matemática Complexa

## Descrição

Este é um projeto de uma calculadora matemática complexa que oferece uma variedade de funções para cálculos matemáticos avançados. Utilizando a biblioteca `rich` para uma interface de terminal interativa, o aplicativo oferece operações como derivadas, integrais, resoluções de equações quadráticas, funções trigonométricas, entre outros.

## Funcionalidades

A calculadora inclui as seguintes operações:

- **Derivada**: Cálculo da derivada de uma função no ponto fornecido.
- **Integral**: Cálculo da integral definida de uma função no intervalo fornecido.
- **Equação Quadrática**: Resolução de equações quadráticas \( ax^2 + bx + c = 0 \).
- **Raiz Quadrada**: Cálculo da raiz quadrada de um número.
- **Fatorial**: Cálculo do fatorial de um número.
- **Exponencial**: Cálculo de \( e^x \).
- **Logaritmo Natural (ln)**: Cálculo do logaritmo natural de um número.
- **Funções Trigonométricas**: Seno, Cosseno e Tangente de um ângulo (em graus).
- **Média Aritmética**: Cálculo da média de uma lista de números.
- **Desvio Padrão**: Cálculo do desvio padrão de uma lista de números.
- **Conversão de Temperatura**: Conversão entre Celsius, Fahrenheit e Kelvin.
- **Potência**: Cálculo da potência de um número (base^expoente).
- **Soma de Matrizes 2x2**: Soma de duas matrizes 2x2.
- **Determinante de Matriz 2x2**: Cálculo do determinante de uma matriz 2x2.

## Requisitos

Este projeto utiliza a biblioteca `rich`, que pode ser instalada via `pip`:

```bash
pip install rich
```

Além disso, o código utiliza funções matemáticas da biblioteca `math`, que é uma biblioteca padrão do Python.

## Como Usar

1. Clone o repositório ou baixe o arquivo `app.py`.
2. Execute o script em um terminal com o comando:
   ```bash
   python app.py
   ```
3. Escolha a operação desejada a partir do menu interativo.
4. Digite os valores solicitados para cada operação e veja o resultado.

## Testes

O código pode ser testado manualmente utilizando o terminal interativo. Para cada operação, o usuário deve fornecer os valores de entrada conforme solicitado. Não há testes automatizados no momento, mas é possível adicionar testes unitários utilizando frameworks como `unittest` ou `pytest` para garantir a funcionalidade das funções matemáticas.

### Exemplo de Teste

```python
# Teste de derivada
def test_derivada():
    f = lambda x: x**2 + 3*x - 5
    assert derivada(f, 2) == 7  # Derivada de f(x) = x^2 + 3x - 5 no ponto x = 2
```

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
