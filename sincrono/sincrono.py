import requests
import time
import concurrent.futures
import threading
import psycopg2

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)
        
def connect_db():
    try:
    conexion = psycopg2.connect(database='concurrencia', user='postgres', password='2022')
    cursor1=conexion.cursor()
    cursor1.execute('select version()')
    version=cursor1.fetchone()
except Exception as err:
    print('Error al conecta a la base de datos')

def get_service(url):
    response = requests.get(url)
    if response.status_code == 200:
        photos = response.json()
    for photo in photos:
        print(dataout["title"])
        write_db(photo["title"])

def write_db(title):
    try:
        cursor1.execute("insert into photos (title) values ('"+title+"')")
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conexion.commit()


if __name__ == "__main__":
    init_time = time.time()
    url_site = ["https://jsonplaceholder.typicode.com/photos"]
    service(url_site)
    end_time = time.time() - init_time
    print(end_time)