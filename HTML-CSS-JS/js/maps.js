function range(start, end) {
  return Array.from({ length: end - start + 1 }, (_, i) => i)
};

const origin = [38066.8071289063 ,3842467.31384277];
const resolutions = [(origin[1]-origin[0])/256];
var i;
for (i in range(1,17)){
    var cozunurluk = resolutions[i]/2;
    resolutions.push(cozunurluk);
};
var gecerli_koordinat = "EPSG:3857"
const koordinat_sistemleri = {
  "EPSG:3857":L.CRS.EPSG3857,
  "EPSG:2319":new L.Proj.CRS (
            "EPSG:2319",
            "+proj=tmerc +lat_0=0 +lon_0=27 +k=1 +x_0=500000 +y_0=0 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs", 
            {resolutions: resolutions,
                origin:[38066.8071289063,3842467.31384277],
                }),
  "EPSG:2320":new L.Proj.CRS (
            "EPSG:2320",
            "+proj=tmerc +lat_0=0 +lon_0=30 +k=1 +x_0=500000 +y_0=0 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs ", 
            {resolutions: resolutions,
                origin:[38066.8071289063,3842467.31384277],
                }),
  "EPSG:2321":new L.Proj.CRS (
            "EPSG:2321",
            "+proj=tmerc +lat_0=0 +lon_0=33 +k=1 +x_0=500000 +y_0=0 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs ", 
            {resolutions: resolutions,
                origin:[38066.8071289063,3842467.31384277],
                }),
  "EPSG:2322":new L.Proj.CRS (
            "EPSG:2322",
            "+proj=tmerc +lat_0=0 +lon_0=36 +k=1 +x_0=500000 +y_0=0 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs ", 
            {resolutions: resolutions,
                origin:[38066.8071289063,3842467.31384277],
                }),   
   "EPSG:2323":new L.Proj.CRS (
            "EPSG:2323",
            "+proj=tmerc +lat_0=0 +lon_0=39 +k=1 +x_0=500000 +y_0=0 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs", 
            {resolutions: resolutions,
                origin:[38066.8071289063,3842467.31384277],
                }),   
   "EPSG:2324":new L.Proj.CRS (
            "EPSG:2324",
            "+proj=tmerc +lat_0=0 +lon_0=42 +k=1 +x_0=500000 +y_0=0 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs", 
            {resolutions: resolutions,
                origin:[38066.8071289063,3842467.31384277],
                }),       
   "EPSG:2325":new L.Proj.CRS (
            "EPSG:2325",
            "+proj=tmerc +lat_0=0 +lon_0=45 +k=1 +x_0=500000 +y_0=0 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs", 
            {resolutions: resolutions,
                origin:[38066.8071289063,3842467.31384277],
                }),
   "EPSG:7931":new L.Proj.CRS (
            "EPSG:7931",
            "+proj=tmerc +lat_0=0 +lon_0=27 +k=1 +x_0=500000 +y_0=0 +ellps=GRS80 +units=m +no_defs", 
            {resolutions: resolutions,
                origin:[38066.8071289063,3842467.31384277],
                }),                 
}
function koordinat_degistirme(i){
  var i = i

  if (i==="EPSG:3857"){
    gecerli_koordinat="EPSG:3857"
  }
}

//harita ekranının oluşturulması
var map
function map_create(i){
  if (i==="EPSG:3857"){
      map = L.map('map_screen',{
              center: [38.9637,35.2433],
              zoom: 7,
              zoomControl: false,
              drawControl: true,
            })
    }
}

