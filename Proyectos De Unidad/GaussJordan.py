import numpy as np
import sys


class GaussJordan:
    def llenarmatriz(self, var, col):

        m = np.zeros((int(var), int(col)))
        for i in range(int(var)):
            for j in range(col):
                m[i][j] = float(input('M[' + str(i) + '][' + str(j) + ']= '))
        """
        m = np.array([[2, 0, 0, 0, -1, -8],
                      [1, 2, -3, 0, 0, 31],
                      [1, 0, 0, 3, 0, 36],
                      [0, 0, 3, 3, 0, 27],
                      [0, 0, 0, 0, 1, 30]])
        """
        return m

    def setmatriz(self, var, col):
        M = self.llenarmatriz(var, col)

        return M

    def pivoteo(self, var, M):
        temp = np.zeros((int(var), int(var) + 1))
        ind = []
        sum = 0

        for i in range(int(var)):
            ind.append(i)
            sum = sum + i
        print("Ind Inicial:", ind)
        for i in range(int(var)):
            if M[i][i] == 0:
                for j in range(int(var)):
                    if ind.count(j) == 1:
                        if M[j][i] != 0:
                            ind[i] = i + 1
                            ind[i + 1] = i
        print("Ind Final:", ind)
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

    def respuesta(self, var, M):
        x = np.zeros(int(var))
        for i in range(int(var)):
            x[i] = np.round((M[i][int(var)]), 6)

        print('\nLas soluciones a las incógnitas son: ')
        for i in range(int(var)):
            print("x[", i, "]= ", x[i])
        sys.exit()


class main:
    print("__RESOLUCION DE INCOGNITAS POR GJ__")
    variables = input("Ingrese el número de incógnitas:\n n=")
    columnas = int(variables) + 1
    objGJ = GaussJordan()
    Mat = objGJ.setmatriz(variables, columnas)
    print("Matriz Inicial:\n", Mat)
    det = objGJ.checardeterminante(variables, Mat)
    if float(det) == 0:
        print("¡Determinante es igual a 0!\n No hay Inversa/Solución.")
        sys.exit()
    Mat = objGJ.pivoteo(variables, Mat)
    Mat = objGJ.escalonada(variables, columnas, Mat)
    Mat = objGJ.escalonadareducida(variables, columnas, Mat)
    print("Escalonada Reducida\n", Mat)
    objGJ.respuesta(variables, Mat)


if __name__ == "__main__":
    main()
