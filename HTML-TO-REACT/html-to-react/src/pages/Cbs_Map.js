import React from 'react'
import Helmet from 'react-helmet';
import { Link } from 'react-router-dom'
import './static/layout.css'

export default function Cbs_Map() {
  return (
    <React.Fragment>
      <Helmet>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet-control-geocoder/dist/Control.Geocoder.css" />
      </Helmet>
        <div id="top_tab">
          <span id="sayfamesajlari"></span>
          <div id="top_tab_opacity"></div>
        <Link to="/">
          <button type="menu" id="go_homepage">
          </button></Link>         
          <details id="create_object"><summary style={{fontSize:"small",listStyle:"none",padding:"5px",fontWeight:"bold"}}>Obje Oluştur</summary>
            <button className="button" type="menu" onclick="create_point()">Nokta</button>
            <button className="button"type="menu">Çizgi</button>
            <button className="button" type="menu">Çokgen</button></details>
          <details id="up_data"><summary style={{fontSize:"small",listStyle:"none",padding:"5px",fontWeight:"bold"}}>Vektör Veri Yükle</summary>
            <button className="button" type="menu">Shp</button>
            <button className="button"type="menu">Dwg</button>
            <button className="button" type="menu">Ncz</button>
            <button className="button" type="menu">Kml</button></details>
          <details id="down_data"><summary style={{fontSize:"small",listStyle:"none",padding:"5px",fontWeight:"bold"}}>Vektör Veri İndir</summary>
            <button className="button" type="menu">Shp</button>
            <button className="button"type="menu">Dwg</button>
            <button className="button" type="menu">Ncz</button>
            <button className="button" type="menu">Kml</button></details>
            <details id="map_services"><summary style={{fontSize:"small",listStyle:"none",padding:"5px",fontWeight:"bold"}}>Harita Servisleri</summary>
              <button className="button1" onclick="add_osm()" ondblclick="remove_osm()" type="menu">Open Street Map</button>
              <button className="button2"type="menu"  onClick="add_googlestreet()" ondblclick="remove_googlestreet()">Google Street Map</button>
              <button className="button2"type="menu"onclick="add_googlesatellite()" ondblclick="remove_googlesatellite()">Google Satellite Map</button>
              <button className="button3" type="menu" onclick="add_cardodb_darkmatter()" ondblclick="remove_cardodb_darkmatter()" >Carto Dark Matter</button>
              <button className="button4" type="menu" onclick="add_mapbox_satellite()" ondblclick="remove_mapbox_satellite()">MapBox Satellite</button>
              <button className="button4" type="menu" onclick="add_mapbox_streets()" ondblclick="remove_mapbox_streets()">MapBox Streets</button>
              <button className="button4" type="menu" onclick="add_stamen_watercolor()" ondblclick="remove_stamen_watercolor()">Stamen Watercolor</button>
              <button className="button4" type="menu" onclick="add_opentopomap()" ondblclick="remove_opentopomap()">Opentopo map</button>
              <button className="button4" type="menu" onclick="add_herev3()" ondblclick="remove_herev3()">Here Map V3</button>
              <button className="button4" type="menu" onclick="(add_jawg_map())" ondblclick="remove_jawg_map()">Jawg Map</button></details>
            <button id="button12" type="menu" onclick='map.flyTo([38.9637,35.2433],7)' style={{fontSize:"small",listStyle:"none",padding:"5px",fontWeight:"bold"}}>Haritayı Yenile</button>
        </div>
        <div id="map_view_background"></div>
        <div id="map_screen"></div>
        <div id="map_view">
          <div id="left_tabs">
            <details id="vektor"><summary id="vektor_text">Vektörler</summary>
            <div id="layers_vektor">
            </div></details>
            <details id="raster"><summary id="raster_text">Rasterlar</summary>
              <div id="layers_raster"></div></details>
          </div>
        </div>
        <div id="right_tab">
          <details id="tools_bar"><summary id="tools_text">Araçlar</summary>
          <div id="tools_tab"></div></details>
          <details id="analys"><summary id="analyst_text">Analizler</summary>
            <div id="analys_tab"></div></details>

        </div>
        <div id="coordinat_tab"></div>
        <span id="obje_girdi"></span>
        <div id="oznitelikpenceresi"></div>
        <Helmet>
        <script src="./js/cbs_map.js" type="text/javascript" />
        <script src="https://unpkg.com/react@17/umd/react.development.js" crossorigin></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js" crossorigin></script>
        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
        <script src="https://unpkg.com/leaflet-control-geocoder/dist/Control.Geocoder.js"></script>
        <script src="./js/leaflet-providers.js"></script>
        <script src="./js/maps.js"></script>
        <script src="./js/create_point.js"></script>
        </Helmet>
        </React.Fragment>
  )
}


