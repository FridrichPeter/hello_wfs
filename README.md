# EVI Raster Classification

This project provides a methodology for classifying Enhanced Vegetation Index (EVI) raster data to assess vegetation vitality in various classes. Using ArcPy and its Spatial Analyst module, the script classifies, averages, and reclassifies EVI raster files, resulting in a mean classified raster output.

## Methodology

1. **Initial Data Analysis**: Each raster's `min`, `max`, `mean`, and `std` values are extracted using `gdalinfo`. This analysis helps to understand data distribution and is crucial for defining the remap ranges for classification.
   
2. **Classification of EVI Rasters**: Each raster is classified into five classes based on predefined EVI value ranges, informed by the data analysis step. Classes represent vegetation vitality, with `NoData` values set to -998.

3. **Mean Calculation**: Using `CellStatistics`, the script calculates an average value for each classified raster across the input rasters.

4. **Reclassification**: The mean raster is then reclassified to simplify interpretation, creating a final output for analysis.

## Tools and Libraries

- **GDAL (`gdalinfo`)**: Used to analyze raster statistics before classification to determine appropriate value ranges.
- **ArcPy**: Python library for geoprocessing tasks.
- **ArcPy Spatial Analyst (`arcpy.sa`)**: Used for `Reclassify` and `CellStatistics` functions to handle raster classification and aggregation.

## Output

- **Classified Rasters**: Intermediate rasters for each input, classified into five classes.
- **Final Reclassified Mean Raster**: `EVI_Classified_Mean_Reclassified.tif`, providing an average vegetation vitality view.

## Usage

1. Run `gdalinfo` on each raster to collect statistical values.
2. Modify the remap ranges in the script based on the observed statistics.
3. Run the script to process EVI TIFF files in the specified `input_dir` and store outputs in `output_dir`.

---

### Requirements
- GDAL for raster analysis
- ArcPy with Spatial Analyst extension
- Python environment compatible with ArcPy (typically ArcGIS Pro's Python environment)

---
