#import libs if you run it outside of esri env.
import arcpy
from arcpy.sa import *
import os

#env
input_dir = r"..\WFS\WFS_data_analyst_task_data"
output_dir = r"..\WFS\WFS_arcpy"
arcpy.env.workspace = input_dir

#list all TIFF files
rasters = arcpy.ListRasters("*")

#define the remap ranges for classification
remap = RemapRange([
    [-998, -998, -998],  # No data
    [0.23, 0.35, 1],     # Cl. 1
    [0.35, 0.47, 2],     # Cl. 2
    [0.47, 0.59, 3],     # Cl. 3
    [0.59, 0.71, 4],     # Cl. 4
    [0.71, 0.90, 5]      # Cl. 5
])

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#classify each raster and add to list
classified_rasters = []
for raster in rasters:
    #reclassify and create a raster object
    classified_raster = Reclassify(raster, "Value", remap, "NODATA")
    classified_raster_path = os.path.join(output_dir, f"Classified_{os.path.basename(raster).split('.')[0]}.tif")
    #set nodata to -998 and out pixel type
    arcpy.CopyRaster_management(classified_raster, classified_raster_path, nodata_value=-998, pixel_type="16_BIT_SIGNED")
    #append raster object to list
    classified_rasters.append(Raster(classified_raster_path))

#calculate the mean of classified raster obj.
mean_classified_raster = CellStatistics(classified_rasters, "MEAN", "NODATA")

#reclassify the mean raster
mean_remap = RemapRange([
    [-998, -998, -998],  # No data
    [1, 3.5, 1],         # Cl. 1
    [3.5, 4, 2],         # Cl. 2
    [4, 4.5, 3],         # Cl. 3
    [4.5, 4.7, 4],       # Cl. 4
    [4.7, 5, 5]          # Cl. 5
])
reclassified_mean_raster = Reclassify(mean_classified_raster, "Value", mean_remap, "NODATA")

#save the reclassified mean raster
reclassified_mean_raster_path = os.path.join(output_dir, "EVI_Classified_Mean_Reclassified.tif")
arcpy.CopyRaster_management(reclassified_mean_raster, reclassified_mean_raster_path, nodata_value=-998, pixel_type="16_BIT_SIGNED")
