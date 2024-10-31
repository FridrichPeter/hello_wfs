#import libs
import rasterio
import numpy as np
import os

def reclassify(data, bins, values):
    if np.isnan(data).any():
        data = np.nan_to_num(data, nan=-998)

    ri = np.digitize(data, bins, right=True)
    classified_data = np.array([values[r - 1] if r > 0 and r <= len(values) else -998 for r in ri.flat]).reshape(
        data.shape)

    return classified_data.astype(np.int16)  # pix 16

#env
input_dir = r"..\WFS\WFS_data_analyst_task_data"
output_dir = r"..\WFS\WFS_rasterio"

tif_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.tif', '.tiff'))]
if not tif_files:
    raise Exception("No TIFF files found in the input directory.")

raster_stack = []

for filename in tif_files:
    with rasterio.open(os.path.join(input_dir, filename)) as src:
        data = src.read(1)
        metadata = src.meta

        bins = [0.23, 0.35, 0.47, 0.59, 0.71, 0.90]
        values = [-998, 1, 2, 3, 4, 5]
        classified_data = reclassify(data, bins, values)
        raster_stack.append(classified_data)

        metadata.update(dtype=rasterio.int16, nodata=-998)
        output_path = os.path.join(output_dir, f"Classified_{filename}")
        with rasterio.open(output_path, 'w', **metadata) as dst:
            dst.write(classified_data, 1)

mean_classified = np.nanmean(np.stack(raster_stack), axis=0)

mean_bins = [1, 3.5, 4, 4.5, 4.7, 5]
mean_values = [-998, 1, 2, 3, 4, 5]
reclassified_mean_raster = reclassify(mean_classified, mean_bins, mean_values)

mean_raster_path = os.path.join(output_dir, "EVI_Classified_Mean_Reclassified.tif")
metadata.update(dtype=rasterio.int16, nodata=-998)
with rasterio.open(mean_raster_path, 'w', **metadata) as dst:
    dst.write(reclassified_mean_raster, 1)
