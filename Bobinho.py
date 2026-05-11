
from pybricks.parameters import Port
from pybricks.tools import wait
from lib.CNATMake_lib import CNATMAKER_Bot


robo = CNATMAKER_Bot()
cor_cond = 0
cont = 1
cor_c = 0
cor_d = 0
cor_c_cond = 0
cor_d_cond = 0
robo.atuador.movimento.configurar(esq=Port.E, dir=Port.F, cm_por_rotacao=17.5)
c = robo.sensor.cor.reflexao(Port.C)
d = robo.sensor.cor.reflexao(Port.D)
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

def dois_pretos():
    global g
    c_val = robo.sensor.cor.reflexao(Port.C)
    d_val = robo.sensor.cor.reflexao(Port.D)
    

    if c_val < 40 and d_val < 40:
        robo.atuador.movimento.mover(sentido="frente", cm=5, potencia=30)
        robo.atuador.movimento.parar()
        robo.sensor.giroscopio.resetar()
        while g < 90 and c_val >= 35:
            g = robo.ler_angulo_local()
            c_val = robo.sensor.cor.reflexao(Port.C)
            d_val = robo.sensor.cor.reflexao(Port.D)
            robo.atuador.motor.arrancar(Port.F, sentido="anti_horario", potencia=25)
            robo.atuador.motor.arrancar(Port.E, sentido="anti_horario", potencia=25)
            if c_val < 40:
                return seguir_linha()
        while d_val >= 35:
            c_val = robo.sensor.cor.reflexao(Port.C)
            d_val = robo.sensor.cor.reflexao(Port.D)
            robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=25)
            robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=25)
            if d_val < 40:
               return seguir_linha()

def quadrado_verde(cor_c, cor_d, cor_c_cond, cor_d_cond, cor_cond):
    cor_c = cor_c
    cor_d = cor_d
    cor_c_cond = cor_c_cond
    cor_d_cond = cor_d_cond
    cor_cond = cor_cond
    
    if cor_c_cond == 1 or cor_d_cond == 1:
        robo.atuador.movimento.parar()
        wait(1000)
          
    if cor_c_cond == 1 and cor_d_cond == 0 and cor_cond == 0:
        
        robo.atuador.movimento.mover(sentido="frente", cm=9, potencia=23)
        robo.atuador.movimento.girar(sentido="esquerda", graus=115, potencia=25)
        while robo.sensor.cor.reflexao(Port.D) > 40:
            robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=15)
            robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=15)
            if robo.sensor.cor.reflexao(Port.D) < 40:
                robo.atuador.movimento.parar()
                return 
            
    elif cor_d_cond == 1 and cor_c_cond == 0 and cor_cond == 0:
        
        robo.atuador.movimento.mover(sentido="frente", cm=9, potencia=23)
        robo.atuador.movimento.girar(sentido="direita", graus=90, potencia=25)
        while robo.sensor.cor.reflexao(Port.D) > 40:
            robo.atuador.motor.arrancar(Port.F, sentido="anti_horario", potencia=15)
            robo.atuador.motor.arrancar(Port.E, sentido="anti_horario", potencia=15)
            if robo.sensor.cor.reflexao(Port.D) < 40:
                robo.atuador.movimento.parar()
                return
            
    elif cor_cond == 1:
        robo.atuador.movimento.girar(sentido="esquerda", graus=260, potencia=25)
        while robo.sensor.cor.reflexao(Port.D) > 40:
            robo.atuador.motor.arrancar(Port.F, sentido="horario", potencia=15)
            robo.atuador.motor.arrancar(Port.E, sentido="horario", potencia=15)
            if robo.sensor.cor.reflexao(Port.D) < 40:
                robo.atuador.movimento.parar()
                return 


def obstaculo():
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
        robo.atuador.movimento.mover(sentido='frente', cm=28, potencia=20)
        while g < 0:
            g = robo.ler_angulo_local()
            robo.atuador.motor.arrancar(Port.F, sentido="anti_horario", potencia=25)
            robo.atuador.motor.arrancar(Port.E, sentido="anti_horario", potencia=25)
        robo.atuador.movimento.mover(sentido='frente', cm=55, potencia=20)
        while g < 90:
            g = robo.ler_angulo_local()
            robo.atuador.motor.arrancar(Port.F, sentido="anti_horario", potencia=25)
            robo.atuador.motor.arrancar(Port.E, sentido="anti_horario", potencia=25)
        c = robo.sensor.cor.reflexao(Port.C)
        d = robo.sensor.cor.reflexao(Port.D)
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
                

while True:
    d = robo.sensor.cor.reflexao(Port.D)
    c = robo.sensor.cor.reflexao(Port.C)
    cor_c = robo.sensor.cor.ler(Port.C)
    cor_d = robo.sensor.cor.ler(Port.D)
    
    if cor_d == "VERDE" and cor_c == "VERDE": 
        cor_cond = 1
    else: 
        cor_cond = 0  
    if cor_c == "VERDE":
        cor_c_cond = 1
    else:
        cor_c_cond = 0
        
    if cor_d == "VERDE":
        cor_d_cond = 1
    else:
        cor_d_cond = 0
        
    print(f"C:", c, "D:", d, "Angulo:", robo.ler_angulo_local(), robo.sensor.cor.ler(Port.C), robo.sensor.cor.ler(Port.D), cor_c_cond, cor_d_cond) 
        
    if cor_c == "VERMELHO" or cor_d == "VERMELHO":
        robo.atuador.movimento.parar()
        break
    elif cor_c_cond == 1 or cor_d_cond == 1:
        robo.atuador.movimento.mover(sentido="frente", cm=1, potencia=23)
        quadrado_verde(cor_c, cor_d, cor_c_cond, cor_d_cond, cor_cond)
    else:
        D = robo.sensor.distancia.ler(Port.A)
        if D < 75:  
            obstaculo()
        else:
            seguir_linha()
     
    
