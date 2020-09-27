
g = 9.8
potencia = 0

check = True

def calcular_potencia (tiempo, masa , altura):
    global potencia
    energia_potencial = 9.8 * masa * altura
    potencia = energia_potencial/tiempo
    return(f"La potencia {potencia} W")

def momomentoyomega (diametro, tiempo, radio_eje):
    radio = diametro/2
    circun= 2* 3.141592 * radio
    vueltas = altura/ circun
    w= vueltas/ tiempo
    w_rpm = w * 60
    w_rad = w * 2*3.141592
    momentum = potencia/w_rad
    fuerza = momentum/ radio_eje
    return(f"La velocidad angular es {w} rev/s {w_rpm} rpm {w_rad} rad/s",f"El momento par es de {momentum} N M", f"la fuerza sobre los cangilones es de {fuerza} N" )

print ("Asegurese que sus datos esten en metros, kilogramos y segundo")
checkeo = input("Si tienes los datos en S.I, ESCRIBA 'SI' , en caso de faltar alguna conversion escriba 'no'")

if checkeo == "SI":
    tiempo = float(input("inserte el tiempo"))
    masa= float(input("Masa del peso"))
    altura =float(input("Inserte altura"))
    resultado = calcular_potencia (tiempo, masa, altura)
    print (resultado)

    diametro= float(input("coloca diametro"))
    radio_eje= float(input("Introduzca su radio del eje al extremo para el momento par"))
    resultadofw= momomentoyomega(diametro,tiempo,radio_eje)
    print (resultadofw)
else:
    print("Reinicie el código cuando tenga todas las unidades especificadas")