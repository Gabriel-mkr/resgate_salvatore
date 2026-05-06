
from pybricks.parameters import Port
from pybricks.tools import wait
from lib.CNATMake_lib import CNATMAKER_Bot


robo = CNATMAKER_Bot()

cont = 1
cor_c = 0
cor_d = 0
robo.atuador.movimento.configurar(esq=Port.E, dir=Port.F, cm_por_rotacao=17.5)
c = robo.sensor.cor.reflexao(Port.C)
d = robo.sensor.cor.reflexao(Port.D)
c_val = robo.sensor.cor.reflexao(Port.C)
d_val = robo.sensor.cor.reflexao(Port.D)

def seguir_linha():
	c = robo.sensor.cor.reflexao(Port.C)
	d = robo.sensor.cor.reflexao(Port.D)
	if c > 40 and d > 40:
		robo.atuador.movimento.arrancar(sentido="frente", potencia=30)
	elif c > 40 and d < 40:
		robo.atuador.motor.arrancar(Port.F, sentido="anti_horario", potencia=25)
		robo.atuador.motor.arrancar(Port.E, sentido="anti_horario", potencia=25)
	elif d > 40 and c < 40:
		robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=25)
		robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=25)

def dois_pretos():
    c_val = robo.sensor.cor.reflexao(Port.C)
    d_val = robo.sensor.cor.reflexao(Port.D)

    if c_val < 45 and d_val < 45:
        robo.atuador.movimento.mover(sentido="frente", cm=5, potencia=30)
        robo.atuador.movimento.parar()
        robo.sensor.giroscopio.resetar()
        while robo.ler_angulo_local() > -90 or c_val >= 35:
            c_val = robo.sensor.cor.reflexao(Port.C)
            d_val = robo.sensor.cor.reflexao(Port.D)
            robo.atuador.movimento.girar(sentido="esquerda", graus=15, potencia=25)
            if d_val < 40:
                return seguir_linha()
        while d_val >= 35:
            c_val = robo.sensor.cor.reflexao(Port.C)
            d_val = robo.sensor.cor.reflexao(Port.D)
            robo.atuador.movimento.girar(sentido="direita", graus=15, potencia=25)
            if c_val < 40:
               return seguir_linha()

def quadrado_verde():
    cor_c = robo.sensor.cor.ler(Port.C)
    cor_d = robo.sensor.cor.ler(Port.D)
    
    if cor_c == "VERDE" or cor_d == "VERDE":
        robo.atuador.movimento.parar()
        
        if cor_c == "VERDE" and cor_d != "VERDE":
            robo.atuador.movimento.mover(sentido="frente", cm=5, potencia=30)
            robo.atuador.movimento.girar(sentido="esquerda", graus=45, potencia=25)
            while True:
                d = robo.sensor.cor.reflexao(Port.D)
                robo.atuador.movimento.girar(sentido="esquerda", graus=10, potencia=25)
                if d < 40:
                    return seguir_linha()
        
        elif cor_d == "VERDE" and cor_c != "VERDE":
            robo.atuador.movimento.mover(sentido="frente", cm=5, potencia=30)
            robo.atuador.movimento.girar(sentido="direita", graus=45, potencia=25)
            while True:
                c = robo.sensor.cor.reflexao(Port.C)
                robo.atuador.movimento.girar(sentido="direita", graus=15, potencia=25)
                if c < 40:
                    return seguir_linha()               
        
        elif cor_c == "VERDE" and cor_d == "VERDE":
            robo.atuador.movimento.girar(sentido="direita", graus=180, potencia=25)
            robo.atuador.movimento.parar()
            return dois_pretos()

while True:
    d = robo.sensor.cor.reflexao(Port.D)
    c = robo.sensor.cor.reflexao(Port.C)
    cor_c = robo.sensor.cor.ler(Port.C)
    cor_d = robo.sensor.cor.ler(Port.D)
    print(f"C:", c, "D:", d, "Angulo:", robo.ler_angulo_local(), robo.sensor.cor.ler(Port.C), robo.sensor.cor.ler(Port.D))
    seguir_linha()
    dois_pretos()
    quadrado_verde()
    
