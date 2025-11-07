import geopandas as gpd
import pandas as pd
from Z1_files import sumds_file # import pliku na którym pracujemy

df = sumds_file() # plik na którym pracujemy

def list_of_voivodeships():
    voivo = df['Województ'].unique()
    return voivo
print(list_of_voivodeships()) # bo jest return!!!

def list_of_counties_in_voivodeship():
    counties = df['Powiat'].unique()
    i = 1
    for county in counties:
        print(f'{i}. {county}')
        i += 1





