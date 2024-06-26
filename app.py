# -*- coding: utf-8 -*-
"""egypt_buildings_streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/kentstephen/egypt_buildings/blob/main/egypt_buildings_notebook.ipynb
Convert App from Streamlit to Gradio
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import datashader as ds
import colorcet
import duckdb
import gradio as gr

# Database connection and data retrieval
def load_data(country_iso):
    con = duckdb.connect()
    con.sql("""
        install spatial;
        load spatial;
        install httpfs;
        load httpfs;
        set s3_region='us-west-2';
    """)
    df = con.sql(f"""
        SELECT
            ST_X(ST_Centroid(ST_GeomFromWKB(geometry))) AS longitude,
            ST_Y(ST_Centroid(ST_GeomFromWKB(geometry))) AS latitude
        FROM read_parquet('s3://us-west-2.opendata.source.coop/vida/google-microsoft-open-buildings/geoparquet/by_country/country_iso={country_iso}/{country_iso}.parquet');
    """).df()
    return df

# Create a Datashader canvas and aggregate points
def create_image(df):
    cvs = ds.Canvas(plot_width=690, plot_height=800)
    agg = cvs.points(df, 'longitude', 'latitude')
    img = ds.tf.shade(agg, cmap=colorcet.fire, how='log')
    return img.to_pil()

# Gradio function that integrates data loading and image creation
def process_data(country_iso):
    df = load_data(country_iso)
    img = create_image(df)
    return img

# Set up the Gradio interface
country_iso_dropdown = gr.Dropdown(choices=["EGY", "TZA", "TUN", "MOZ", "NAM", "NER", "NGA", "RWA",
                                            "BWA", "BFA", "BDI", "CPV", "CMR", "CAF", "TCD", "COM", "COG",
                                            "DJI", "GNQ", "ERI", "SWZ", "ETH", "GAB", "SDN", "SOM", "KEN",
                                            "MDG", "ZWE", "LSO", "ZAF", "AGO", "ZMB", "COD", "SSD", "UGA",  
                                            "BEN", "TGO", "GHA", "CIV", "LBR", "SLE", "GIN", "GNB", "MLI", 
                                            "GMB", "MRT", "DZA", "MAR", "ESH", "LBY", "MWI", "MUS", "MLT"], 
                                  label="Select a country by ISO code")

interface = gr.Interface(fn=process_data,
                         inputs=country_iso_dropdown,
                         outputs="image",
                         title="Building Visualization by Country",
                         description="Select a country to visualize the geographic distribution of buildings.")
interface.launch()
