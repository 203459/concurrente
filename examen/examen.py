import threading
import time

palillosArray = [1,1,1,1,1,1,1,1]

class PalilloPersona(threading.Thread):
     def __init__(self, palillos, personaNum):
        threading.Thread.__init__(self)
        self.palillos = palillos
        self.personaNum = personaNum
        self.datoTemporal =  (self.personaNum + 1) % 8
        
     def tomarPalillos(self):
        self.palillos[self.personaNum].acquire()
        print(f'Persona {self.personaNum} recoge el palillo del lado izquierdo')
        #time.sleep(2)
        time.sleep(0.5)
        self.palillos[self.datoTemporal].acquire()
        print(f'Persona {self.personaNum} recoge el palillo del lado derecho')
        #time.sleep(2)
        time.sleep(0.5)

     def dejarPalillos(self):

        print(f'Persona {self.personaNum} deja el palillo izquierdo')
        self.palillos[self.datoTemporal].release()
        time.sleep(0.5)
        
        print(f'Persona {self.personaNum} deja el palillo derecho')
        self.palillos[self.personaNum].release()
        time.sleep(0.5)
        print(f'Persona {self.personaNum} ha terminado de comer')
        time.sleep(2)

     def run(self):
        print(f'Persona {self.personaNum} esperando')
        #time.sleep(2)
        self.tomarPalillos()
        self.dejarPalillos()


if __name__ == '__main__':
    for i in range(0,8):
        palillosArray[i] = threading.BoundedSemaphore(2)

    for i in range(0,8):
        total = PalilloPersona(palillosArray, i)
        total.start()
        time.sleep(3)