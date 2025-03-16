# Leaflet cluster map of talk locations
#
# Run this from the _talks/ directory, which contains .md files of all your
# talks.This scrapes the location YAML field from each .md file, geolocates it
# with geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# #talkmap Jupyter notebook.
import frontmatter
import os
import time

import getorg
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

# EDIT HERE
places = [
    "IMT Atlantique, Brest, France",  # MSc and PhD, Internship
    "Criteo, Paris, France",  # Internship
    "Hedelfinger Str. 61, 70327 Stuttgart, Germany",  # Visit
    "Centre de Congrès de Lyon, Lyon, France",  # Conference
    "University of Technology Sydney, Sydney, Australia",  # Academic exchange
    "Service de l'Informatique, Papeete, French Polynesia",  # Internship
]
# END EDIT

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
for place in places:
    location = geocoder.geocode(place)
    location_dict[place] = location
    print((place, location.latitude, location.longitude))
    time.sleep(1)

m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)

print("written to", os.path.abspath("talkmap"))
