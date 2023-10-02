def fib(posicion_en_serie):
    if posicion_en_serie <= 1:
        return posicion_en_serie
    return fib(posicion_en_serie - 1) + fib(posicion_en_serie - 2)

def fibonacci_dinamico(n, memo = {}):
    """Mas rápido, pero ocupa más espacio"""
    if n <= 1:
        return n
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado
        return resultado

if __name__ == '__main__':
    print(fibonacci_dinamico(6))
