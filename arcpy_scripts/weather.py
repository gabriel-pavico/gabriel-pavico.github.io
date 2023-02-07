# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:29:58 2022

@author: gabri
"""
import arcpy
from arcpy import env

arcpy.env.workspace = 'D:/OneDrive - Lund University/Map Files/13 - Thesis/Road_Density2.gdb'

# featureClassList = arcpy.ListFeatureClasses()

with arcpy.EnvManager(extent="245167,77930309 6132288,34679233 1079706,17683153 7688269,30994789"):
    for i in range(24,31):
        print(f'Brandrisk_week_{i}')
        arcpy.ddd.Kriging(fr"Brandrisk_week_{i}", "Nederbord", fr"D:/OneDrive - Lund University/Map Files/13 - Thesis/Road_Density2.gdb/Brandrisk_week_{i}_precip", "Spherical 2593,820000 # # #", 1000, "VARIABLE 12", None)
        print('Done precip')
        arcpy.ddd.Kriging(fr"Brandrisk_week_{i}", "Temp", fr"D:/OneDrive - Lund University/Map Files/13 - Thesis/Road_Density2.gdb/Brandrisk_week_{i}_temp", "Spherical 2593,820000 # # #", 1000, "VARIABLE 12", None)
        print('Done temp')
        arcpy.ddd.Kriging(fr"Brandrisk_week_{i}", "FWI", fr"D:/OneDrive - Lund University/Map Files/13 - Thesis/Road_Density2.gdb/Brandrisk_week_{i}_fwi", "Spherical 2593,820000 # # #", 1000, "VARIABLE 12", None)
        print('Done fwi')
        arcpy.ddd.Kriging(fr"Brandrisk_week_{i}", "FWI_Index", fr"D:/OneDrive - Lund University/Map Files/13 - Thesis/Road_Density2.gdb/Brandrisk_week_{i}_fwi_index", "Spherical 2593,820000 # # #", 1000, "VARIABLE 12", None)
        print('Done fwi_index')
        arcpy.ddd.Kriging(fr"Brandrisk_week_{i}", "Vindhastighet", fr"D:/OneDrive - Lund University/Map Files/13 - Thesis/Road_Density2.gdb/Brandrisk_week_{i}_wind", "Spherical 2593,820000 # # #", 1000, "VARIABLE 12", None)
        print('Done wind')
        arcpy.ddd.Kriging(fr"Brandrisk_week_{i}", "RH", fr"D:/OneDrive - Lund University/Map Files/13 - Thesis/Road_Density2.gdb/Brandrisk_week_{i}_humid", "Spherical 2593,820000 # # #", 1000, "VARIABLE 12", None)
        print('Done humid')
