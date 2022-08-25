from ast import For
from random import random
from math import log, e
from statistics import pvariance
import threading
import time
import datetime

from flask.app import cli
from Persona import *

numClientesAtendidos=0
clientesAgregados = 0

seed = random()
seed2 = random()
clientesFila = []
clientesAtendidos = []
diferenciaTiemposEspera = []
tiempoClientesAtendidos = []
seguir=True
lambdaNumber = 0.429
value2=0
quantity = 10
tiempoTotal = 0
tiempoLLegada=0
contador=1
i=0

def correr():
    
    global clientesAtendidos 
    clientesAtendidos = []
    
    
    def generar(seed):
        seed = random()
        seed = fixSeed(seed)
        seed = ((-(log(1 - seed, e)))/lambdaNumber)
        seed = fixSeed(seed)
        value = monteCarloTatencion(seed)
        return value

    def generar2(seed):
        seed = random()
        seed = fixSeed(seed)
        seed = ((-(log(1 - seed, e)))/lambdaNumber)
        seed = fixSeed(seed)
        cantidad=monteCarloPersonas(seed)
        return cantidad

    def llegadaPersona():
        
        value2=generar2(seed)
        tiempoAgregar = value2/60
        print("value 2: ",value2)
        for i in range(value2):
            global tiempoLLegada 
            tiempoLLegada += tiempoAgregar
            clientesAgregados = len(clientesFila) + len(clientesAtendidos)
            persona = Persona (clientesAgregados,tiempoLLegada)
            clientesFila.append(persona)
            time.sleep(tiempoAgregar/1000)

    def atencionCliente():
    
        numClientesAtendidos=0
        global seguir 
        while(seguir == True and len(clientesFila)>0):
            global i
            #print("atención cliente")
            numClientesAtendidos += 1
            value = generar(seed2)
            global tiempoTotal
            tiempoTotal = tiempoLLegada + value
            persona =clientesFila.pop(0)
            persona.set_t_salida(tiempoTotal)    
            clientesAtendidos.append(persona)
            #i-=1
            time.sleep(value/1000)


    def diferenciaTiempo():
        for i in range (len(clientesAtendidos)):
            diferencia=0
            t_l=clientesAtendidos[i].t_llegada
            t_s=clientesAtendidos[i].t_salida
            diferencia= t_s - t_l
            diferenciaTiemposEspera.append(diferencia)
            
    def monteCarloTatencion(number):
        value=0
        if(number>= 0 and number<=0.143):
            tiempoClientesAtendidos.append(1)
            value=1
        elif (number>0.143 and number<=0.286):
            tiempoClientesAtendidos.append(2)
            value=2
        elif (number>0.286 and number<=0.429):
            tiempoClientesAtendidos.append(3)
            value=3
        elif (number>0.429 and number<=0.571):
            tiempoClientesAtendidos.append(4) 
            value=4   
        elif (number>0.571 and number<=0.714):
            tiempoClientesAtendidos.append(5)
            value=5
        elif (number>0.714 and number<=0.857):
            tiempoClientesAtendidos.append(6)
            value=6
        elif (number>0.857 and number<=1):
            tiempoClientesAtendidos.append(7) 
            value=7
        return value   

    def monteCarloPersonas(number): 
        if(number>= 0 and number<=0.043):
            value2=53
        elif (number>0.043 and number<=0.087):
            value2=54
        elif (number>0.087 and number<=0.130):
            value2=55
        elif (number>0.130 and number<=0.174):
            value2=56    
        elif (number>0.174 and number<=0.217):
            value2=57
        elif (number>0.217 and number<=0.261):
            value2=58
        elif (number>0.261 and number<=0.304):
            value2=59
        elif (number>0.304 and number<=0.348):
            value2=60
        elif (number>0.348 and number<=0.391):
            value2=61
        elif (number>0.391 and number<=0.435):
            value2=62
        elif (number>0.435 and number<=0.478):
            value2=63                
        elif (number>0.478 and number<=0.522):
            value2=64
        elif (number>0.522 and number<=0.565):
            value2=65
        elif (number>0.565 and number<=0.609):
            value2=66
        elif (number>0.609 and number<=0.652):
            value2=67
        elif (number>0.652 and number<=0.696):
            value2=68
        elif (number>0.696 and number<=0.739):
            value2=69
        elif (number>0.739 and number<=0.783):
            value2=70
        elif (number>0.783 and number<=0.826):
            value2=71
        elif (number>0.826 and number<=0.870):
            value2=72
        elif (number>0.870 and number<=0.913):
            value2=73
        elif (number>0.913 and number<=0.957):
            value2=74
        elif (number>0.957 and number<=1):
            value2=75              
        return value2

    def fixSeed(seed):
        while seed >= 1:
            seed = seed/10
        return seed

    def datos():
        global contador 
        print("\n*************** CORRIDA ",contador," **********************")
        tiempo_final=datetime.datetime.now()
        print("tiempo de simulación: ",tiempo_final.second - tiempo_inicial.second," segundos")
        #print("lista de llegada de clientes: ",clientesFila)
        #print("Clientes atendidos ",clientesAtendidos)
        print("lista tiempo clientes atendidos ",tiempoClientesAtendidos)
        print("\n\n*************** Datos Estadisticos ")
        print("Cantidad clientes atendidos: ",len(tiempoClientesAtendidos))
        #if(numClientesAtendidos != 0):
        print("Promedio clientes atendidos: ",(len(clientesAtendidos)/(len(clientesAtendidos) + len(clientesFila)))*100)
        print("Promedio clientes No atendidos: ",(len(clientesFila)/(len(tiempoClientesAtendidos) + len(clientesFila)))*100)


    tiempo_inicial=datetime.datetime.now()


    thread1 = threading.Thread(name="hilo1",target=llegadaPersona)
    thread2 = threading.Thread(name="hilo2",target=atencionCliente)

    thread3 = threading.Thread(name="hilo3",target=llegadaPersona)
    thread4 = threading.Thread(name="hilo4",target=atencionCliente)

    thread5 = threading.Thread(name="hilo5",target=llegadaPersona)
    thread6 = threading.Thread(name="hilo6",target=atencionCliente)

    thread7 = threading.Thread(name="hilo7",target=llegadaPersona)
    thread8 = threading.Thread(name="hilo8",target=atencionCliente)

    thread9 = threading.Thread(name="hilo9",target=llegadaPersona)
    thread10 = threading.Thread(name="hilo10",target=atencionCliente)

    thread11 = threading.Thread(name="hilo11",target=llegadaPersona)
    thread12 = threading.Thread(name="hilo12",target=atencionCliente)

    thread13 = threading.Thread(name="hilo13",target=llegadaPersona)
    thread14 = threading.Thread(name="hilo14",target=atencionCliente)

    thread15 = threading.Thread(name="hilo15",target=llegadaPersona)
    thread16 = threading.Thread(name="hilo16",target=atencionCliente)

    #CORRIDAS
    thread1.start()
    time.sleep(0.2)
    thread2.start()

    thread1.join()
    seguir=False
    thread2.join()
    datos()

    generatedNumbersA=[]
    global contador
    contador+=1


    #CORRIDA 2
    seguir=True
    thread3.start()
    thread4.start()

    thread3.join()
    seguir=False
    thread4.join()
    datos()
    #generatedNumbers=[]
    #generatedNumbersA=[]
    contador+=1

    #CORRIDA 3
    seguir=True
    thread5.start()
    thread6.start()

    thread5.join()
    seguir=False
    thread6.join()
    datos()
    #generatedNumbers=[]
    #generatedNumbersA=[]
    contador+=1

    #CORRIDA 4
    seguir=True
    thread7.start()
    thread8.start()

    thread7.join()
    seguir=False
    thread8.join()
    datos()
    #generatedNumbers=[]
    #generatedNumbersA=[]
    contador+=1

    #CORRIDA 5
    seguir=True
    thread9.start()
    thread10.start()

    thread9.join()
    seguir=False
    thread10.join()
    datos()
    #generatedNumbers=[]
    #generatedNumbersA=[]
    contador+=1

    #CORRIDA 6
    seguir=True
    thread11.start()
    thread12.start()

    thread11.join()
    seguir=False
    thread12.join()
    datos()
    #generatedNumbers=[]
    #generatedNumbersA=[]
    contador+=1

    #CORRIDA 7
    seguir=True
    thread13.start()
    thread14.start()

    thread13.join()
    seguir=False
    thread14.join()
    datos()
    #generatedNumbers=[]
    #generatedNumbersA=[]
    contador+=1

    #CORRIDA 8
    seguir=True
    thread15.start()
    thread16.start()

    thread15.join()
    seguir=False
    thread16.join()
    datos()
    #generatedNumbers=[]
    #generatedNumbersA=[]
    contador+=1


    print("\n\n*******************DATOS FINALES **************:\n\n" , clientesAtendidos)
    print("\n\nTOTAL CLIENTES ATENDIDOS:\n\n", clientesAtendidos)
    print("\n\nCLIENTES QUE QUEDARON EN LA FILA:\n\n ",clientesFila)

    print("\n\nCANTIDAD DE CLIENTES ATENDIDOS: ",len(clientesAtendidos))
    print("CANTIDAD DE CLIENTES NO ATENDIDOS: ",len(clientesFila))
    print(":TOTAL PROMEDIO DE CLIENTES ATENDIDOS: ",(len(clientesAtendidos)/(len(clientesAtendidos) + len(clientesFila)))*100)
    print("TOTAL PROMEDIO DE CLIENTES NO: ",(len(clientesFila)/(len(tiempoClientesAtendidos) + len(clientesFila)))*100)
    diferenciaTiempo()
    print("MAXIMO DIFERENCIA TIEMPOS ESPERA: ", max(diferenciaTiemposEspera))

    listaFinal = clientesAtendidos
    for i in clientesFila:
        listaFinal.append(clientesFila.pop(0))

    return listaFinal

