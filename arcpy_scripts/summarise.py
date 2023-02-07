# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:14:48 2022

@author: gabri
"""

import arcpy
import numpy as np
import statistics

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'D:/OneDrive - Lund University/Map Files/13 - Thesis/Road_Density2.gdb'

# featureclasses = arcpy.ListFeatureClasses('grid_*')
# featureclasses = ['grid_forest_parcels', 'grid_wetland_parcels', 'grid_open_parcels', 'grid_fire_extents2018', 'grid_connected_wetland', 'grid_connected_openland', 'grid_connected_forest']
featureclasses = ['grid_fire_extents2018', 'grid_connected_wetland', 'grid_connected_openland', 'grid_connected_forest']

grid = 'fishnet_sweden'

#get fields
# fields = arcpy.ListFields(grid)
# fld = []
# for field in fields:
#     fld.append(field.name)
# skipped
fld = ['OID']


#get ID of grids
# oid = []    
# with arcpy.da.SearchCursor(grid, fld[0]) as cursor:
#     for row in cursor:
#         oid.append(row[0])
# for quicker processing, above is skipped


for fc in featureclasses:
    print(fc)
    tbl = []
    for x in range(1,145):
        tbl.append(x)
    
    mean = []
    median = []
    for i in range(144):
        #iterate through grids
        print(tbl[i])
        select_grid = arcpy.SelectLayerByAttribute_management(grid, 'NEW_SELECTION', f'{fld[0]} = {tbl[i]}')
        
        #select features in grid
        select_features = arcpy.management.SelectLayerByLocation(fc, 'WITHIN', select_grid)
        values = []
        
        #extract values of selected features
        for row in arcpy.da.SearchCursor(select_features, ['fid', 'area']):
            print(f'ID: {row[0]} Area: {row[1]}')
            values.append(row[1])
        
        #if empty values
        if len(values) == 0:
            mean.append(0)
            median.append(0)
        else:
            mean.append(statistics.mean(values))
            median.append(statistics.median(values))
    
    table = np.column_stack([tbl, mean, median])
    np.savetxt(f'D:/OneDrive - Lund University/Map Files/13 - Thesis/griddata/{fc}.csv', table, delimiter=',', fmt='%.6f')
