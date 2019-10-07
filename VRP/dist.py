import networkx as nx
import osmnx as ox
import folium
#ox.plot_shape(ox.project_gdf(city))
G = ox.graph_from_place('Cracow, Poland', network_type='drive')
orig_node = ox.get_nearest_node(G, (50.067048, 19.906700))
dest_node = ox.get_nearest_node(G, (50.060139, 19.899624))
dest_node2 = ox.get_nearest_node(G, (50.073139, 19.849624))

# find the route between these nodes then plot it
route1 = nx.shortest_path(G, orig_node, dest_node, weight='length')
route2 = nx.shortest_path(G, dest_node, dest_node2, weight='length')
print(route1)
print(route2)
print(route1+route2)
CRACOW_CENTRE = {"CRACOW": [50.061681, 19.938104]}
m = folium.Map(location=[CRACOW_CENTRE["CRACOW"][0], CRACOW_CENTRE["CRACOW"][1]],
            zoom_start=15, control_scale=True)
ox.plot_route_folium(G, route1, route_width=3, route_map= m, route_color='#AA1111', tiles='Stamen Terrain', popup_attribute='name')
ox.plot_route_folium(G, route2, route_width=3, route_map= m, route_color='blue', tiles='Stamen Terrain', popup_attribute='name')
m.save("graph.html")
#route distance in meters
print(nx.shortest_path_length(G, orig_node, dest_node, weight='length'))


