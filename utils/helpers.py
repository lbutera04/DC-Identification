from shapely import LineString, Point, Polygon, MultiPolygon
import osmnx as ox
import networkx as nx
import geopandas as gpd

def generate_graph(region):
    geom = ox.geocode_to_gdf(region)
    if geom.geom_type == "Polygon":
        cleaned = Polygon(geom.exterior)
    elif geom.geom_type == "MultiPolygon":
        cleaned = MultiPolygon([Polygon(p.exterior) for p in geom.geoms])
    else:          
        return geom
    return cleaned.buffer(0) 