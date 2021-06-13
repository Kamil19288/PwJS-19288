# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 11:23:57 2021

@author: patry
"""

import sqlite3

if __name__ == "__main__":

    conn = sqlite3.connect('database.db')
    print("DB is open")
    
    conn.execute('CREATE TABLE pracownicy (imienazwisko TEXT, nrpracownika TEXT, adres TEXT)')
    print("Tabela utworzona")
    
    conn.close()
    print("BD zamknieta")
    
    
    conn = sqlite3.connect('database.db')
    print("BD otwarta")
    cur = conn.cursor()
    
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Patryk Pieczarka','1','Elblag') )
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Szymon Bednarski','2','Sopot') )
    conn.commit()
    
    cur.execute('SELECT * FROM pracownicy ORDER BY nrpracownika')
    print(cur.fetchall())
    #zamkniecie DB
    conn.close()
    print("DB is close")