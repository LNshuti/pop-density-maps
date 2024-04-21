# -*- coding: utf-8 -*-
"""egypt_buildings_streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/kentstephen/egypt_buildings/blob/main/egypt_buildings_notebook.ipynb
"""

# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import datashader as ds
import colorcet
import duckdb

# Initialize Streamlit app
st.title("Building Visualization by Country")

# Country selection dropdown
country_iso = st.selectbox("Select a country by ISO code",
                            ["SLV", "EGY", "TZA", "TUN","MOZ", "NAM", "NER", "NGA", "RWA",
                             "BWA", "BFA", "BDI", "CPV", "CMR", "CAF", "TCD", "COM", "COG",
                            "DJI", "GNQ", "ERI", "SWZ", "ETH", "GAB", "SDN", "SOM", "KEN",
                            "MDG", "ZWE", "LSO", "ZAF", "AGO", "ZMB", "COD", "SSD"]
                         )

# Database connection and data retrieval
@st.cache_data
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

df = load_data(country_iso)

# Create a Datashader canvas and aggregate points
@st.cache_data
def create_image(df):
    cvs = ds.Canvas(plot_width=690, plot_height=800)
    agg = cvs.points(df, 'longitude', 'latitude')
    img = ds.tf.shade(agg, cmap=colorcet.fire, how='log')
    return img

img = create_image(df)

# Convert the Datashader image to a NumPy array and display it
fire_cmap = LinearSegmentedColormap.from_list("fire", colorcet.fire)
img_np = np.array(img.to_pil())

fig, ax = plt.subplots(figsize=(6.9, 8), facecolor='black')
ax.imshow(img_np, cmap=fire_cmap)
ax.axis('off')
plt.tight_layout()

# Show the plot in Streamlit
st.pyplot(fig)
