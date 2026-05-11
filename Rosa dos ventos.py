from pybricks.parameters import Port
from pybricks.tools import wait
from lib.CNATMake_lib import CNATMAKER_Bot
cont = 1
  
robo = CNATMAKER_Bot()
robo.atuador.movimento.configurar(esq=Port.E, dir=Port.F, cm_por_rotacao=17.5)


g_inicial = robo.ler_angulo_local()
norte = g_inicial 
leste = g_inicial + 90
oeste = g_inicial - 90
sul = g_inicial + 180
print("norte: ", norte, "leste: ", leste, "oeste: ", oeste, "sul: ", sul)

c = robo.sensor.cor.reflexao(Port.C)
d = robo.sensor.cor.reflexao(Port.D)
D = robo.sensor.distancia.ler(Port.A)
c_val = robo.sensor.cor.reflexao(Port.C)
d_val = robo.sensor.cor.reflexao(Port.D)
g = robo.ler_angulo_local()

def seguir_linha():
	c = robo.sensor.cor.reflexao(Port.C)
	d = robo.sensor.cor.reflexao(Port.D)
	if c > 40 and d > 40:
		robo.atuador.movimento.arrancar(sentido="frente", potencia=23)
	elif c > 40 and d < 40:
		robo.atuador.motor.arrancar(Port.F, sentido="anti_horario", potencia=25)
		robo.atuador.motor.arrancar(Port.E, sentido="anti_horario", potencia=25)
	elif d > 40 and c < 40:
		robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=25)
		robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=25)


def obstaculo(norte, sul, leste, oeste):
    global g
    norte = norte
    sul = sul
    leste = leste 
    oeste = oeste
    D = robo.sensor.distancia.ler(Port.A)
    if D < 75:
        robo.atuador.movimento.parar()
        robo.sensor.giroscopio.resetar()
        wait(500)
        g = robo.ler_angulo_local()
        while g > -90:
            g = robo.ler_angulo_local()
            robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=25)
            robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=25)
        if  g > oeste:
            while g > oeste:
                g = robo.ler_angulo_local()
                robo.atuador.motor.arrancar(Port.F, sentido="anti_horario", potencia=10)
                robo.atuador.motor.arrancar(Port.E, sentido="anti_horario", potencia=11)

        elif g < oeste:
            while g < oeste:
                g = robo.ler_angulo_local()
                robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=10)
                robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=11)
                print("passei no oeste 2")
                print(g)
        robo.atuador.movimento.mover(sentido='frente', cm=28, potencia=20)
        while g < 0:
            g = robo.ler_angulo_local()
            robo.atuador.motor.arrancar(Port.F, sentido="anti_horario", potencia=25)
            robo.atuador.motor.arrancar(Port.E, sentido="anti_horario", potencia=25)
        if  g > norte:
            while g > norte:
                g = robo.ler_angulo_local()
                robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=25)
                robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=25)
        elif robo.ler_angulo_local() < norte:
            while robo.ler_angulo_local() < norte:
                g = robo.ler_angulo_local()
                robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=20)
                robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=20)
        robo.atuador.movimento.mover(sentido='frente', cm=55, potencia=20)
        while g < 90:
            g = robo.ler_angulo_local()
            robo.atuador.motor.arrancar(Port.F, sentido="anti_horario", potencia=25)
            robo.atuador.motor.arrancar(Port.E, sentido="anti_horario", potencia=25)
        if g > leste:
            g = robo.ler_angulo_local()
            robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=25)
            robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=25)
        elif g < leste:
            g = robo.ler_angulo_local()
            robo.atuador.motor.arrancar(Port.F, sentido="anti_horario", potencia=25)
            robo.atuador.motor.arrancar(Port.E, sentido="anti-horario", potencia=25)

        while c > 40 and d > 40 :
            c = robo.sensor.cor.reflexao(Port.C)
            d = robo.sensor.cor.reflexao(Port.D)
            robo.atuador.movimento.arrancar(sentido='frente', potencia=20)
        if c < 40 and d < 40:
            robo.atuador.movimento.mover(sentido='frente', cm=5, potencia=20)
            while d >= 35:
                d = robo.sensor.cor.reflexao(Port.D)
                robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=25)
                robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=25)
                if d < 35:
                    return seguir_linha()

while cont == 1:
    seguir_linha()
    obstaculo(norte, sul, leste, oeste)
