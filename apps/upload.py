import streamlit as st
import leafmap.foliumap as leafmap
from keplergl import KeplerGl
import geopandas as gpd
from streamlit_keplergl import keplergl_static


def app():
    
    st.title("IIT Jodhpur's Hostels")

    # m = leafmap.Map()
    # in_csv = 'map (3).geojson'
    # config = 'kepler.gl.json'
    # m.add_geojson(in_csv, layer_name="hex_data")
    # m.to_streamlit(height=700)
    
    with open('map (3).geojson', 'r') as f:
        geojson = f.read()

    conf={"version":"v1","config":{"visState":{"filters":[],"layers":[{"id":"qwoaf2t","type":"geojson","config":{"dataId":"f10dsgkr8","label":"map (3)","color":[119,110,87],"highlightColor":[252,242,26,255],"columns":{"geojson":"_geojson"},"isVisible":True,"visConfig":{"opacity":0.8,"strokeOpacity":0.8,"thickness":0.5,"strokeColor":[114,12,157],"colorRange":{"name":"Custom Palette","type":"custom","category":"Custom","colors":["#184a5a","#C70039"]},"strokeColorRange":{"name":"Global Warming","type":"sequential","category":"Uber","colors":["#5A1846","#900C3F","#C70039","#E3611C","#F1920E","#FFC300"]},"radius":10,"sizeRange":[0,10],"radiusRange":[0,50],"heightRange":[0,500],"elevationScale":0.5,"enableElevationZoomFactor":True,"stroked":True,"filled":True,"enable3d":True,"wireframe":True},"hidden":False,"textLabel":[{"field":None,"color":[255,255,255],"size":18,"offset":[0,0],"anchor":"start","alignment":"center"}]},"visualChannels":{"colorField":{"name":"type","type":"string"},"colorScale":"ordinal","strokeColorField":None,"strokeColorScale":"quantile","sizeField":None,"sizeScale":"linear","heightField":{"name":"population","type":"integer"},"heightScale":"log","radiusField":None,"radiusScale":"linear"}}],"interactionConfig":{"tooltip":{"fieldsToShow":{"f10dsgkr8":[{"name":"name","format":None},{"name":"population","format":None},{"name":"type","format":None}]},"compareMode":False,"compareType":"absolute","enabled":True},"brush":{"size":0.5,"enabled":False},"geocoder":{"enabled":False},"coordinate":{"enabled":False}},"layerBlending":"normal","splitMaps":[],"animationConfig":{"currentTime":None,"speed":1}},"mapState":{"bearing":-31.714895207288237,"dragRotate":True,"latitude":26.47439658457512,"longitude":73.1150498086556,"pitch":41.778548162555424,"zoom":15.581155874629815,"isSplit":False},"mapStyle":{"styleType":"dark","topLayerGroups":{},"visibleLayerGroups":{"label":True,"road":True,"border":False,"building":True,"water":True,"land":True,"3d building":False},"threeDBuildingColor":[9.665468314072013,17.18305478057247,31.1442867897876],"mapStyles":{}}}}
    

    # map_1.add_data(data=geojson, name='geojson')

    # data=gpd.read_file('map (3).geojson')
   
    # map=KeplerGl(height=700, data={"data":data}, config=config) 
    # map.to_streamlit()
    map_1 = KeplerGl()
    map_1.add_data(data=geojson, name='geojson')
    map_1.config=conf
    keplergl_static(map_1,center_map=True)