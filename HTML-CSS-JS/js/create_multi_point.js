
function multi_create_point(a){
    document.getElementById("oznitelikpenceresi").innerHTML="";
    var name = a
    document.getElementById('sayfamesajlari').style.backgroundColor  = "black";
    document.getElementById('sayfamesajlari').innerText="Çoklu Point Katmanı oluşturuldu\n"+name;//sayfa mesajlarında objenin oluştuğuna dair bilgi
    //harita üzerinde tıklama olayı ile koordinat almanın etkinleştirilmesi
    map.on('click', (e)=>{
    x = (e.latlng.lat).toFixed(8);
    y = (e.latlng.lng).toFixed(8);
    // oluşturulacak point için benzersiz bir id üretilir ve daha önceden bu id verilmiş mi kontrol edilir
      if ((typeof window[name])!=="object"){  //id in daha önceden var olup olmadığının kontrolü
          document.getElementById("vektor").open = true //katman penceresi sürekli açık olacak
          document.getElementById('sayfamesajlari').style.backgroundColor  = "black"; 
          var name2 = "point"+(new Date()).getMilliseconds()+Math.floor(Math.random()*1000);//benzersiz obje id alma
          window[name]= new multi_point(class_name=name); //alınan koordinat ve alınan rastgele obje adına göre çoklu point sınıfı oluşturulur
          window[name].objeler_ve_ozellikleri(x_coordinats=x,y_coordinats=y,object_name=name2)
          window[name].menuleriolustur()
          window[name].haritayaekle(window[name].objeler_bicim[(name2+"_bicim")],(name2+"_ozellikler"))
          document.getElementById('sayfamesajlari').innerText="Point oluşturuldu \n"+"E="+x+"   "+"B="+y;//sayfa mesajlarında objenin oluştuğuna dair bilgi
          //window[name].menuleriolustur()
          //window[name].haritayaekle(window[name].object_stil[window[name2].bicim])
        }
      else if ((typeof window[name])=="object" && (window[name].objeler_id_nolari.length > 0)) {
        document.getElementById("vektor").open = true
        document.getElementById('sayfamesajlari').style.backgroundColor  = "black"; 
        var name2 = "point"+(new Date()).getMilliseconds()+Math.floor(Math.random()*1000);//benzersiz obje id alma
        if (window[name].objeler_id_nolari.includes(name2)===true){
            alert("tekrar deneyiniz")}
        else{
          window[name].objeler_ve_ozellikleri(x_coordinats=x,y_coordinats=y,object_name=name2)
          window[name].haritayaekle(window[name].objeler_bicim[(name2+"_bicim")],(name2+"_ozellikler"))
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
    constructor(class_name){
        this.id_nosu = class_name
        this.objeler_properties_geometry = {}
        this.objeler_bicim = {}
        this.objeler_id_nolari = []
        this.layers = []
      }
    objeler_ve_ozellikleri(x_coordinats,y_coordinats,object_name){
      this.objeler_id_nolari.push(object_name.toString())
      window[object_name+"_ozellikler"] = {
        "type":"Feature",
        "properties": {
                        "featureid" : this.object_name,
                        "Geometri Tipi" : "Nokta",
                        "X Koordinatı (Enlem)" : parseFloat(x_coordinats),
                        "Y Koordinatı (Boylam)" : parseFloat(y_coordinats)
                        },
        "geometry":   {
                        "type":"Point",
                        "coordinates":[y_coordinats,x_coordinats]
                      }
      }
      window[object_name+"_bicim"] = {
        bicim:{radius: 8,
          fillColor: renk_listesi[Math.floor(Math.random()*renk_listesi.length)], //her oluşan obje bu algoritma ile rastgele bir renk alır
          color: "#000",  //dış çizginin renki
          weight: 1,  //dış çizginin kalınlığı
          opacity: 3, //dış çizginin opaklığı
          fillOpacity: 0.8},

          ikon:{ //objenin sembol ayarları bu nesneye gider
            iconUrl:null,
            iconSize:[50,50],
          }
      }
      this.objeler_properties_geometry[object_name.toString()+"_ozellikler"] = window[object_name+"_ozellikler"]
      this.objeler_bicim[object_name.toString()+"_bicim"] = window[object_name+"_bicim"]
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
    haritayaekle(x,y){
      var asd = L.geoJSON(this.objeler_properties_geometry[y],{
        pointToLayer:function(feature,latlng){
          return L.circleMarker(latlng,x.bicim)
        }
      })
      this.layers.push(asd)
      for (var c in this.layers){
        this.layers[c].addTo(map)
      }
    }
    haritadagizle(){
      for (var x in this.layers){
        map.removeLayer(this.layers[x])
      }
    }
  }
