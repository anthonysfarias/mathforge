import math
from rich.console import Console
from rich.prompt import Prompt

# Criar um objeto Console para usar com o Rich
console = Console()

# Função para calcular a derivada de uma função f(x) para um ponto x
def derivada(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# Função para calcular a integral de uma função f(x) usando o método da soma de Riemann
def integral(f, a, b, n=10000):
    h = (b - a) / n
    soma = 0
    for i in range(n):
        soma += f(a + i * h) * h  # Método dos retângulos à esquerda
    return soma

# Função para resolver uma equação quadrática ax^2 + bx + c = 0
def resolver_equacao_quadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "Sem solução real"
    elif discriminante == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (x1, x2)

# Função para calcular a raiz quadrada
def raiz_quadrada(x):
    if x < 0:
        return "Número negativo não tem raiz quadrada real"
    return math.sqrt(x)

# Função para calcular o fatorial de um número
def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Função para calcular e^x (exponencial de x)
def exponencial(x):
    return math.exp(x)

# Função para calcular o logaritmo natural (ln)
def logaritmo(x):
    if x <= 0:
        return "Logaritmo definido apenas para números positivos"
    return math.log(x)

# Funções trigonométricas
def trigonomometrica(opcao, x):
    x_rad = math.radians(x)  # Converte de graus para radianos
    if opcao == "seno":
        return math.sin(x_rad)
    elif opcao == "cosseno":
        return math.cos(x_rad)
    elif opcao == "tangente":
        return math.tan(x_rad)

# Função para calcular a média de uma lista de números
def media(numeros):
    return sum(numeros) / len(numeros)

# Função para calcular o desvio padrão de uma lista de números
def desvio_padrao(numeros):
    media_valor = media(numeros)
    variancia = sum((x - media_valor) ** 2 for x in numeros) / len(numeros)
    return math.sqrt(variancia)

# Funções de conversão de temperatura
def conversao_temperatura(valor, tipo_entrada, tipo_saida):
    if tipo_entrada == "Celsius":
        if tipo_saida == "Fahrenheit":
            return (valor * 9/5) + 32
        elif tipo_saida == "Kelvin":
            return valor + 273.15
    elif tipo_entrada == "Fahrenheit":
        if tipo_saida == "Celsius":
            return (valor - 32) * 5/9
        elif tipo_saida == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
    elif tipo_entrada == "Kelvin":
        if tipo_saida == "Celsius":
            return valor - 273.15
        elif tipo_saida == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32
    return "Conversão inválida"

# Função para calcular a potência de um número
def potencia(base, expoente):
    return base ** expoente

# Função para somar duas matrizes 2x2
def soma_matrizes(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(2)] for i in range(2)]

# Função para calcular o determinante de uma matriz 2x2
def determinante_matriz_2x2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def obter_matriz_2x2():
    while True:
        try:
            linha1 = list(map(int, input("Digite os elementos da linha 1 da matriz 2x2, separados por espaço: ").split()))
            if len(linha1) != 2:
                raise ValueError("Cada linha deve conter exatamente 2 elementos.. Tente novamente! Exemplo: 1 2")
            linha2 = list(map(int, input("Digite os elementos da linha 2 da matriz 2x2, separados por espaço: ").split()))
            if len(linha2) != 2:
                raise ValueError("Cada linha deve conter exatamente 2 elementos.. Tente novamente! Exemplo: 1 2")
            return [linha1, linha2]
        except ValueError as e:
            print(f"Erro: {e}")


