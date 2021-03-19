import time
from sympy.abc import x
import sympy as sp


class NumericalMethods:
    def biseccion(self, f, a, b, maxit):
        fa = f.subs(x, a)
        fb = f.subs(x, b)
        if fa * fb >= 0:
            print("Error.")
            return None
        a_n = a
        b_n = b
        iter = 0
        while iter < maxit:

            m_n = (a_n + b_n) / 2
            f_m_n = f.subs(x, m_n)
            if f.subs(x, a_n) * f_m_n < 0:
                a_n = a_n
                b_n = m_n
            elif f.subs(x, b_n) * f_m_n < 0:
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                print("Se encontró solución.")
                return m_n
            else:
                print("Error.")
                return None

            iter += 1
        return (a_n + b_n) / 2

    def newton(self,f,x0,tol,maxit):
        xn = x0
        Df=f.diff(x)
        for n in range(0, maxit):
            fxn = f.subs(x,xn)
            if abs(fxn) < tol:
                print("Se encontró solución.")
                root=xn.evalf()
                return root
            Dfxn = Df.subs(x,xn)
            if Dfxn == 0:
                print("Error")
                return None
            xn = xn - fxn / Dfxn
        print("Ya se tardón... Ahí muere")
        return None

    def secante(self, f, a, b, maxit, tol):
        fa = f.subs(x, a)
        fb = f.subs(x, b)
        if fa * fb >= 0:
            print("Error.")
            return None
        a_n = a
        b_n = b
        iter = 0
        while iter < maxit:
            m_n = a_n - f.subs(x, a_n) * (b_n - a_n) / (f.subs(x, b_n) - f.subs(x, a_n))
            f_m_n = f.subs(x, m_n)
            fmn=f_m_n.evalf()
            fam=f.subs(x, a_n) * f_m_n
            fbm=f.subs(x, b_n) * f_m_n
            if float(fam) < 0:
                a_n = a_n
                b_n = m_n
            if float(fbm) < 0:
                a_n = m_n
                b_n = b_n
            elif abs(fmn) < tol:
                print("Se encontró solución.")
                root=m_n.evalf(4)
                return root
            else:
                print("Error")
                return None
            iter += 1

        root= (a_n - f.subs(x, a_n) * (b_n - a_n) / (f(x, b_n) - f(x, a_n))).evalf()
        return root


def main():
    x0 = 7
    maxIter = 1000
    tol = 0.1
    func = 0.4 * sp.sin((sp.pi / 8) * x)
    a = 5
    b = 10

    # Objeto para métodos numéticos
    objNM = NumericalMethods()

    print("____METODO DE LA BISECCION____")
    startbisection = time.time()
    rootbisection = objNM.biseccion(func, a, b, maxIter)
    endbisection = time.time()
    tiempobiseccion = endbisection - startbisection
    print("Raíz:", rootbisection)
    print("Tiempo de ejecución:", tiempobiseccion)

    print("________METODO NEWTONRAPHSON________")
    startnr = time.time()
    rootnr = objNM.newton(func,x0,tol,maxIter)
    endnr = time.time()
    tiemponr = endnr - startnr
    print("Más Cercano a la Raíz:", rootnr)
    print("Tiempo de ejecución:", tiemponr)


    print("________METODO SECANTE________")
    startsec = time.time()
    rootsec = objNM.secante(func, a, b, maxIter, tol)
    endsec = time.time()
    tiemposec = endsec - startsec
    print("Más Cercano a la Raíz:", rootsec)
    print("Tiempo de ejecución:", tiemposec)


    print("Programa Finalizado con Éxito")


if __name__ == "__main__":
    main()
