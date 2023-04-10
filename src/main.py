import os
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon


rev_url="https://donnees.montreal.ca/dataset/8a4bf03c-dff6-4add-b58b-c38954b0ed0d/resource/8ad67029-cf2e-49ae-a4b6-20d31611ab6e/download/reseau-express-velo.geojson"
parks_url="https://donnees.montreal.ca/dataset/2e9e4d2f-173a-4c3d-a5e3-565d79baa27d/resource/35796624-15df-4503-a569-797665f8768e/download/espace_vert.json"
bikepath_url="https://donnees.montreal.ca/dataset/5ea29f40-1b5b-4f34-85b3-7c67088ff536/resource/0dc6612a-be66-406b-b2d9-59c9e1c65ebf/download/reseau_cyclable.geojson"
fountains_url="https://donnees.montreal.ca/dataset/3ff400f3-63cd-446d-8405-842383377fb8/resource/26659739-540d-4fe2-8107-5f35ab7e807c/download/fontaine_eau_potable_v2018.csv"
greenstreets_url="https://data.montreal.ca/dataset/ab3ce7bb-09a7-49d7-8f76-461ed4c39937/resource/15883136-0180-4061-9860-d7ce3d46c73c/download/ruelles-vertes.geojson"
urbanfurnitures_url="https://donnees.montreal.ca/dataset/fb04fa09-fda1-44df-b575-1d14b2508372/resource/65766e31-f186-4ac9-9595-bfcf47ae9158/download/mobilierurbaingp.geojson"
externinstallation_url="https://donnees.montreal.ca/dataset/60850740-dd83-47ee-9a19-13d674e90314/resource/2dac229f-6089-4cb7-ab0b-eadc6a147d5d/download/terrain_sport_ext.json"


fountains = pd.read_csv(fountains_url)
fountains.columns = fountains.columns.str.lower()

fountains = gpd.GeoDataFrame(fountains, geometry=gpd.points_from_xy(fountains.longitude, fountains.latitude))
fountains = fountains.filter(["id", "geometry"])

print(fountains)