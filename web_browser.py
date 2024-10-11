"""Author:Shayinn"""
import webbrowser
import time

def abrir_pestaña_google(termino):
    url = f"https://www.virustotal.com/gui/file/{termino}"
    webbrowser.open_new_tab(url)

archivo = "terminos_busqueda.txt"
tiempo_espera = 2

with open(archivo, 'r') as f:
    for linea in f:
        termino = linea.strip()
        abrir_pestaña_google(termino)
        time.sleep(tiempo_espera)