# https://github.com/TomSchimansky/TkinterMapView


import tkinter
import tkintermapview

# Créer une fenetre
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("Selectionner les points pour le trajet")

# Créer la map
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# set current widget position and zoom
map_widget.set_position(48.860381, 2.338594)  # Paris, France
map_widget.set_zoom(15)

# Définir l'adresse de widget 
map_widget.set_address("Saint Orens de Gameville, France")

# set current widget position by address
marker_1 = map_widget.set_address("2 Av. du Lycée, Saint-Orens-de-Gameville, France", marker=True)
marker_1.set_text("Point de départ")  # set new text
# 
# marker_1.set_position(48.860381, 2.338594)  # change position
# marker_1.delete()

# A croiser plus tard avec les data du drone
# Marqueur dans la console d'exécution
print(marker_1.position, marker_1.text)  # get position and text

#Fonction pour ajouter une points clic droit
def add_marker_event(coords):
    print("Ajouter un point:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="Nouveau point")
    
# Fonction pour afficher coordonnées dans console clic gauche
def left_click_event(coordinates_tuple):
    print("Left click event with coordinates:", coordinates_tuple)

map_widget.add_left_click_map_command(left_click_event) 

map_widget.add_right_click_menu_command(label="Add Marker",
                                        command=add_marker_event,
                                        pass_coords=True) 

# Vue sattelite google
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite


# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

map_widget.set_overlay_tile_server("http://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png")  # railway infrastructure
# Lancemement de la fenêtre
root_tk.mainloop()