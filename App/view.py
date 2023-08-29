"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback

default_limit = 1000
sys.setrecursionlimit(default_limit*10)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos de los archivos CSV
    """

    
    # Cargar resultados de partidos
    result_file = "results-utf8.csv"
    controller.load_data(control, result_file, "results")
    
    # Cargar anotaciones de jugadores
    goalscorers_file = "goalscorers-utf8.csv"
    controller.load_data(control, goalscorers_file, "goalscorers")
    
    # Cargar definiciones de partidos desde el punto penal
    shootouts_file = "shootouts-utf8.csv"
    controller.load_data(control, shootouts_file, "shootouts")
    
    print("Carga de datos completa.")


    

def print_results(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    matches = controller.sort_results(control)
    
    headers = ["Match Date", "Home Team", "Away Team", "Home escore", "Away score", "Tournament", "Country", "City"]
    table = []
    
    for match in lt.iterator(matches):
        table.append([
            match["date"],
            match["home_team"],
            match["away_team"],
            match['home_score'],
            match['away_score'],
            match["tournament"],
            match["country"],
            match["city"]
        ])
    
    print(tabulate(table, headers=headers, tablefmt="grid"))


def print_goalscorers_data(control):
    goalscorers = controller.sort_goalscorers(control)
    
    headers = ["Match Date", "Home Team", "Away Team", "Player", "Player's Team", "Minute", "Penalty", "Own Goal"]
    table = []
    
    for goalscorer in lt.iterator(goalscorers):
        table.append([
            goalscorer["date"],
            goalscorer["home_team"],
            goalscorer["away_team"],
            goalscorer["scorer"],
            goalscorer["scorer_team"],
            goalscorer["minute"],
            goalscorer["penalty"],
            goalscorer["own_goal"]
        ])
    
    print("Total goalscorers loaded:", lt.size(goalscorers))
    print(tabulate(table, headers=headers, tablefmt="grid"))

def print_shootouts_data(control):
    shootouts = controller.sort_shootouts(control)
    
    headers = ["Match Date", "Home Team", "Away Team", "Winner"]
    table = []
    
    for shootout in lt.iterator(shootouts):
        table.append([
            shootout["date"],
            shootout["home_team"],
            shootout["away_team"],
            shootout["winner"]
        ])
    
    print("Total shootouts loaded:", lt.size(shootouts))
    print(tabulate(table, headers=headers, tablefmt="grid"))




def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            print_results(control)
            print_goalscorers_data(control)
            print_shootouts_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
