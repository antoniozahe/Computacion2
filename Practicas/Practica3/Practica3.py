import time
import numpy as np
from sympy.abc import x


class NumericalMethods:

    def newtonraphson(self, tol, maxIter, x0, func):
        df = func.diff(x)
        x1 = x0
        x2 = func.subs(x, x1) / df.subs(x, x1)
        iter = 0

        while (abs(x2) >= tol and iter < maxIter):
            x2 = func.subs(x, x1) / df.subs(x, x1)
            x1 = abs(x1 - x2)
            iter += 1
            if iter == int(maxIter) - 1:
                print("No se encontró raíz")
                return None

        return float(x1)

    def secante(self, func, a, b):
        fa = func.subs(x, a)
        fb = func.subs(x, b)
        iter = 30
        if fa * fb >= 0:
            print("Secant method fails.")
            return None
        a_n = a
        b_n = b
        fa_n = func.subs(x, a_n)
        fb_n = func.subs(x, b_n)

        for n in range(1, iter + 1):
            m_n = a_n - fa_n * (b_n - a_n) / (fb_n - fa_n)
            f_m_n = func.subs(x, m_n)
            if fa_n * f_m_n < 0:
                a_n = a_n
                b_n = m_n
            elif fb_n * f_m_n < 0:
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                print("Found exact solution.")
                return m_n
            else:
                print("Secant method fails.")
                return None
        raiz = a_n - fa_n * (b_n - a_n) / (fb_n - fa_n)
        return float(raiz)
    """
    def brentDekkerMethod(self, a, b, tol, maxIter, func):
        root = np.inf
        error = np.inf
        iter = 0

        if func.subs(x, a) * func.subs(x, b) >= 0:
            print("No existe una raíz en el intervalo proporcionado...")
            exit(0)
        # Validar valores
        if abs(func.subs(x, a)) < (func.subs(x, b)):
            # Cambiar los valores de a por b y viceversa
            a, b = b, a

        c = a
        while (error > tol and iter < maxIter):
            if (func.subs(x, a) != func.subs(x, c)) and (func.subs(x, b) != func.subs(x, c)):
                s = ((a * func.subs(x, b) * func.subs(x, c)) / (
                            ((func.subs(x, a) - func.subs(x, b))) * (func.subs(x, a)) - func.subs(x, c))) +
                (((b * func.subs(x, a) * func.subs(x, c)) / (
                            ((func.subs(x, b) - func.subs(x, a))) * (func.subs(x, b)) - func.subs(x, c)))) +
                (((c * func.subs(x, a) * func.subs(x, b)) / (
                            ((func.subs(x, c) - func.subs(x, a))) * (func.subs(x, c)) - func.subs(x, b))))
            else:
                # Método de la secante
                s = b - (func.subs(x, b)) * ((b - a) / (func.subs(x, b) - func.subs(x, a)))
            elif:
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
            if abs(func.subs(x, a)) < (func.subs(x, b)):
            # Cambiar los valores de a por b y viceversa
                a, b = b, a
"""
    def bisectionMethod(self, a, b, tol, func):

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
    tol = 0.000001
    func = 2 * x ** 3 - 3 * x - 5
    a = -3
    b = 3

    # Objeto para métodos numéticos
    objNM = NumericalMethods()

    print("____METODO DE LA BISECCION____")
    startbisection = time.time()
    rootbisection = objNM.bisectionMethod(a, b, tol, func)
    endbisection = time.time()
    tiempobiseccion = endbisection - startbisection
    print("Raíz:", rootbisection)
    print("Tiempo de ejecución:", tiempobiseccion)

    """
    print("________METODO INGENUO________")
    startnaive = time.time()
    rootnaive = objNM.incrementalSearch(a, b, func)
    endnaive = time.time()
    tiemponaive = endnaive - startnaive
    print("Más Cercano a la Raíz:", rootnaive)
    print("Tiempo de ejecución:", tiemponaive)
    """

    print("________METODO NEWTONRAPHSON________")
    startnr = time.time()
    rootnr = objNM.newtonraphson(tol, maxIter, x0, func)
    endnr = time.time()
    tiemponr = endnr - startnr
    print("Más Cercano a la Raíz:", rootnr)
    print("Tiempo de ejecución:", tiemponr)

    print("________METODO SECANTE________")
    startsec = time.time()
    rootsec = objNM.secante(func, a, b)
    endsec = time.time()
    tiemposec = endsec - startsec
    print("Más Cercano a la Raíz:", rootsec)
    print("Tiempo de ejecución:", tiemposec)

    print("Programa Finalizado con Éxito")


if __name__ == "__main__":
    main()
