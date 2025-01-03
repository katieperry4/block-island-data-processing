import rasterio
import numpy as np
import json
import gzip


def elevation_to_color(elev):
    if elev < 0:
        return [0,0,255] #blue
    elif elev < 50:
        return [0,255,0] #green
    elif elev <= 150:
        return [255,255,0] #yellow
    else:
        return [255,0,0] #red
    
file_path = 'BLGeotiff.tif'
output_path = "elevation_data1.json"
try:
    dataset = rasterio.open(file_path)
    elevation = dataset.read(1)
    transform = dataset.transform

    downsample_factor = 100
    elevation_downsampled = elevation[::downsample_factor, ::downsample_factor]

    data_points = []

    #rows, cols = elevation_downsampled.shape
    for row in range(elevation_downsampled.shape[0]):
        for col in range(elevation_downsampled.shape[1]):
            elev = elevation_downsampled[row,col]
            if elev != dataset.nodata:
                x, y = rasterio.transform.xy(transform, row * downsample_factor, col * downsample_factor)
                color = elevation_to_color(elev)
                data_points.append({"x" : x, "y" : y, "elevation": float(elev), "color" : color})

    with open(output_path, 'w') as json_file:
        json.dump(data_points, json_file)

    print(f"Downsampling and processing complete, data saved to {output_path}")

except Exception as e:
    print(f"error: {e}")

