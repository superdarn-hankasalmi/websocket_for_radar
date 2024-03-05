import geojson
import os
import pydarn
from datetime import datetime
import sys
import matplotlib.pyplot as plt

def make_geojson(stid,nbeams,ngates):

    date = datetime.now()
    #FOV = pydarn.radar.radFov.fov(site=site, rsep=rsep, ngates=ngates, nbeams=nbeams, coords = 'geo', date_time=date)
    FOV = pydarn.radar_fov(stid, coords='geo')
    lat = FOV[0]
    lon = FOV[1]
    #print(FOV[0])
    #print(len(FOV[0]), len(ngates))

    polys = []
    cs = []

    coords =[]
    for gate in range(ngates):
        coords.append((lon[gate,0],lat[gate,0]))
    
    for beam in range(nbeams):
        coords.append((lon[ngates,beam],lat[ngates,beam]))

    for gate in range(ngates, 0, -1):
        coords.append((lon[gate,nbeams],lat[gate,nbeams]))
        
    for beam in range(nbeams, 0, -1):
        coords.append((lon[0,beam],lat[0,beam]))
    
    
    coords.append((lon[0,0],lat[0,0]))
    polys.append(geojson.Feature(geometry=geojson.Polygon([coords]),id=str(stid)+"_fan"))
    
    
    featureCollection = geojson.FeatureCollection(polys)
    # Prints True if a valid collection
    validation = featureCollection.is_valid
    print(validation)

    return featureCollection

def main():
	radar = sys.argv[1]
	nbeams = int(sys.argv[2])
	ngates = int(sys.argv[3])

	stid = pydarn.read_hdw_file(radar).stid
	print(radar)
	#site = pydarn.radar.site(radId=radId, dt=date)

	#myFov_15km = pydarn.radar.radFov.fov(site=site, rsep=15, ngates=ngates, nbeams=nbeams, coords = 'geo', date_time=date)
	#myFov_45km = pydarn.radar.radFov.fov(site=site, rsep=45, ngates=ngates, nbeams=nbeams, coords = 'geo', date_time=date)

	#geo_15km = make_geojson(stid, nbeams,ngates)
	geo_45km = make_geojson(stid, nbeams,ngates)

	#filename_1 = radar + "geojson_15km.json"
	filename_2 = radar + "FANgeojson_45km.json"

	#with open(filename_1,'w') as outfile:
	#	geojson.dump(geo_15km,outfile)

	with open(filename_2,'w') as outfile:
		geojson.dump(geo_45km,outfile)

if __name__ == "__main__":
	main()
