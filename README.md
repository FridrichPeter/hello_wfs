# EVI Raster Classification

This project provides a methodology for classifying Enhanced Vegetation Index (EVI) raster data to assess vegetation vitality in various classes. Using ArcPy and its Spatial Analyst module, the script classifies, averages, and reclassifies EVI raster files, resulting in a mean classified raster output.

## Methodology

1. **Classification of EVI Rasters**: Each raster is classified into five classes based on predefined EVI value ranges. Classes represent vegetation vitality, with `NoData` values set to -998.
2. **Mean Calculation**: Using `CellStatistics`, the script calculates an average value for each classified raster across the input rasters.
3. **Reclassification**: The mean raster is then reclassified to simplify interpretation, creating a final output for analysis.

## Tools and Libraries

- **ArcPy**: Python library for geoprocessing tasks.
- **ArcPy Spatial Analyst (`arcpy.sa`)**: Used for `Reclassify` and `CellStatistics` functions to handle raster classification and aggregation.

## Output

- **Classified Rasters**: Intermediate rasters for each input, classified into five classes.
- **Final Reclassified Mean Raster**: `EVI_Classified_Mean_Reclassified.tif`, providing an average vegetation vitality view.

## Usage

Run the script to process EVI TIFF files in the specified `input_dir` and store outputs in `output_dir`.

---

### Requirements
- ArcPy with Spatial Analyst extension
- Python environment compatible with ArcPy (typically ArcGIS Pro's Python environment)

---

