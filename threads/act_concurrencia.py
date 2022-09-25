import requests
import psycopg2
import concurrent.futures
import threading
import time
from pytube import YouTube

try: 
    conexion = psycopg2.connect(database='concurrencia', user='postgres', password='2022')
    cursor1=conexion.cursor()
    cursor1.execute('select version()')
    version=cursor1.fetchone()
except Exception as err:
    print('Error al conecta a la base de datos')

def get_service(url):
    r = requests.get(url)
    photos = r.json()
    for photo in photos:
        write_db(photo["title"])

def write_db(title):
    try:
        cursor1.execute("insert into photos (title) values ('"+title+"')")
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conexion.commit()

def service_videos(link):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_videos, link)

def get_videos(link):
    video = YouTube(link)
    video.streams.filter(
        file_extension='mp4').get_by_itag(18).download()

def get_services(dato=0):
    response = requests.get('https://randomuser.me/api/')
   #print(f"Dato{dato}")
    if response.status_code == 200:
       results = response.json().get('results')
       name = results[0].get('name').get('first')
       print(name)


if __name__ == "__main__":

    link = ["https://www.youtube.com/watch?v=uS50rVFkheE",
            "https://www.youtube.com/watch?v=9pjIxtf7Y74",
            "https://www.youtube.com/watch?v=R3_XT1qzL2Q",
            "https://www.youtube.com/watch?v=CjyQA4thaMk",
            "https://www.youtube.com/watch?v=bo9Z_pgByQY"]
            

    th1 = threading.Thread(target=service_videos, args=[link])
    th1.start()
    
    th2_args = ["https://jsonplaceholder.typicode.com/photos"]
    thread2 = threading.Thread(target=get_service, args=[th1_args[0]])
    thread2.start()

for x in range(0,50):
    th3 = threading.Thread(target=get_services, args=[x])
    th3.start()