# Função principal
def main():
    # Título estilizado com o Rich
    console.print("[bold green]Calculadora Matemática Complexa[/bold green]", style="bold underline")

    # Menu com cores e fontes diferenciadas
    console.print("\n[bold yellow]Escolha uma operação:[/bold yellow]")
    console.print("[cyan]1:[/cyan] Derivada")
    console.print("[cyan]2:[/cyan] Integral")
    console.print("[cyan]3:[/cyan] Resolver Equação Quadrática")
    console.print("[cyan]4:[/cyan] Raiz Quadrada")
    console.print("[cyan]5:[/cyan] Fatorial")
    console.print("[cyan]6:[/cyan] Exponencial (e^x)")
    console.print("[cyan]7:[/cyan] Logaritmo Natural (ln)")
    console.print("[cyan]8:[/cyan] Trigonometria (Seno, Cosseno, Tangente)")
    console.print("[cyan]9:[/cyan] Média Aritmética")
    console.print("[cyan]10:[/cyan] Desvio Padrão")
    console.print("[cyan]11:[/cyan] Conversão de Temperatura")
    console.print("[cyan]12:[/cyan] Potência")
    console.print("[cyan]13:[/cyan] Soma de Matrizes")
    console.print("[cyan]14:[/cyan] Determinante de Matriz 2x2")

    # Entrada do usuário
    opcao = Prompt.ask("Digite o número da opção desejada", choices=[str(i) for i in range(1, 15)], default="1")

    if opcao == "1":
        x = float(Prompt.ask("Digite o valor de x para a derivada"))
        resultado = derivada(lambda x: x**2 + 3*x - 5, x)
        console.print(f"[bold magenta]Derivada de f(x) = x^2 + 3x - 5 no ponto x = {x}: {resultado}[/bold magenta]")

    elif opcao == "2":
        a = float(Prompt.ask("Digite o valor de a (início do intervalo)"))
        b = float(Prompt.ask("Digite o valor de b (fim do intervalo)"))
        resultado = integral(lambda x: x**2 + 3*x - 5, a, b)
        console.print(f"[bold blue]Integral de f(x) = x^2 + 3x - 5 no intervalo [{a}, {b}]: {resultado}[/bold blue]")

    elif opcao == "3":
        a = float(Prompt.ask("Digite o valor de a"))
        b = float(Prompt.ask("Digite o valor de b"))
        c = float(Prompt.ask("Digite o valor de c"))
        resultado = resolver_equacao_quadratica(a, b, c)
        console.print(f"[bold red]Soluções da equação {a}x^2 + {b}x + {c} = 0: {resultado}[/bold red]")

    elif opcao == "4":
        x = float(Prompt.ask("Digite o valor para calcular a raiz quadrada"))
        resultado = raiz_quadrada(x)
        console.print(f"[bold cyan]Raiz quadrada de {x}: {resultado}[/bold cyan]")

    elif opcao == "5":
        n = int(Prompt.ask("Digite o número para calcular o fatorial"))
        resultado = fatorial(n)
        console.print(f"[bold magenta]Fatorial de {n}: {resultado}[/bold magenta]")

    elif opcao == "6":
        x = float(Prompt.ask("Digite o valor de x para calcular e^x"))
        resultado = exponencial(x)
        console.print(f"[bold green]e^{x} = {resultado}[/bold green]")

    elif opcao == "7":
        x = float(Prompt.ask("Digite o valor de x para calcular o logaritmo"))
        resultado = logaritmo(x)
        console.print(f"[bold blue]Logaritmo natural de {x}: {resultado}[/bold blue]")

    elif opcao == "8":
        trig = Prompt.ask("Escolha a operação trigonométrica: seno, cosseno, tangente", choices=["seno", "cosseno", "tangente"])
        x = float(Prompt.ask("Digite o valor de x (em graus)"))
        resultado = trigonomometrica(trig, x)
        console.print(f"[bold yellow]{trig.capitalize()} de {x}°: {resultado}[/bold yellow]")

    elif opcao == "9":
        numeros = list(map(float, Prompt.ask("Digite os números para calcular a média, separados por espaço").split()))
        resultado = media(numeros)
        console.print(f"[bold cyan]Média dos números: {resultado}[/bold cyan]")

    elif opcao == "10":
        numeros = list(map(float, Prompt.ask("Digite os números para calcular o desvio padrão, separados por espaço").split()))
        resultado = desvio_padrao(numeros)
        console.print(f"[bold magenta]Desvio padrão dos números: {resultado}[/bold magenta]")

    elif opcao == "11":
        valor = float(Prompt.ask("Digite o valor da temperatura"))
        tipo_entrada = Prompt.ask("Digite o tipo de temperatura (Celsius, Fahrenheit, Kelvin)")
        tipo_saida = Prompt.ask("Digite o tipo de temperatura de saída (Celsius, Fahrenheit, Kelvin)")
        resultado = conversao_temperatura(valor, tipo_entrada, tipo_saida)
        console.print(f"[bold blue]Temperatura convertida: {resultado}[/bold blue]")

    elif opcao == "12":
        base = float(Prompt.ask("Digite a base"))
        expoente = float(Prompt.ask("Digite o expoente"))
        resultado = potencia(base, expoente)
        console.print(f"[bold green]{base}^{expoente} = {resultado}[/bold green]")

    elif opcao == "13":
        m1 = obter_matriz_2x2()
        m2 = obter_matriz_2x2()
        resultado = soma_matrizes(m1, m2)
        console.print(f"[bold yellow]Soma das matrizes:\n{resultado}[/bold yellow]")

    elif opcao == "14":
        m = obter_matriz_2x2()
        resultado = determinante_matriz_2x2(m)
        console.print(f"[bold cyan]Determinante da matriz: {resultado}[/bold cyan]")

if __name__ == "__main__":
    main()
