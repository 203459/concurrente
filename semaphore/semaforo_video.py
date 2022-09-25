from threading import Thread, Semaphore
from pytube import YouTube
semaforo = Semaphore(1)

links =["https://www.youtube.com/watch?v=uS50rVFkheE",
        "https://www.youtube.com/watch?v=9pjIxtf7Y74",
        "https://www.youtube.com/watch?v=R3_XT1qzL2Q",
        "https://www.youtube.com/watch?v=CjyQA4thaMk",
        "https://www.youtube.com/watch?v=bo9Z_pgByQY"]

def critico(links):
     video= YouTube(links)
     file = video.streams.filter(file_extension='mp4').get_by_itag(18)

class Hilo(Thread):
    def __init__(self, links):
        Thread.__init__(self)
        self.links=links
    
    def run(self):
        semaforo.acquire()#inicializacion semaforo
        critico(self.links)
        semaforo.release()#librera un semaforo e incrementa la variable semaforo


threads_semaphore = [Hilo(links[0]), Hilo(links[1]), Hilo(links[2]), Hilo(links[3]), Hilo(links[4])]

for t in threads_semaphore:
     t.start()