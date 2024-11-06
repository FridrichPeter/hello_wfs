# EVI Raster Classification

This project provides a methodology for classifying Enhanced Vegetation Index (EVI) raster data to assess vegetation vitality in various classes. The script offers two approaches: one using ArcPy and its Spatial Analyst module, and another with `rasterio` and `numpy`. Each approach classifies, averages, and reclassifies EVI raster files, resulting in a mean classified raster output.

## Methodology

1. **Initial Data Analysis**: Each raster's statistics (`min`, `max`, `mean`, and `std`) are extracted using `gdalinfo` to analyze data distribution and define classification ranges effectively.

2. **Classification of EVI Rasters**: 
   - **ArcPy**: Rasters are classified into five classes using predefined EVI value ranges, representing vegetation vitality, with `NoData` values set to -998.
   - **Rasterio and Numpy**: The code defines classification bins and values, then iterates over rasters to reclassify them using the `reclassify` function with `numpy.digitize`. Classified rasters are saved as 16-bit signed TIFF files with `NoData` set to -998.

3. **Mean Calculation**: 
   - **ArcPy**: The `CellStatistics` tool is used to calculate the mean of classified raster objects.
   - **Rasterio and Numpy**: `numpy.nanmean` is used to stack the classified rasters and compute the mean array.

4. **Reclassification of the Mean Raster**: The mean raster is reclassified into simplified classes, resulting in a final output for analysis.

## Tools and Libraries

- **GDAL (`gdalinfo`)**: Used to analyze raster statistics before classification.
- **ArcPy and ArcPy Spatial Analyst (`arcpy.sa`)**: Used for `Reclassify` and `CellStatistics`.
- **Rasterio and Numpy**: Provides an alternative approach to reading, processing, and reclassifying rasters.

## Output

- **Classified Rasters**: Intermediate rasters for each input, classified into five classes and saved in `WFS_arcpy` (ArcPy) and `WFS_rasterio` (rasterio).
- **Final Reclassified Mean Raster**: `EVI_Classified_Mean_Reclassified.tif`, showing the average vegetation vitality in five classes.

## Usage

1. Run `gdalinfo` to collect statistics from each raster.
2. Adjust classification ranges based on observed statistics.
3. Choose either ArcPy or Rasterio/Numpy methods to process the TIFF files in `input_dir` and store outputs in `output_dir`.

---

### Requirements

- GDAL for data analysis
- ArcPy with Spatial Analyst extension or Rasterio/Numpy for classification
- Python environment compatible with ArcPy (if using the ArcPy approach)

--- 
