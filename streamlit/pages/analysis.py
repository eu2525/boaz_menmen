import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster
import pandas as pd

st.title("음식점 어디 갈래~")

# File uploader for user to upload an Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    df = pd.read_excel(uploaded_file)
    
    # Ensure 'lat' and 'lon' columns are present, else create them
    if 'lat' not in df.columns or 'lon' not in df.columns:
        if 'lng' in df.columns:
            df['lat'] = df['lat'] if 'lat' in df.columns else None
            df['lon'] = df['lng'] if 'lng' in df.columns else None
        else:
            st.error("The uploaded file does not contain 'lat' and 'lon' or 'lng' columns.")
            st.stop()

    avg_lat = df['lat'].mean()
    avg_lon = df['lon'].mean()
    # Create a Folium map centered on a default location
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=15)

    # Add marker cluster
    marker_cluster = MarkerCluster().add_to(m)

    # Add markers to the map
    for idx, row in df.iterrows():
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=f'음식점이름 : {row["nm"]} \n category : {row["category"]}',
        ).add_to(marker_cluster)

    # Display the map in Streamlit
    folium_static(m)
else:
    st.info("Please upload an Excel file to visualize the data.")