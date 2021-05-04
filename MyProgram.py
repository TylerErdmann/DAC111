# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:43:49 2021

@author: erdma
"""
import sqlite3 as sl

FLIGHTS_DB = "C:/src/DAC111/flights.db"

def main():
    connection = sl.connect(FLIGHTS_DB)
    cursor = connection.cursor()
    
    query = "select * from airlines limit 5;"
    cursor.execute(query)
    
    results = cursor.fetchall()
    print(results)
    
    cursor.close()
    connection.close()
    
main()

