# Q_viewshed

# Objetivo
Calcula la cuenca visual para cada punto de una capa shapefile de puntos.
La altura del punto puede proceder de un atributo de la capa bien una altura igual para todos los puntos.

#Parámetros
Puntos = "Z:/Proxectos/589_astillero_4_0/5_gis/shp/20180529_Astillero_nuevo/Viewshed_puntos.shp"
MDE = "Z:/Proxectos/589_astillero_4_0/5_gis/paisaje/LIDAR_1km/MDE_cota.tif"
Output = "Z:/Proxectos/589_astillero_4_0/5_gis/paisaje/Viewshed_provisional_MDE_cota6_15km"
AltAtr = "Altura"
AltElem = int(100)
AltObs = float(1.8)
Distancia = int(1000)
Memoria = int(2000)
CurvTer = bool(1)
RefAtm = bool(1)
Acumulado = bool(1)
Visibilidad01 = bool(1)

## Condiciones:
-- Shapefile de puntos. Puede haber un atributo con la altura de cálculo (AltAtr).
-- MDT en formato raster.

## Salida: 
Solo se necesita especificar la carpeta de salida, en ella se guardarán todos los archivos con el nombre "viewshed_id". 
El archivo de suma se llamará "viewshed_suma"