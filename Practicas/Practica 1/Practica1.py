import numpy as np
import sys


class GaussJordan:
    def llenarmatriz(self, var, opc):
        if int(opc) == 1:
            cols = int(var) + 1
        if int(opc) == 2:
            cols = 2 * int(var)
        if int(opc) == 3:
            cols = var

        m = np.zeros((int(var), int(cols)))

        for i in range(int(var)):
            if int(opc) == 1:
                for j in range(cols):
                    m[i][j] = float(input('M[' + str(i) + '][' + str(j) + ']= '))
            if int(opc) == 2:
                for j in range(int(var)):
                    m[i][j] = float(input('M[' + str(i) + '][' + str(j) + ']='))
                    m[i][i + int(var)] = 1
            if int(opc) == 3:
                for j in range(int(var)):
                    m[i][j] = float(input('M[' + str(i) + '][' + str(j) + ']= '))
        return m

    def setmatriz(self, var, opc):
        M = self.llenarmatriz(var, opc)

        return M

    def pivoteo(self, var, col, M):
        temp = np.copy(M)

        ind = []
        for i in range(int(var)):
            if M[i][i] == 0:
                for j in range(int(var)):
                    if M[j][i] != 0:
                        ind.append(int(j))
                        break
            else:
                ind.append(int(i))

        for i in range(int(var)):
            temp[i] = M[ind[i]]

        return temp

    def checardeterminante(self, var, M):
        temp = np.zeros((int(var), int(var)))

        for i in range(int(var)):
            for j in range(int(var)):
                temp[i][j] = M[i][j]

        det = np.linalg.det(temp)
        return det

    def escalonada(self, var, col, M):
        # Eliminacion por GJ
        for i in range(int(var)):
            if M[i][i] == 0.0:
                print('División entre 0, no es posible seguir')
                sys.exit()

            for j in range(int(var)):
                if i != j:
                    cociente = M[j][i] / M[i][i]
                    for k in range(int(col)):
                        M[j][k] = M[j][k] - cociente * M[i][k]

        return M

    def escalonadareducida(self, var, col, M):
        for i in range(int(var)):
            div = M[i][i]
            for j in range(int(col)):
                M[i][j] = M[i][j] / div
        return M

    def respuesta(self, var, M, opc):
        if int(opc) == 1:
            x = np.zeros(int(var))
            for i in range(int(var)):
                x[i] = np.round((M[i][int(var)]), 6)

            print('\nLas soluciones a las incógnitas son: ')
            for i in range(int(var)):
                print("x[", i, "]= ", x[i])
            sys.exit()

        if int(opc) == 2:
            Inv = np.zeros((int(var), int(var)))
            for i in range(int(var)):
                for j in range(int(var)):
                    Inv[i][j] = M[i][j + int(var)]

            print("Matriz Inversa:\n", Inv)
            sys.exit()

        if int(opc) == 3:
            Inversa = np.zeros((int(var), int(var)))
            for i in range(int(var)):
                for j in range(int(var)):
                    Inversa[i][j] = M[i][j + int(var)]
            return Inversa


class main:
    print("¿Qué desea hacer?\n"
          "1. Encontrar Incógnitas por GJ\n"
          "2. Buscar la Matriz Inversa por GJ\n"
          "3. Encontrar la Matriz X en una ecuación lineal de tipo:\n"
          "   AX= kA+ lB")
    opciones = input("Ingrese el número de la opción a escoger: ")

    if int(opciones) == 1:
        variables = input("Ingrese el número de incógnitas:\n n=")
        columnas = int(variables) + 1
        objGJ = GaussJordan()
        Mat = objGJ.setmatriz(variables, opciones)
        print("Matriz Inicial:\n", Mat)
        det = objGJ.checardeterminante(variables, Mat)
        if float(det) == 0:
            print("¡Determinante es igual a 0!\n No hay Inversa/Solución.")
            sys.exit()
        Mat = objGJ.pivoteo(variables, columnas, Mat)
        Mat = objGJ.escalonada(variables, columnas, Mat)
        Mat = objGJ.escalonadareducida(variables, columnas, Mat)
        objGJ.respuesta(variables, Mat, opciones)

    if int(opciones) == 2:
        variables = input("Ingrese el tamaño de su Matriz nxn: ")
        columnas = 2 * int(variables)
        objGJ = GaussJordan()
        Mat = objGJ.setmatriz(variables, opciones)
        print("Matriz Inicial:\n", Mat)
        det = objGJ.checardeterminante(variables, Mat)
        if float(det) == 0:
            print("¡Determinante es igual a 0!\n No hay Inversa/Solución.")
            sys.exit()
        Mat = objGJ.pivoteo(variables, columnas, Mat)
        Mat = objGJ.escalonada(variables, columnas, Mat)
        Mat = objGJ.escalonadareducida(variables, columnas, Mat)
        objGJ.respuesta(variables, Mat, opciones)

    if int(opciones) == 3:
        variables = int(input("Ingrese el tamaño de sus Matrices nxn: "))
        columnas = variables
        colinv = 2 * variables
        objGJ = GaussJordan()
        print("Llene su matriz A:")
        A = objGJ.setmatriz(variables, opciones)
        print("Llene su matriz B:")
        B = objGJ.setmatriz(variables, opciones)
        k = input("Ingrese el valor de k:")
        l = input("Ingrese el valor de l:")
        a=float(k)*A
        b=float(l)*B
        C=a+b
        det = objGJ.checardeterminante(variables, A)
        if float(det) == 0:
            print("¡Determinante es igual a 0!\n No hay Inversa/Solución.")
            sys.exit()

        Inv = np.zeros((int(variables), int(colinv)))
        for i in range(int(variables)):
            for j in range(int(variables)):
                Inv[i][j] = A[i][j]
                Inv[i][i + int(variables)] = 1

        det = objGJ.checardeterminante(variables, Inv)
        if float(det) == 0:
            print("¡Determinante es igual a 0!\n No hay Inversa/Solución.")
            sys.exit()
        Inv = objGJ.pivoteo(variables, colinv, Inv)
        Inv = objGJ.escalonada(variables, colinv, Inv)
        Inv = objGJ.escalonadareducida(variables, colinv, Inv)
        Inv = objGJ.respuesta(variables, Inv, opciones)

        X = np.matmul(Inv, C)
        print("El Valor de la Matriz X en una ecuación de tipo AX= kA+ lB es:\n", X)


if __name__ == "__main__":
    main()
