#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Ing.Jesús Matías González
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Ing.Jesús Matías González"
__email__ = "ingjesusmrgonzalez@gmail.com"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html

def create_schema():
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS estudiante;")

    c.execute("""
        CREATE TABLE estudiante(
            [identificador] INTEGER PRIMARY KEY AUTOINCREMENT,
            [nombre] TEXT NOT NULL,
            [edad] INTEGER NOT NULL,
            [grado] INTEGER,
            [tutor] TEXT
        );
    """)

    conn.commit()
    conn.close()

def fill(nombre, edad, grado=None, tutor=None):
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    values = [nombre, edad, grado, tutor]
    c.execute("""
        INSERT INTO estudiante (nombre, edad, grado, tutor)
        VALUES (?,?,?,?);
    """, values)

    conn.commit()
    conn.close()

def fetch():
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    print('\n📋 Listado de estudiantes:')
    for row in c.execute('SELECT * FROM estudiante'):
        print(row)

    conn.close()

def search_by_grade(grade):
    print(f'\n🔍 Estudiantes en grado {grade}:')
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    for row in c.execute("SELECT identificador, nombre, edad FROM estudiante WHERE grado = ?", (grade,)):
        print(row)

    conn.close()
    
def insert(student):
    print('\n➕ Insertando nuevo estudiante...')
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    c.execute("""
        INSERT INTO estudiante (nombre, edad)
        VALUES (?,?);
    """, student)

    conn.commit()
    conn.close()

def modify(id, name):
    print(f'\n✏️ Modificando estudiante con id {id}...')
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    rowcount = c.execute("""
        UPDATE estudiante SET nombre = ?
        WHERE identificador = ?;
    """, (name, id)).rowcount

    print('Filas actualizadas:', rowcount)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python 🚀")

    create_schema()

    # Insertar estudiantes
    fill("Jesús González", 40, 1, "Madre")
    fill("Rosa Chavez", 28, 1, "Madre")
    fill("Carolina Figueroa", 24, 2, "Padre")
    fill("Francisco Gallo", 23, 2, "Madre")
    fill("Gastón Villarreal", 35, 3, "Padre")

    fetch()

    grade = 3
    search_by_grade(grade)

    # Insertar un nuevo estudiante
    new_student = ['You', 16]
    insert(new_student)

    fetch()

    # Modificar nombre de un estudiante
    name = '¿Instituto Zuviría?'
    id = 2
    modify(id, name)

    fetch()

    print("\n Programa finalizado correctamente.")
