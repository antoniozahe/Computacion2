import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import x


class Depuracion():
    def depuracion(self,df,paiscode, yr0, yr1,ejex,ejey):
        dffilter=(df[(df.Code == paiscode)])

        df_filt=(dffilter[(dffilter.Year >= yr0) & (dffilter.Year <= yr1)])

        year=df_filt['Year'].tolist()
        undernourish=df_filt['Suite of Food Security Indicators - Prevalence of undernourishment (percent) (3-year average) - 210041 - Value - 6121 - %'].tolist()

        return year,undernourish

class Interpolation():
    def linearInterpolation(self, X, Y):
        # b0 = intecepto, b1 = pendiente
        b0 = Y[0]
        b1 = (Y[1] - Y[0]) / (abs(X[1]) - abs(X[0]))
        #print("b1", b1)
        return b0 + b1*(x - X[0])
    
    def tmpLinearInterpolation(self, X, Y):
        # b0 = intecepto, b1 = pendiente
        b0 = Y[0]
        b1 = (Y[1] - Y[0]) / (abs(X[1]) - abs(X[0]))

        return b0, b1

    def cuadraticInterpolation(self, X, Y):
        if (len(X) == 3 and len(Y) == 3):   
            b0, b1 = self.tmpLinearInterpolation(X, Y)
            b2 = (((Y[2] - Y[1]) / (X[2] - X[1])) - b1 ) / (X[2]-X[0])
            return b0 + b1*(x-X[0]) + b2*(x -X[0]) *(x-X[1])

    def DividedDiff(self,X,Y):
        rows=len(X)+1
        cols=len(X)+1
        table = [[0 for i in range(cols)] for j in range(rows)]
        for i in range (0,len(X)):
            table[0][i+1]=(i)
            table[i+1][0]=X[i]
            table[i+1][1]=Y[i]
            
        table[0][0]="x"
        table[0][1]="f(x)"

        for i in range (2,rows):
            for j in range (1,cols):
                
                if i+j<len(X)+2:
                    num=table[j+1][i-1]-table[j][i-1]
                    den=table[j+(i-1)][0]-table[j][0]
                    table[j][i]=num/den


        b = [0 for i in range(len(X))]

        for i in range(0,len(X)):
            b[i]=table[1][i+1]

        poly=list()
        poly.append(1)
        for i in range (0,len(X)):
            poly.append(x-X[i])
        
        for i in range (1,len(X)):
            poly[i]=poly[i-1]*poly[i]
       
        func=list()
        for i in range(len(X)):
            tmp=b[i]*poly[i]
            func.append(tmp)
        
        return(sum(func))


class Graph():
    # Genera un gráfico de dispersión
    def plotScatter(self, X, Y, lab):
        plt.scatter(X, Y, label = lab)
        plt.title("Inseguridad Alimenticia vs Tiempo")
        plt.xlabel("AÑO")
        plt.ylabel("Inseguridad Alimenticia")
    # Genera un gráfico de línea

    def plotLine(self, func,a ,b, leg,color):
        X = np.linspace(a, b, 100)
        Y = np.zeros_like(X)

        for i in range(len(X)):
            Y[i] = func.subs(x, X[i])
        
        plt.plot(X,Y,  c = color, ls='--')
        plt.legend(loc='best')
    # Despliega el gráfico (útil para ) 
    def displayPlot(self):
        plt.show()

def main():
    #----DEPURACION----#
    df = pd.read_csv("https://raw.githubusercontent.com/antoniozahe/Computacion2/main/Practicas/Practica4/prevalence-of-undernourishment.csv")
    pais='MEX'
    year0=2004
    year1=2015
    ejex='Year'
    ejey='Suite of Food Security Indicators - Prevalence of undernourishment (percent) (3-year average) - 210041 - Value - 6121 - %'
    
    objDF=Depuracion()
    X,Y=objDF.depuracion(df,pais, year0, year1,ejex,ejey)

    #----INTERPOLACIÓN LINEAL----#
    objInt = Interpolation()

    funcList = list()

    for i in range(len(X) - 1):
        ##print(X[i:i+2])
        funcList.append(objInt.linearInterpolation(X[i:i+2], Y[i:i+2]))

    lastFunc = funcList[-3]

    #----INTERPOLACIÓN CUADRATICA----#
    funcquad = list()  
    for i in range(len(X) - 2):
        #print(X[i:i+2])
        funcquad.append(objInt.cuadraticInterpolation(X[i:i+3], Y[i:i+3]))
 
    lastQuad=funcquad[-3]
    #----INTERPOLACION DIFERENCIASDIVIDIDAD(NEWTON)----#
    newtoninter=objInt.DividedDiff(X,Y)

    #----Graficos----#
    objG=Graph()
    objG.plotScatter(X,Y,"Valores Iniciales")
    

    objG.plotLine(newtoninter, year0, year1, "Interpolación Newton",'r')
    for i in range(len(X)-1):
        objG.plotLine(funcList[i], X[i], X[i+1], "Interpolación lineal",'g')

    for i in range(len(X)-2):
        objG.plotLine(funcquad[i], X[i], X[i+2], "Interpolación cuadrática",'m')
        
    x1 =2012.5
    ylin = lastFunc.subs(x, x1)
    yquad=lastQuad.subs(x,x1)
    ynewt=  newtoninter.subs(x,x1)

    print("\n_____APROXIMACIONES_____")
    print("Aproximación lineal de x=",x1,":", ylin)
    print("Aproximación cuadratica de x=",x1,":", yquad)
    print("Aproximación Newton de x=",x1,":", ynewt)
    
    error1=abs((yquad-ylin)/yquad)*100
    error2=abs((ynewt-yquad)/ynewt)*100
    print("\n_____ERRORES_____")
    print("Error entre Lineal y Cuadratica en x=", x1,": ", round(error1,3),"%")
    print("Error entre Cuadratica y Diferencias Divididas en x=", x1,": ", round(error2,3),"%")
    
    

if __name__ == "__main__":
    main()
