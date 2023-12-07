import arcpy
from arcpy.sa import *
Red_band = ( r”raster file location.tif”)
NIR_band = ( r”raster file location.tif”)
NDVI_Raster_date = Divide(Float(Raster(NIR_band) - Raster(Red_band)) , Float(Raster(NIR_band) + Raster(Red_band)))  
NDVI_Raster_date.save ( r”Save location/Name.tif”)