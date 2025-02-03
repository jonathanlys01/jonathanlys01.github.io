

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks.
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy


import getorg
from geopy import Nominatim

# EDIT HERE
places = [
    "Brest, France", # MSc and PhD, Internship
    "Paris, France", # Internship
    "Stuttgart, Germany", # Visit
    "Lyon, France", # Conference
    "Sydney, Australia", # Academic exchange
    "Papeete, French Polynesia", # Internship
]
# END EDIT

geocoder = Nominatim()
location_dict = {place: geocoder.geocode(place) for place in places}

m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="../visitmap", hashed_usernames=False)



