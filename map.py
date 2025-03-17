import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load school dataset from Excel
schools = pd.read_excel("/Users/prabhpreet16/Desktop/aparna-assignment/School_Profile_Data.xlsx")  # Replace with actual filename

# Aggregate school count per state
state_counts = schools.groupby("State").size().reset_index(name="Number of Schools")

# Load India state shapefile (Use a clean version without district lines)
india_map = gpd.read_file("/Users/prabhpreet16/Downloads/gadm41_IND_shp/gadm41_IND_1.shp")  # Replace with actual shapefile path

# Merge school data with map
india_map = india_map.merge(state_counts, left_on="NAME_1", right_on="State", how="left")

# Fill missing values (states with no schools will have 0)
india_map["Number of Schools"] = india_map["Number of Schools"].fillna(0)

# Get state centroids for placing circles
india_map["coords"] = india_map["geometry"].centroid
india_map["Longitude"] = india_map["coords"].apply(lambda p: p.x)
india_map["Latitude"] = india_map["coords"].apply(lambda p: p.y)

# Create a clean map with Cartopy
fig, ax = plt.subplots(figsize=(10, 12), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([68, 98, 6, 38])  # India extent

# Add natural earth background map
ax.add_feature(cfeature.LAND, color="lightgrey")
ax.add_feature(cfeature.BORDERS, linestyle="-", linewidth=0.8)

# Plot India states
india_map.boundary.plot(ax=ax, color="black", linewidth=0.6)

# Scatter plot circles for states
scatter = ax.scatter(
    india_map["Longitude"], india_map["Latitude"],
    s=india_map["Number of Schools"] * 50,  # Scale circle size
    color="red", alpha=0.6, edgecolors="black"
)

# Label states with school numbers
for i, row in india_map.iterrows():
    if row["Number of Schools"] > 0:
        ax.text(row["Longitude"], row["Latitude"], row["State"], fontsize=9, ha="right")

# Add legend for circle size
sizes = [5, 10, 20]  # Example school numbers
for size in sizes:
    plt.scatter([], [], s=size * 50, color="red", label=f"{size} Schools")

plt.legend(title="Number of Schools", loc="upper right")
plt.title("SmartBox Program - Schools per State")
plt.show()
