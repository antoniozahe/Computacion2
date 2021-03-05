import numpy as np
from sympy.abc import x, y
import time


class NumericalMethods:

    def bisectionMethod(self, a, b, tol, maxIter, func):

        if (func.subs(x, a) * func.subs(x, b)) < 0:
            print("Existe un cambio de signo")
        elif (func.subs(x, a) * func.subs(x, b)) > 0:
            print("Intervalo incorrecto:")
            exit(0)

        error = np.inf

        while error > tol:
            c = (a + b) / 2
            fa = func.subs(x, a)
            fc = func.subs(x, c)
            if fc == 0:
                break
            if (fc * fa) < 0:
                b = c
            else:
                a = c

        return c

    def incrementalSearch(self, a, b, func):
        spacing = abs(b - a) * 1000  # homologamos la distancia entre valores a evaluar
        X = np.linspace(a, b, spacing)
        Y = np.zeros_like(X)
        cercanoacerox = []
        cercanoaceroy = []
        cero = 0
        for i in range(len(X)):
            Y[i] = abs(func.subs(x, X[i]))
            if abs(Y[i]) < 0.5:
                cercanoacerox.append(X[i])
                cercanoaceroy.append(Y[i])
        ind = cercanoaceroy.index(min(cercanoaceroy))
        raiz = cercanoacerox[ind]
        return raiz


def main():
    x0 = 0
    maxIter = 90000
    tol = 0.0000000000000000001
    func = 2 * x ** 3 - 3 * x - 5
    a = -5
    b = 5

    # Objeto para métodos numéticos
    objNM = NumericalMethods()

    print("____METODO DE LA BISECCION____")
    startbisection = time.time()
    rootbisection = objNM.bisectionMethod(a, b, tol, maxIter, func)
    endbisection = time.time()
    tiempobiseccion = endbisection - startbisection
    print("Raíz:", rootbisection)
    print("Tiempo de ejecución:", tiempobiseccion)

    print("________METODO INGENUO________")
    startnaive = time.time()
    rootnaive = objNM.incrementalSearch(a, b, func)
    endnaive = time.time()
    tiemponaive = endnaive - startnaive
    print("Más Cercano a la Raíz:", rootnaive)
    print("Tiempo de ejecución:", tiemponaive)


if __name__ == "__main__":
    main()
