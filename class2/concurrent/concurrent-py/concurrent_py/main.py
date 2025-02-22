# import concurrent.futures
# import time
# import requests

# def download_page(url):
#     response = requests.get(url)
#     return f"{url} - {len(response.content)} bytes"

# urls = [
#     "https://www.python.org",
#     "https://www.github.com",
#     "https://www.google.com"
# ]

# start_time = time.time()

# #ThreadPool - Concurrencia #IO dependientes
# #ProcessPool - Paralelismo. #CPU dependiente

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     #Crea futuros a ejecutar
#     futures = [executor.submit(download_page, url) for url in urls]

#     #Cuando los futuros esten listos
#     for future in concurrent.futures.as_completed(futures):
#         #TODO EL CODIGO QUE QUIERAS
#         print(future.result())

# end_time = time.time()
# print(f"Descargué todas las páginas en {end_time - start_time} segundos")

from calculator import series
import concurrent.futures
import time

def main():
    numbers = [500, 600, 700, 800]

    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(series.factorial, num) for num in numbers]

        for future in concurrent.futures.as_completed(futures):
            print(f"El factorial de {numbers[futures.index(future)]} es {future.result()}")

    end_time = time.time()

    print(f"Calculé todos los factoriales en {end_time - start_time} segundos")

if __name__ == '__main__':
    main()
