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


if __name__ == "__main__":
    
    th2_args = ["https://jsonplaceholder.typicode.com/photos"]
    thread2 = threading.Thread(target=get_service, args=[th1_args[0]])
    thread2.start()