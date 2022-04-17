import React, { Component } from 'react'

export class UstSekme extends Component {
  render() {
    return (
        <div id="top_tab">
            <span id="sayfamesajlari"></span>
            <div id="top_tab_opacity"></div>
            <button type="menu" id="go_homepage"></button>
            <details id="create_object"><summary style={{fontSize:"small",listStyle:"none",padding:"5px",fontWeight:"bold"}}>Obje Oluştur</summary>
                <button className="button" type="menu" onclick="create_point()">Nokta</button>
                <button className="button"type="menu">Çizgi</button>
                <button className="button" type="menu">Çokgen</button>
            </details>
            <details id="up_data"><summary style={{fontSize:"small",listStyle:"none",padding:"5px",fontWeight:"bold"}} >Vektör Veri Yükle</summary>
                <button className="button" type="menu">Shp</button>
                <button className="button"type="menu">Dwg</button>
                <button className="button" type="menu">Ncz</button>
                <button className="button" type="menu">Kml</button>
            </details>
            <details id="down_data"><summary style={{fontSize:"small",listStyle:"none",padding:"5px",fontWeight:"bold"}}>Vektör Veri İndir</summary>
                <button className="button" type="menu">Shp</button>
                <button className="button"type="menu">Dwg</button>
                <button className="button" type="menu">Ncz</button>
                <button className="button" type="menu">Kml</button>
            </details>
            <details details id="map_services"><summary style={{fontSize:"small",listStyle:"none",padding:"5px",fontWeight:"bold"}}>Harita Servisleri</summary>
                <button className="button1" onclick="add_osm()" ondblclick="remove_osm()" type="menu">Open Street Map</button>
                <button className="button2"type="menu"onclick="add_googlestreet()" ondblclick="remove_googlestreet()">Google Street Map</button>
                <button className="button2"type="menu"onclick="add_googlesatellite()" ondblclick="remove_googlesatellite()">Google Satellite Map</button>
                <button className="button3" type="menu" onclick="add_cardodb_darkmatter()" ondblclick="remove_cardodb_darkmatter()" >Carto Dark Matter</button>
                <button className="button4" type="menu" onclick="add_mapbox_satellite()" ondblclick="remove_mapbox_satellite()">MapBox Satellite</button>
                <button className="button4" type="menu" onclick="add_mapbox_streets()" ondblclick="remove_mapbox_streets()">MapBox Streets</button>
                <button className="button4" type="menu" onclick="add_stamen_watercolor()" ondblclick="remove_stamen_watercolor()">Stamen Watercolor</button>
                <button className="button4" type="menu" onclick="add_opentopomap()" ondblclick="remove_opentopomap()">Opentopo map</button>
                <button className="button4" type="menu" onclick="add_herev3()" ondblclick="remove_herev3()">Here Map V3</button>
                <button className="button4" type="menu" onclick="add_jawg_map()" ondblclick="remove_jawg_map()">Jawg Map</button>
            </details>
            <button id="button12" type="menu" onclick='map.flyTo([38.9637,35.2433],7)' style={{fontSize:"small",listStyle:"none",padding:"5px",fontWeight:"bold"}}>Haritayı Yenile</button>
        </div>
    )
  }
}

export default UstSekme