import pytest
from unittest.mock import patch
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import (
    derivada,
    integral,
    resolver_equacao_quadratica,
    raiz_quadrada,
    fatorial,
    exponencial,
    logaritmo,
    trigonomometrica,
    media,
    desvio_padrao,
    conversao_temperatura,
    potencia,
    soma_matrizes,
    determinante_matriz_2x2
)

# Teste para a função derivada
def test_derivada():
    resultado = derivada(lambda x: x**2 + 3*x - 5, 2)
    assert math.isclose(resultado, 7, abs_tol=1e-2)

# Teste para a função integral
def test_integral():
    resultado = integral(lambda x: x**2 + 3*x - 5, 0, 1)
    print(f"Resultado calculado: {resultado}")  # Imprimir o valor calculado
    assert math.isclose(resultado, -3.166, abs_tol=1e-2)

# Teste para resolver equação quadrática
@pytest.mark.parametrize("a, b, c, resultado_esperado", [
    (1, -3, 2, (2, 1)),
    (1, 2, 1, -1),
    (1, 2, 5, "Sem solução real"),
])
def test_resolver_equacao_quadratica(a, b, c, resultado_esperado):
    resultado = resolver_equacao_quadratica(a, b, c)
    if isinstance(resultado, tuple):
        assert all(math.isclose(r, e, abs_tol=1e-2) for r, e in zip(resultado, resultado_esperado))
    else:
        assert resultado == resultado_esperado

# Teste para raiz quadrada
@pytest.mark.parametrize("x, resultado_esperado", [
    (4, 2),
    (9, 3),
    (16, 4),
    (-1, "Número negativo não tem raiz quadrada real"),
])
def test_raiz_quadrada(x, resultado_esperado):
    resultado = raiz_quadrada(x)
    assert resultado == resultado_esperado

# Teste para fatorial
def test_fatorial():
    assert fatorial(5) == 120
    assert fatorial(0) == 1
    assert fatorial(-1) == "Fatorial não definido para números negativos"

# Teste para exponencial
def test_exponencial():
    assert math.isclose(exponencial(1), math.e, abs_tol=1e-2)
    assert math.isclose(exponencial(0), 1, abs_tol=1e-2)

# Teste para logaritmo
@pytest.mark.parametrize("x, resultado_esperado", [
    (math.e, 1),
    (1, 0),
    (2, 0.693),
    (-1, "Logaritmo definido apenas para números positivos"),
])
def test_logaritmo(x, resultado_esperado):
    resultado = logaritmo(x)
    assert math.isclose(resultado, resultado_esperado, abs_tol=1e-2) if isinstance(resultado_esperado, float) else resultado == resultado_esperado

# Teste para funções trigonométricas
@pytest.mark.parametrize("opcao, x, resultado_esperado", [
    ("seno", 30, 0.5),
    ("cosseno", 60, 0.5),
    ("tangente", 45, 1),
])
def test_trigonomometrica(opcao, x, resultado_esperado):
    resultado = trigonomometrica(opcao, x)
    assert math.isclose(resultado, resultado_esperado, abs_tol=1e-2)

# Teste para média
def test_media():
    assert math.isclose(media([1, 2, 3, 4, 5]), 3, abs_tol=1e-2)

# Teste para desvio padrão
def test_desvio_padrao():
    assert math.isclose(desvio_padrao([1, 2, 3, 4, 5]), 1.414, abs_tol=1e-2)

# Teste para conversão de temperatura
@pytest.mark.parametrize("valor, tipo_entrada, tipo_saida, resultado_esperado", [
    (0, "Celsius", "Fahrenheit", 32),
    (32, "Fahrenheit", "Celsius", 0),
    (273.15, "Kelvin", "Celsius", 0),
    (100, "Celsius", "Kelvin", 373.15),
])
def test_conversao_temperatura(valor, tipo_entrada, tipo_saida, resultado_esperado):
    resultado = conversao_temperatura(valor, tipo_entrada, tipo_saida)
    assert math.isclose(resultado, resultado_esperado, abs_tol=1e-2)

# Teste para potência
def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1

# Teste para soma de matrizes
def test_soma_matrizes():
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    resultado = soma_matrizes(m1, m2)
    assert resultado == [[6, 8], [10, 12]]

# Teste para determinante de matriz 2x2
def test_determinante_matriz_2x2():
    m1 = [[1, 2], [3, 4]]
    assert determinante_matriz_2x2(m1) == -2
