
function multi_create_point(){
    document.getElementById("oznitelikpenceresi").innerHTML="";
    var tekdongu=[1];
    //Sayfa Mesajlarında Çizime Başlamaya Dair Bildiri
    document.getElementById('sayfamesajlari').innerText="Çizime Başlayabilirsiniz.\nHome: Koordinat Gir\nEnd: Bitir";
    document.getElementById('sayfamesajlari').style.backgroundColor  = "black";
    sureli_bekletme(2000)
    var name = "multipoint"+(new Date()).getMilliseconds()+Math.floor(Math.random()*1000);//benzersiz id alma
    if ((typeof window[name])!=="object"){
        document.getElementById('sayfamesajlari').style.backgroundColor  = "black";
        document.getElementById('sayfamesajlari').innerText="Çoklu Point Katmanı oluşturuldu\n"+name;//sayfa mesajlarında objenin oluştuğuna dair bilgi
      }
    //harita üzerinde tıklama olayı ile koordinat almanın etkinleştirilmesi
    map.on('click', (e)=>{
    x = (e.latlng.lat).toFixed(8);
    y = (e.latlng.lng).toFixed(8);
    // oluşturulacak point için benzersiz bir id üretilir ve daha önceden bu id verilmiş mi kontrol edilir
      if ((typeof window[name])!=="object"){  //id in daha önceden var olup olmadığının kontrolü
          
          document.getElementById("vektor").open = true //katman penceresi sürekli açık olacak
          document.getElementById('sayfamesajlari').style.backgroundColor  = "black"; 
          var name2 = "point"+(new Date()).getMilliseconds()+Math.floor(Math.random()*1000);//benzersiz obje id alma
          window[name]= new multi_point(x_coordinats=x,y_coordinats=y,object_name=name2,class_name=name); //alınan koordinat ve alınan rastgele obje adına göre çoklu point sınıfı oluşturulur
          document.getElementById('sayfamesajlari').innerText="Point oluşturuldu \n"+"E="+x+"   "+"B="+y;//sayfa mesajlarında objenin oluştuğuna dair bilgi
          window[name].menuleriolustur()
          window[name].haritayaekle(window[name].object_stil[window[name2].bicim])
        }
      else if ((typeof window[name])=="object" && (window[name].geojsonfutures.length > 0)) {
        document.getElementById("vektor").open = true
        document.getElementById('sayfamesajlari').style.backgroundColor  = "black"; 
        var name2 = "point"+(new Date()).getMilliseconds()+Math.floor(Math.random()*1000);//benzersiz obje id alma
        if (window[name].object_id_list.includes(name2)===true){
            alert("tekrar deneyiniz")}
        else{
            window[name].point_ekle(x_coordinats=x,y_coordinats=y,object_name=name2)
            window[name].haritayaekle(object_stil[window[name2].bicim])
            console.log(window[name].geojsonfutures)
        }
        }
      else{
        alert("Bu İd'ye Sahip Bir Obje Bulunmakta.");   
           }});
     // klavye kısayollarının etkinleştirilmesi
    document.addEventListener('keydown', function abc(event)  {
    var code = event.code;
      // home tuşunun basılması durumunda elle korodinat girme fonksiyonu çalıştırılır
    if (code==="Home"){
    document.getElementById('obje_girdi').style.backgroundColor = "black";
    document.getElementById('obje_girdi').innerHTML='<label for="xbuton">E :</label><input type="number" maxlength="999999" id="xbuton" step="0.001" value="" required><br><label for="ybuton">B :</label><input type="number" maxlength="999999" id="ybuton" step="0.001" value="" required><input id="koordinatal" type="submit"  value="nokta oluştur">';
    document.getElementById("koordinatal").setAttribute("onclick","koordinatileolustur('"+"olustur"+"')")
    document.removeEventListener("keydown",abc)
    map.off('click');
    }
    // end tuşuna basılması durumunda nokta oluşturma işlemi tamamlanır
    else if (code==="End") {
    document.getElementById('sayfamesajlari').style.backgroundColor = "black";
    document.getElementById('sayfamesajlari').innerText = "İşlem Tamamlandı";
    document.removeEventListener("keydown",abc)
    bekleme();
    map.off('click');
    }
    });
  }

  class multi_point {
    constructor(x_coordinats,y_coordinats,object_name,class_name){
        var random_name = object_name+".."  //obje ad
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
        this.id_nosu = class_name 
        this.geojsonfutures=[this.object_name]
        this.object_id_list = [object_name]
        var x = class_name.toString()
        window[x]
        console.log(window[x])

        this.object_stil = [window[class_name]]
        
        this.object_stil[window[class_name].bicim]
        this.objeler_ozellikleri=[
                this.object_stil]
        console.log(this.objeler_ozellikleri)
        console.log(this.geojsonfutures)
    }
    point_ekle(x_coordinats,y_coordinats,object_name){

      window[object_name] =  {bicim:{radius: 8,
        fillColor: renk_listesi[Math.floor(Math.random()*renk_listesi.length)], //her oluşan obje bu algoritma ile rastgele bir renk alır
        color: "#000",  //dış çizginin renki
        weight: 1,  //dış çizginin kalınlığı
        opacity: 3, //dış çizginin opaklığı
        fillOpacity: 0.8},
        ikon:{ //objenin sembol ayarları bu nesneye gider
          iconUrl:null,
          iconSize:[50,50],
        }}
        console.log(window[object_name])
      var stil = []
      stil.push(window[object_name])
      this.object_id_list.push(object_name)
      this.objeler_ozellikleri.push(stil)
      this.geojsonfutures.push({
        "type":"Feature",
        "properties":{"featureid":object_name,
                      "Geometri Tipi":"Nokta",
                      "X Koordinatı(Enlem)":parseFloat(x_coordinats),
                      "Y Koordinatı(Boylam)":parseFloat(y_coordinats)},
        "geometry":{
            "type":"Point",
            "coordinates":[y_coordinats,x_coordinats]}
      })
      console.log(this.objeler_ozellikleri)
    }
    menuleriolustur(){
      this.details_katman =document.createElement("details");
      this.details_katman.setAttribute("id",this.id_nosu);
      this.details_katman.setAttribute("name",this.id_nosu);
      this.summary_katman = document.createElement("summary");
      this.summary_katman.setAttribute("id",this.id_nosu+"_summary");
      document.getElementById("layers_vektor").appendChild(this.details_katman);
      document.getElementById(this.id_nosu).innerHTML='<button class="haritadagosterme" type="menu" >Haritada Göster</button><button class="haritadagizleme" type="menu" >Haritada Gizle</button><button class="sil" type="menu">Katmanı Sil</button><button class="duzenle" type="menu">Katmanı Düzenle</button><button class="yaklasma" type="menu" >Yaklaş</button><button class="stildegistir" type="menu" >Stil Değiştir</button><button class="oznitelikbilgi" type="menu" >Öznitelikleri Görüntüle ve Düzenle</button>';
      document.getElementById(this.id_nosu).appendChild(this.summary_katman);
      document.getElementById(this.id_nosu+"_summary").innerText=this.id_nosu;
      document.getElementById(this.id_nosu+"_summary").style.listStyle="none";
      document.getElementById(this.id_nosu+"_summary").style.fontSize="medium";
      document.getElementById(this.id_nosu+"_summary").style.fontWeight="bolder";
      document.getElementById(this.id_nosu+"_summary").style.color="black";
      document.getElementById(this.id_nosu+"_summary").style.fontFamily="'Courier New', Courier, monospace";
      document.getElementById(this.id_nosu+"_summary").style.cursor="pointer";
      document.getElementById(this.id_nosu+"_summary").style.listStyle="none";
      document.getElementById(this.id_nosu+"_summary").style.borderStyle="solid";
      document.getElementById(this.id_nosu+"_summary").style.backgroundColor=renk_listesi[Math.floor(Math.random()*renk_listesi.length)];
      document.getElementById(this.id_nosu+"_summary").style.borderColor="white";
      //butonlar ve kullanılacakları işlevler
      
      document.getElementById(this.id_nosu).getElementsByTagName("button")[0].setAttribute('onclick',"window['"+this.id_nosu+"'].objeyiyenile(window['"+this.id_nosu+"'])");
      document.getElementById(this.id_nosu).getElementsByTagName("button")[1].setAttribute('onclick',"window['"+this.id_nosu+"'].haritadagizle()");
      document.getElementById(this.id_nosu).getElementsByTagName("button")[2].setAttribute('onclick',"katman_sil('"+this.id_nosu+"')");
      document.getElementById(this.id_nosu).getElementsByTagName("button")[3].setAttribute('onclick',"window['"+this.id_nosu+"'].katmanduzenle(window['"+this.id_nosu+"'])");
      document.getElementById(this.id_nosu).getElementsByTagName("button")[4].setAttribute('onclick',"window['"+this.id_nosu+"'].objeyeyaklas()");
      document.getElementById(this.id_nosu).getElementsByTagName("button")[5].setAttribute('onclick',"window['"+this.id_nosu+"'].stildegistirme()");
      document.getElementById(this.id_nosu).getElementsByTagName("button")[6].setAttribute('onclick',"window['"+this.id_nosu+"'].oznitelikgoruntulemeveduzenleme()");
    }
    haritayaekle(x){
      this.layer = L.geoJSON(this.geojsonfutures,{
        pointToLayer:function(feature,latlng){
          return L.circleMarker(latlng,x)
        }
      }).addTo(map)
      console.log(this.layer)
    }
  }
