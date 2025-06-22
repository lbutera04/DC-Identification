from shapely import LineString, Point, Polygon, MultiPolygon
import osmnx as ox
import networkx as nx
import geopandas as gpd

def fill_holes_and_dissolve(geom):
    """
    Remove interior rings and dissolve overlaps of a polygon
    Args:
        geom (shapely.Polygon, shapely.MultiPolygon): The polygon to be filled in
    Returns:
        cleaned.buffer[0] (shapely.Polygon, shapely.MultiPolygon): The cleaned polygon
    """
    if geom.geom_type == "Polygon":
        cleaned = Polygon(geom.exterior)
    elif geom.geom_type == "MultiPolygon":
        cleaned = MultiPolygon([Polygon(p.exterior) for p in geom.geoms])
    else:          
        return geom
    return cleaned.buffer(0) 

def generate_graph(region):
    """
    Generate a graph from a region
    Parameters:
        region : string
            The name of the region, formatted for ox.geocode_to_gdf()
    Outputs:
        graph : nx.MultiDiGraph
            Graph from the region's outermost polygon
    """
    geom = ox.geocode_to_gdf(region)
    graph = geom['geometry'].apply(fill_holes_and_dissolve)
    return graph

__all__ = [
    "fill_holes_and_dissolve", 
    "generate_graph",   # ← add this
]