import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

#AJUSTES DE SIMULACIÓN ##########################################################

T_in=-3.     #inicio de la simulación
T_fin=6.    #final de la simulación
Resol=10000  #número de puntos computados

#INTRODUCE AQUI TU FUNCION Y VARIABLES RELACIONADAS #############################

P = 3.    #Periodo de la función
cte = 100  #Es el factor P/Δt del ejercicio propuesto
d = P/cte
f = lambda t: np.exp(-((t-3*P/2)/d)**2)+np.exp(-((t-(P/2))/d)**2)+np.exp(-((t+P/2)/d)**2)

#TERMINOS DE LA SERIE DE FOURIER A TENER EN CUENTA ##############################

minN = 5  #términos consideerados en la primera aproximación gráfica
maxN = 30    #términos considerados en la última aproximación gráfica
paso = 5  # entre dibujado y dibujado, cuantos términos deben añadirse

#DISCRETIZACIÓN Y DEFINICIÓN DE SUBALGORITMOS####################################

t_computada = np.linspace(T_in, T_fin, Resol)
imagen_t = f(t_computada) 

def CoeficientesFourier(func, N):
    Coefs = []
    for n in range(N+1):
        an = (2./P) * spi.quad(lambda t: func(t) * np.cos(2 * np.pi * n * t / P), 0, P)[0]
        bn = (2./P) * spi.quad(lambda t: func(t) * np.sin(2 * np.pi * n * t / P), 0, P)[0]
        Coefs.append((an, bn))
    return np.array(Coefs)


def ConstruccionSerieFourier(t, AB):
    serie = 0.
    A = AB[:,0]
    B = AB[:,1]
    for n in range(0, len(AB)):
        if n > 0:
            serie +=  A[n] * np.cos(2. * np.pi * n * t / P) + B[n] * np.sin(2. * np.pi * n * t / P)
        else:
            serie +=  A[0]/2.
    return serie

#AJUSTES DE DIBUJADO ############################################################

COLs = 2
FILs = 3

fig, axs = plt.subplots(FILs, COLs)
fig.tight_layout(rect=[0, -0.1, 1, 1], pad=3.0)
fig.suptitle('Pulso gaussiano con P = ' + str(P) + '  , P/Δt = ' + str(cte))
pos = 0

#AJUSTES DE TERMINO DE SERIE DEFOURIER SUFICIENTE ###############################

insuficientes = True
epsilon = 0.005        #Precisión para considerar una aproximación válida
integral_f = 0
for i in range(0,Resol):
    integral_f = integral_f + imagen_t[i]


#################################################################################


for N in range(minN, maxN + 1,paso):
    
    AB = CoeficientesFourier(f, N)
    f_fourier = ConstruccionSerieFourier(t_computada, AB)
    
    if(insuficientes):
        integral_f_fourier = 0
        for i in range(0,Resol):
            integral_f_fourier = integral_f_fourier + f_fourier[i]
        delta = np.abs(integral_f_fourier - integral_f)
        if delta < epsilon:
            print("numero de terminos suficientes para el desarrollo en serie: " + str(N))
            insuficientes = False

    
    
    pos = pos + 1
    fila = (pos-1) // COLs
    columna = (pos-1) % COLs
    axs[fila, columna].set_title('caso N=' + str(N))
    axs[fila, columna].scatter(t_computada, imagen_t, color='blue', s=1, marker='.')
    axs[fila, columna].scatter(t_computada, f_fourier, color='red', s=2, marker='.')

if insuficientes:
    print("residuo con los coeficientes utilizados: " + str(delta))
plt.show()


                                                  
                            ########              
                          ######  ####            
                          ######  ############    
                          ##################      
                            ########              
                            ######                
                            ######                
                            ######                
                            ########              
                          ############            
                        ##############            
                      ##################          
          ##############################                
        ################################          
        ################################          
          ############################            
                ####################              
                    ####                          
                    ########                     
                      #####LRZ