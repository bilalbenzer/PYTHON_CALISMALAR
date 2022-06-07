
function multi_create_point(){
    document.getElementById("oznitelikpenceresi").innerHTML="";
    var tekdongu=[1];
    //Sayfa Mesajlarında Çizime Başlamaya Dair Bildiri
    document.getElementById('sayfamesajlari').innerText="Çizime Başlayabilirsiniz.\nHome: Koordinat Gir\nEnd: Bitir";
    document.getElementById('sayfamesajlari').style.backgroundColor  = "black";
    var name = "multipoint"+(new Date()).getMilliseconds()+Math.floor(Math.random()*1000);//benzersiz id alma
    //harita üzerinde tıklama olayı ile koordinat almanın etkinleştirilmesi
    map.on('click', (e)=>{
    x = (e.latlng.lat).toFixed(8);
    y = (e.latlng.lng).toFixed(8);
    // oluşturulacak point için benzersiz bir id üretilir ve daha önceden bu id verilmiş mi kontrol edilir
    var as;
    for (as in tekdongu ){ 
      if ((typeof window[name])!=="object"){  //id in daha önceden var olup olmadığının kontrolü
          document.getElementById("vektor").open = true
          document.getElementById('sayfamesajlari').style.backgroundColor  = "black"; 
          var name2 = "point"+(new Date()).getMilliseconds()+Math.floor(Math.random()*1000);//benzersiz obje id alma
          window[name]= new multi_point(x_coordinats=x,y_coordinats=y,object_name=name2); //objenin oluşturulması
          window[name].point_ekle(window[name].object_name)
          document.getElementById('sayfamesajlari').innerText="Point oluşturuldu \n"+"E="+x+"   "+"B="+y;//sayfa mesajlarında objenin oluştuğuna dair bilgi
          var a = window[name].object_id_list.includes(name2)
          console.log(a)
        }
      else if ((typeof window[name])=="object" && (window[name].geojsonfutures.length > 0)) {
        document.getElementById("vektor").open = true
        document.getElementById('sayfamesajlari').style.backgroundColor  = "black"; 
        var name2 = "point"+(new Date()).getMilliseconds()+Math.floor(Math.random()*1000);//benzersiz obje id alma
        if (window[name].object_id_list.includes(name2)===true){
          alert("tekrar deneyiniz")}
        else{
          window[name].point_ekle(x_coordinats,y_coordinats,object_name=name2)
        }
      }
      else{
        alert("Bu İd'ye Sahip Bir Obje Bulunmakta.");   
           }}});
     // klavye kısayollarının etkinleştirilmesi
    document.addEventListener('keydown', function abc(event)  {
    var code = event.code;
      // home tuşunun basılması durumunda elle korodinat girme fonksiyonu çalıştırılır
    if (code==="Home"){
    document.getElementById('obje_girdi').style.backgroundColor = "black";
    document.getElementById('obje_girdi').innerHTML='<label for="xbuton">E :</label><input type="number" maxlength="999999" id="xbuton" step="0.001" value="" required><br><label for="ybuton">B :</label><input type="number" maxlength="999999" id="ybuton" step="0.001" value="" required><input id="koordinatal" type="submit"  value="nokta oluştur">';
    document.getElementById("koordinatal").setAttribute("onclick","koordinatileolustur('"+"olustur"+"')")
    document.removeEventListener("keydown",abc)
    }
    // end tuşuna basılması durumunda nokta oluşturma işlemi tamamlanır
    else if (code==="End") {
    document.getElementById('sayfamesajlari').style.backgroundColor = "black";
    document.getElementById('sayfamesajlari').innerText = "İşlem Tamamlandı";
    document.removeEventListener("keydown",abc)
    bekleme();
    }
    });
  }

  class multi_point {
    constructor(x_coordinats,y_coordinats,object_name){
        var random_name = object_name+"merhaba"
        this.random_name = {     //--->objenin öznitelik bilgilerinin tutulduğu nesne
            "featureid":object_name,
            "Geometri Tipi":"Nokta",
            "X Koordinatı(Enlem)":parseFloat(x_coordinats),
            "Y Koordinatı(Boylam)":parseFloat(y_coordinats),
          };
        this.object_name= 
            { //öznenin geometri tipi, öznitelikleri ve koordinatlarının tutulduğu nesne(leaflet bu nesneyi haritaya ekler)
            "type": "Feature",
            "properties": this.random_name,
            "geometry":{
              "type":"Point",
              "coordinates":[y_coordinats,x_coordinats]}}
        
        this.geojsonfutures=[this.object_name]
        this.object_id_list = [object_name]
        console.log(this.object_id_list)
        console.log(this.geojsonfutures)
    }
    point_ekle(x_coordinats,y_coordinats,object_name){
      this.object_id_list.push(object_name)
      this.geojsonfutures.push({
        "type":"Feature",
        "properties":{"featureid":object_name,
                      "Geometri Tipi":"Nokta",
                      "X Koordinatı(Enlem)":parseFloat(x_coordinats),
                      "Y Koordinatı(Boylam)":parseFloat(y_coordinats)},
        "geometry":{
            "type":"Point",
            "coordinates":[y_coordinats,x_coordinats]        }
      })
    }
    
  }
