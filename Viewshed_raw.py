##Viewshed=group
##Viewshed=name
##Puntos=vector Point
##MDE=raster
##Output=folder
##AtributoAltura=string Altura
##AltElem=number 180
##AltObs=number 1.8
##Distancia=string 5000
##Memoria=number 2000
##CurvTer=boolean TRUE
##RefAtm=boolean TRUE
##Acumulado=boolean TRUE
##Visibilidad01=boolean TRUE

from PyQt4.QtCore import QFileInfo, QSettings, QVariant
from qgis.core import *
import qgis.utils
import os, glob, processing, string, time, shutil, os.path, subprocess

#parametros
Puntos = "Z:/Proxectos/573_Adelanta_DocumentosAmbientaisPPEE/140_PPEE_SUIDO/5_GIS/SHP/PE_CDA/Alternativa_B_20180117/Aeros_AltB_20180117.shp"
MDE = "Z:/Material/SIG/_00_Base/_01b_MDT05_Gal_clip/_01b_MDT05_Gal_clip.tif"
Output = "Z:/Proxectos/573_Adelanta_DocumentosAmbientaisPPEE/140_PPEE_SUIDO/5_GIS/PE_CDA_paisaje/Visibilidad_MDT05_15km_AltB/"
AtributoAltura = "Altura"
AltElem = int(180)
AltObs = float(1.75)
Distancia = int(15000)
Memoria = int(2000)
CurvTer = bool(1)
RefAtm = bool(1)
Acumulado = bool(1)
Visibilidad01 = bool(1)

#crear capa vectorial a partir de la ruta anterior
layer = QgsVectorLayer(Puntos, "testlayer_shp", "ogr")
features = layer.getFeatures()

#crear lista vacia para meter los rasters que despues seran sumados
lista = list()

#extension del raster (servira para los procesos posteriores)
rasterlayer = QgsRasterLayer(MDE,"rasterlayer")
rasterext = rasterlayer.extent()
xmin = rasterext.xMinimum()
xmax = rasterext.xMaximum()
ymin = rasterext.yMinimum()
ymax = rasterext.yMaximum()
extension = "%f,%f,%f,%f" %(xmin, xmax, ymin, ymax)

#iterar sobre features de capa de puntos y ejecutar viewshed para cada punto
count=int(1)
for f in features:
    geom = f.geometry()
   # crear coordenada de punto
    a = geom.asPoint()
    punto = str(str(int(a[0]))+','+str(int(a[1])))
    id = str(count)
   # nombre de archivo de salida y lista con los archivos creados
    salida = str(Output+"/"+"viewshed"+"_"+id+".tif")
    lista.append(salida)
    #si el campo AtributoAltura no esta vacio pillar el valor de ese atributo de cota altura o lo que sea
    #si esta vacio entonces pillar el valor de AltElem
    if AtributoAltura !="":
        Altura = f[AtributoAltura]
    elif AtributoAltura == "":
        Altura = AltElem
    
    if os.path.isfile(salida) is not True:
        print ("Procesando id:"+' '+id)
        print (Altura)
        # proceso de viewshed
        processing.runalg('grass7:r.viewshed',
        MDE,
        punto,
        Altura,
        AltObs,
        Distancia,
        0.14286,
        Memoria,
        CurvTer,
        RefAtm,
        True,False,
        extension,
        0,
        salida)
        count+=1

#suma de rasters
# if Acumulado == True:
	# AcumuladoTif = str(Output+"/"+"viewshed"+"_"+"acumulado"+".tif")
	# if os.path.isfile(AcumuladoTif) is not True:
		# print ("Procesando raster acumulado")
		# processing.runalg("grass7:r.series",lista,False,10,"-10000000000,10000000000",extension,0,AcumuladoTif)

# if Visibilidad01 == True:
	# Visibilidad01Tif = str(Output+"/"+"viewshed"+"_"+"vis01"+".tif")
	# if os.path.isfile(Visibilidad01Tif) is not True:
		# print ("Creando raster de visibilidad 1 o visibilidad 0")
		# processing.runalg("grass7:r.series",lista,False,6,"-10000000000,10000000000",extension,0,Visibilidad01Tif)	