import threading
import random
import time

turn = random.randint(0, 1) #creamos un semaforo
def proceso1():
    global turn 
    while(turn!=0):
        pass
    print("Proceso 1 en la seccion critica se cambia el turno a 1\n")
    turn = 1


def proceso2():
    global turn 
    while(turn!=1):
        pass
    print("Proceso 2 en la seccion critica se cambia el turno a 0\n")
    turn = 0

if __name__ == '__main__':
    i = 0
    while(True):
        turn = random.randint(0, 1)
        print(f"Interacion N: {i + 1}\n")
        print(f"La variable turno: {turn} \n")

        #Creamos los hilos
        hilo1 = threading.Thread(target=proceso1,daemon=True,)
        hilo2 = threading.Thread(target=proceso2,daemon=True,)
        
        hilo1.start()
        hilo2.start()
        print("\n\n")

        time.sleep(3)
        i = i + 1
        if i == 16:
            hilo1.join()
            hilo2.join()
            break

    


