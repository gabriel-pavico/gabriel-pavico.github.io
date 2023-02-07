# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:49:10 2022

@author: gabri
"""

import arcpy
# from arcpy.sa import *

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'D:/OneDrive - Lund University/Map Files/13 - Thesis/Road_Density2.gdb'


# rasters = arcpy.ListRasters('Site_Brandrisk*')

# for raster in range(36,40):
#     i = rasters[raster]
#     arcpy.sa.ZonalStatisticsAsTable('fire_extents2018', 'ObjectId_1', f'{i}', f'D:/OneDrive - Lund University/Map Files/13 - Thesis/Road_Density2.gdb/{i}_mean', "DATA", "MEAN", "CURRENT_SLICE", 90, "AUTO_DETECT")
#     print(i)

tables = arcpy.ListTables('Site_Brandrisk*')
for i in tables:
    arcpy.conversion.TableToExcel(i, f'D:/OneDrive - Lund University/Map Files/13 - Thesis/griddata/{i}.xls', "NAME", "CODE")
    print(i)
