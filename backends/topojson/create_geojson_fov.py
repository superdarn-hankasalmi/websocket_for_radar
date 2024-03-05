import geojson
import os
import pydarn
from datetime import datetime
import sys

def make_geojson(stid,nbeams,ngates):

    date = datetime.now()
    #FOV = pydarn.radar.radFov.fov(site=site, rsep=rsep, ngates=ngates, nbeams=nbeams, coords = 'geo', date_time=date)
    FOV = pydarn.radar_fov(stid, coords='geo')
    lat = FOV[0]
    lon = FOV[1]

    polys = []
    cs = []
    reversedWinding = [4,11,12,13,14,15,18,24,21,97]
    if stid in reversedWinding:
        print(stid, 'reverse!')
        for beam in range(nbeams):
            for gate in range(ngates):
                coords = []
                # TAKE NOTE OF WINDING ORDER! If they dont work, swap the 2nd and 4th rows.
                #print beam, gate,myFov.latFull[beam,gate],myFov.latFull[beam+1,gate],myFov.latFull[beam,gate+1], myFov.latFull[beam+1,gate+1],myFov.lonFull[beam,gate],myFov.lonFull[beam+1,j],myFov.lonFull[i,j+1], myFov.lonFull[i+1,gate+1]
                coords.append((lon[gate,beam],lat[gate,beam]))
                coords.append((lon[gate, beam+1],lat[gate,beam+1]))
                coords.append((lon[gate+1, beam+1],lat[gate+1, beam+1]))
                coords.append((lon[gate+1, beam],lat[gate+1, beam]))
                coords.append((lon[gate, beam],lat[gate, beam]))

                polys.append(geojson.Feature(geometry=geojson.Polygon([coords]),id=str(beam).zfill(2)+str(gate).zfill(2)))
    else:
        for beam in range(nbeams):
            for gate in range(ngates):
                coords = []
                # TAKE NOTE OF WINDING ORDER! If they dont work, swap the 2nd and 4th rows.
                #print beam, gate,myFov.latFull[beam,gate],myFov.latFull[beam+1,gate],myFov.latFull[beam,gate+1], myFov.latFull[beam+1,gate+1],myFov.lonFull[beam,gate],myFov.lonFull[beam+1,j],myFov.lonFull[i,j+1], myFov.lonFull[i+1,gate+1]
                coords.append((lon[gate,beam],lat[gate,beam]))
                coords.append((lon[gate+1, beam],lat[gate+1, beam]))
                coords.append((lon[gate+1, beam+1],lat[gate+1, beam+1]))
                coords.append((lon[gate, beam+1],lat[gate,beam+1]))
                coords.append((lon[gate, beam],lat[gate, beam]))

                polys.append(geojson.Feature(geometry=geojson.Polygon([coords]),id=str(beam).zfill(2)+str(gate).zfill(2)))

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
    filename_2 = radar + "geojson_45km.json"

    #with open(filename_1,'w') as outfile:
    #	geojson.dump(geo_15km,outfile)

    with open(filename_2,'w') as outfile:
        geojson.dump(geo_45km,outfile)

if __name__ == "__main__":
	main()