//draw geommety 

  // harita çeşitleri
    var osm_map = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      });
    var googlestreets =L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
      maxZoom: 20,
      subdomains:['mt0','mt1','mt2','mt3']
   });
    var mapbox_satellite = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 18,
      id: 'mapbox/satellite-v9',
      tileSize: 512,
      zoomOffset: -1,
      accessToken: 'pk.eyJ1IjoiYmlsYWxiZW56ZXIiLCJhIjoiY2wxM3QwanJwMDk0ZTNwbHFrdXNsc215aiJ9.cpvdEZ1Dv8cmWASBnyvnag'
  });
    var mapbox_streets = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 18,
      id: 'mapbox/streets-v11',
      tileSize: 512,
      zoomOffset: -1,
      accessToken: 'pk.eyJ1IjoiYmlsYWxiZW56ZXIiLCJhIjoiY2wxM3QwanJwMDk0ZTNwbHFrdXNsc215aiJ9.cpvdEZ1Dv8cmWASBnyvnag'
  });
    var CartoDB_DarkMatter = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
  subdomains: 'abcd',
      maxZoom: 19
  });
    var googlesatellite = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
     maxZoom: 20,
     subdomains:['mt0','mt1','mt2','mt3']
   });
    var Stamen_Watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
   attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  subdomains: 'abcd',
  minZoom: 1,
  maxZoom: 16,
  ext: 'jpg'
  });
    var OpenTopoMap = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      maxZoom: 20,
      attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });
    var herev3 = L.tileLayer.provider('HEREv3.terrainDay', {
      apiKey: 'pwF1Xj9Xob7B_oRW2xgQVJ65gC21q0hfaLpbBRWWMnc'
  });
    var jawg_map = L.tileLayer.provider('Jawg.Streets', {
      variant: '',
      accessToken: 'wpnsRT419zEQ9XTokJabanKEDLmSbNI6J3b4suZiYVwQgOQgDUvbj9v7WTMer2aT'
  });
  
  
  //harita çeşitlerinin nesnede belirtilmesi ( fonksiyonlar için)
  const maps_for_leaflet = {
    "OpenStreetMap":osm_map,
    "GoogleStreetsMap":googlestreets,
    "GoogleSatelliteMap":googlesatellite,
    "Mapbox Satellite":mapbox_satellite,
    "Mapbox Streets":mapbox_streets,
    "CartoDbDarkMatter":CartoDB_DarkMatter,
    "WatStamenercolor":Stamen_Watercolor,
    "Open Topo Map":OpenTopoMap,
    "herev3":herev3,
    "jawg map":jawg_map};
  // farklı haritaları yükleme fonksiyonları
  function add_opentopomap(){
    for (var i in maps_for_leaflet) {
      if (i === "Open Topo Map"){
        maps_for_leaflet[i].addTo(map);
        continue;}
      maps_for_leaflet[i].remove(map);
    }
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="unset";
  }
  function  remove_opentopomap(){
    OpenTopoMap.remove(map);
  
    document.getElementById('map_screen').style.backgroundColor="white";
  }
  function add_stamen_watercolor() {
    for (var i in maps_for_leaflet) {
      if (i === "WatStamenercolor"){
        maps_for_leaflet[i].addTo(map);
        continue;}
      maps_for_leaflet[i].remove(map);
    }
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="unset";
  }
  function remove_stamen_watercolor() {
    Stamen_Watercolor.remove(map);
    document.getElementById('map_screen').style.backgroundColor="white";
  }
  function add_osm() {
    for (var i in maps_for_leaflet) {
      if (i === "OpenStreetMap"){
        maps_for_leaflet[i].addTo(map);
        continue;}
      maps_for_leaflet[i].remove(map);
    }
  
    document.getElementById('map_screen').style.backgroundColor="unset";
  }
  function remove_osm() {
    osm_map.remove(map);
  
    document.getElementById('map_screen').style.backgroundColor="white";
  }
  function add_googlestreet() {
    for (var i in maps_for_leaflet) {
      if (i === "GoogleStreetsMap"){
        maps_for_leaflet[i].addTo(map);
        continue;}
      maps_for_leaflet[i].remove(map);
    }
    document.getElementById('map_screen').style.backgroundColor="unset";
    document.getElementById('map_screen').style.opacity = 1;
  }
  function remove_googlestreet() {
    googlestreets.remove(map);
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="white";
   }
  function add_googlesatellite() {
    for (var i in maps_for_leaflet) {
      if (i === "GoogleSatelliteMap"){
        maps_for_leaflet[i].addTo(map);
        continue;}
      maps_for_leaflet[i].remove(map);
    }
    document.getElementById('map_screen').style.backgroundColor="unset";
    document.getElementById('map_screen').style.opacity = 1;
  }
  function remove_googlesatellite() {
    googlesatellite.remove(map);
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="white";
   }
  function add_mapbox_satellite() {
    for (var i in maps_for_leaflet) {
      if (i === "Mapbox Satellite"){
        maps_for_leaflet[i].addTo(map);
        continue;}
      maps_for_leaflet[i].remove(map);
    }
    document.getElementById('map_screen').style.backgroundColor="unset";
    document.getElementById('map_screen').style.opacity = 1;
  }
  function remove_mapbox_satellite(){
    mapbox_satellite.remove(map);
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="white";
  }
  function add_mapbox_streets() {
    for (var i in maps_for_leaflet) {
      if (i === "Mapbox Streets"){
        maps_for_leaflet[i].addTo(map);
        continue;}
      maps_for_leaflet[i].remove(map);
    }
    document.getElementById('map_screen').style.opacity = 1;
    
    document.getElementById('map_screen').style.backgroundColor="unset";
  }
  function remove_mapbox_streets(){
    mapbox_streets.remove(map);
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="white";
  }
  function add_cardodb_darkmatter(){
    for (var i in maps_for_leaflet) {
      if (i === "CartoDbDarkMatter"){
        maps_for_leaflet[i].addTo(map);
        continue;}
      maps_for_leaflet[i].remove(map);
    }
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="unset";
  }
  function remove_cardodb_darkmatter(){
    CartoDB_DarkMatter.remove(map);
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="white";
  }
  function add_herev3(){
    for (var i in maps_for_leaflet) {
      if (i === "herev3"){
        maps_for_leaflet[i].addTo(map);
        continue;}
      maps_for_leaflet[i].remove(map);
    }
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="unset";
  }
  function remove_herev3(){
    herev3.remove(map);
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="white";
  }
  function add_jawg_map(){
    for (var i in maps_for_leaflet) {
      if (i === "jawg map"){
        maps_for_leaflet[i].addTo(map);
        continue;}
      maps_for_leaflet[i].remove(map);
    }
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="unset";
  }
  function remove_jawg_map(){
    jawg_map.remove(map);
    document.getElementById('map_screen').style.opacity = 1;
    document.getElementById('map_screen').style.backgroundColor="white";
  }
  
  // Haritanın Sol Alt Köşesinde Koordinat Gösterme
function show_coordints() {
    
  if (gecerli_koordinat==="EPSG:3857"){
    map_create(gecerli_koordinat)
      map.on('mousemove' , (e) =>{
        document.getElementById('coordinat_tab').innerText ="Enlem:"+(e.latlng.lat).toFixed(8) +"------"+ "Boylam:"+(e.latlng.lng).toFixed(8);
        });
        document.getElementById("crssummary").innerText="WGS 84/ World Mercator (EPSG:3857)"
        koordinat_degistirme("EPSG:3857")}
        
      }

      