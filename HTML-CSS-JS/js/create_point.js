/*Nokta Oluşturma Aşamaları-leaflette:
1- haritada tıklanılan yerden koordinatı alır ve point oluşturur /// elle koordinat girerek de oluşturulabilir
2- oluşturlan point haritaya eklenir
*/
function create_point(){
    
    var tekdongu=[1];
    //Sayfa Mesajlarında Çizime Başlamaya Dair Bildiri
    document.getElementById('sayfamesajlari').innerText="Çizime Başlayabilirsiniz.\nHome: Koordinat Gir\nEnd: Bitir";
    document.getElementById('sayfamesajlari').style.backgroundColor  = "black";
    //harita üzerinde tıklama olayı ile koordinat almanın etkinleştirilmesi
    map.on('click', (e)=>{
    x = (e.latlng.lat).toFixed(8);
    y = (e.latlng.lng).toFixed(8);
    // oluşturulacak point için benzersiz bir id üretilir ve daha önceden bu id verilmiş mi kontrol edilir
    var as;
    for (as in tekdongu ){
      var name = "point"+(new Date()).getMilliseconds()+Math.floor(Math.random()*1000);  //benzersiz id alma
      if ((typeof window[name])!=="object"){  //id in daha önceden var olup olmadığının kontrolü
          document.getElementById("vektor").setAttribute("open","open");
          document.getElementById('sayfamesajlari').style.backgroundColor  = "black"; 
          document.getElementById('sayfamesajlari').innerText=name+" oluşturuldu \n"+"E="+x+"   "+"B="+y;//sayfa mesajlarında objenin oluştuğuna dair bilgi
          window[name]= new point_object(x_coordinats=x,y_coordinats=y,object_name=name); //objenin oluşturulması
          window[name].haritayaekle(window[name].bicim);//objenin haritaya eklenmesi
          window[name].menuleriolustur();  //objeye ait vektörler penceresindeki menülerin oluşturulması
          bekleme(); //sayfa mesajlarındaki yazının kaybolması
          map.off('click');  //tıklama ile point eklemenin pasifleştiirlmesi
          }
      else{
        alert("Bu İd'ye Sahip Bir Obje Bulunmakta.");   
           }
   }
   }
        );
     // klavye kısayollarının etkinleştirilmesi
    document.addEventListener('keydown', (event) => {
    var name = event.key;
    var code = event.code;
    
    for (var x in tekdongu){
      // home tuşunun basılması durumunda elle korodinat girme fonksiyonu çalıştırılır
    if (code==="Home"){
    document.getElementById('obje_girdi').style.backgroundColor = "black";
    document.getElementById('obje_girdi').innerHTML='<label for="xbuton">E :</label><input type="number" maxlength="999999" id="xbuton" step="0.001" value="" required><br><label for="ybuton">B :</label><input type="number" maxlength="999999" id="ybuton" step="0.001" value="" required><input id="koordinatal" onclick="koordinatileolustur()" type="submit"  value="nokta oluştur">';
    map.off('click');
    break;
    }
    // end tuşuna basılması durumunda nokta oluşturma işlemi tamamlanır
    if (code === "End") {
    document.getElementById('sayfamesajlari').style.backgroundColor = "black";
    document.getElementById('sayfamesajlari').innerText = "İşlem Tamamlandı";
    map.off('click');
    bekleme();
    break;}
    }});
  }
  
  //-------------------------------------------------------------------------------------------------------------------------------------
    // koordinat girerek nokta oluşturma
  function koordinatileolustur(){
  var x = document.getElementById('xbuton').value;
  var y = document.getElementById('ybuton').value;
    while (true){
            // x veya y girişlerinin boş olmaması durumunda aşağıdaki if bloğu çalışır
            if (x!=="" && y!==""){
              //benzersiz bir id oluşturulur ve var olup olmadığı kontrol edilir
            name = "point"+(new Date()).getMilliseconds()+Math.floor(Math.random()*1000);
            if ((typeof window[name])!=="object"){  //id in daha önceden var olup olmadığının kontrolü
              document.getElementById('sayfamesajlari').style.backgroundColor  = "black"; 
              document.getElementById('sayfamesajlari').innerText=name+" oluşturuldu \n"+"E="+x+"   "+"B="+y;//sayfa mesajlarında objenin oluştuğuna dair bilgi
              window[name]= new point_object(x_coordinats=x,y_coordinats=y,object_name=name);  //objenin oluşturulması
              window[name].haritayaekle(window[name].bicim); //objenin haritaya eklenmesi
              window[name].menuleriolustur();  //objeye ait vektörler penceresindeki menülerin oluşturulması
              bekleme(); //sayfa mesajlarındaki yazının kaybolması
              document.getElementById('obje_girdi').innerText="";
              document.getElementById('obje_girdi').style.backgroundColor="unset";
              }
            else{
              // atanan id ye ait bir obje varsa uyarı çıkar
              alert("Bu İd'ye Sahip Bir Obje Bulunmakta.");
                break;
                }
            break;
            }
            else{
              alert("X veya Y Değeri Boş Bırakılamaz.");
              document.getElementById('obje_girdi').innerText="";
              document.getElementById('obje_girdi').style.backgroundColor="unset";
              break;
            }
          
          bekleme();
          document.getElementById('obje_girdi').innerText="";
          document.getElementById('obje_girdi').style.backgroundColor="unset";
          break;
          }
        }
  //--------------point objesine ait class-----------------------------------------------------------------------------------------------------------------------
  
class point_object {
      
      constructor(x_coordinats,y_coordinats,object_name){
        this.properties={     //--->objenin öznitelik bilgilerinin tutulduğu nesne
          "featureid":object_name,
          "Geometri Tipi":"Nokta",
          "X Koordinatı(Enlem)":parseFloat(x_coordinats),
          "Y Koordinatı(Boylam)":parseFloat(y_coordinats),
        };
        this.geojsonfeature = { //öznenin geometri tipi, öznitelikleri ve koordinatlarının tutulduğu nesne(leaflet bu nesneyi haritaya ekler)
        "type": "Feature",
        "properties": this.properties,
        "geometry":{
          "type":"Point",
          "coordinates":[y_coordinats,x_coordinats]}};
        this.gecerli_isaret="nokta"  ;   // objenin gösteriminin ne olduğu. stil sembol olarak ayarlanırsa bu değişken "sembol" olarak değişir
        this.bicim = {  //objenin noktasal gösterim ayarları
            radius: 8,
            fillColor: renk_listesi[Math.floor(Math.random()*renk_listesi.length)], //her oluşan obje bu algoritma ile rastgele bir renk alır
            color: "#000",  //dış çizginin renki
            weight: 1,  //dış çizginin kalınlığı
            opacity: 3, //dış çizginin opaklığı
            fillOpacity: 0.8}; //iç alanın opaklığı
        this.id_nosu = object_name   ; //create point fonksiyonunda oluşan id, burada objeye ait id_nosu olarak geçer
        this.icon={ //objenin sembol ayarları bu nesneye gider
          iconUrl:null,
          iconSize:null,
        };
      }
      //obje, create point ile luşturulurken menüler de bu fonksiyon çağırılarak oluşturulur. 
      menuleriolustur(){
        this.details_katman =document.createElement("details");
        this.details_katman.setAttribute("id",this.id_nosu);
        this.details_katman.setAttribute("name",this.id_nosu);
        this.summary_katman = document.createElement("summary");
        this.summary_katman.setAttribute("id",this.id_nosu+"_summary");
        document.getElementById("layers_vektor").appendChild(this.details_katman);
        document.getElementById(this.id_nosu).innerHTML='<button class="haritadagosterme" type="menu" >Haritada Göster</button><button class="haritadagizleme" type="menu" >Haritada Gizle</button><button class="sil" type="menu">Katmanı Sil</button><button class="yaklasma" type="menu" >Yaklaş</button><button class="stildegistir" type="menu" >Stil Değiştir</button><button class="oznitelikbilgi" type="menu" >Öznitelikleri Görüntüle ve Düzenle</button>';
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
        document.getElementById(this.id_nosu+"_summary").style.backgroundColor=this.bicim.fillColor;
        document.getElementById(this.id_nosu+"_summary").style.borderColor="white";
        //butonlar ve kullanılacakları işlevler
        document.getElementById(this.id_nosu).getElementsByTagName("button")[0].setAttribute('onclick',"window['"+this.id_nosu+"'].objeyiyenile(window['"+this.id_nosu+"'])");
        document.getElementById(this.id_nosu).getElementsByTagName("button")[1].setAttribute('onclick',"window['"+this.id_nosu+"'].haritadagizle()");
        document.getElementById(this.id_nosu).getElementsByTagName("button")[2].setAttribute('onclick',"katman_sil('"+this.id_nosu+"')");
        document.getElementById(this.id_nosu).getElementsByTagName("button")[3].setAttribute('onclick',"window['"+this.id_nosu+"'].objeyeyaklas()");
        document.getElementById(this.id_nosu).getElementsByTagName("button")[4].setAttribute('onclick',"window['"+this.id_nosu+"'].stildegistirme()");
        document.getElementById(this.id_nosu).getElementsByTagName("button")[5].setAttribute('onclick',"window['"+this.id_nosu+"'].oznitelikgoruntulemeveduzenleme()");
      }
      objeyiyenile(x){
        // objenin bilgilerinde değişiklik olduğu zaman bu fonksiyon çalışır ve obje yeniden yeni özelliklerle haritaya eklenir
        if(this.gecerli_isaret==="nokta"){ //noktanın geçerli stili nokta ise bu if çalışır ve nokta, noktasal olarak tekrar eklenir
          window[this.id_nosu].haritadagizle() //nokta ilk olarak haritadan kaldırılır
          this.layer=L.geoJSON(this.geojsonfeature,{ 
           // yeni özellikler ile tekrar haritaya eklenir
            pointToLayer:function(feature,latlng){
            return L.circleMarker(latlng,window[x.id_nosu].bicim);}}).addTo(map)// obje, noktassal gösterimde olduğu için circlemarker kullanılır  // haritaya eklendikten sonra üst ortadaki sayfa mesajları kapatılır 
          var a =Object.keys(this.layer._layers)[0]
          map_layers.push(parseInt(a))
          map_layers.push(parseInt(a)+1)
          }
        else{ //geçerli stil sembol ise bu blok çalışır
        window[this.id_nosu].haritadagizle();
        this.layer=L.geoJSON(this.geojsonfeature,{
          pointToLayer:function(feature,latlng){
            return L.marker(latlng,{icon:L.icon(x.icon),  // obje sembol gösteriminde olduğu için l.marker kullanılarak eklenir
            opacity:x.bicim.fillOpacity});}}).addTo(map);
            console.log("seçenek 2 çalıştı")
            var a =Object.keys(this.layer._layers)[0]
            map_layers.push(parseInt(a))
            map_layers.push(parseInt(a)+1)
          }
      }
      haritayaekle(x){  //obje ilk kez oluşturulurken bu fonksiyon çalıştırılır ve obje haritaya eklenir
        this.layer=L.geoJSON(this.geojsonfeature,{
          pointToLayer:function(feature,latlng){
            return L.circleMarker(latlng,x);}}).addTo(map);
        this.bounds=this.layer.getBounds() ; //objeye yakınlaşma işlevinin gerçekleşmesi için bu kısım ile obje çerçevvesinin koordinatları bounds değişkeine atanır
        var a =Object.keys(this.layer._layers)[0]
        map_layers.push(parseInt(a))
        map_layers.push(parseInt(a)+1)
        map_layers_id_nolari.push(window[this.id_nosu])
        if (map_layers_tum.length===0){
          map_layers_tum.push(parseInt(a)+2)
        }
        
      }
      //--------------------- objenin haritada gizlenmesi için aşağıdaki fonksiyon çalışır
      haritadagizle(){
        map.removeLayer(this.layer)
        var a =Object.keys(this.layer._layers)[0]
        var b = parseInt(a)+1
        map_layers.splice(map_layers.indexOf(a),1)
        map_layers.splice(map_layers.indexOf(b),1)
      }
      haritadansil(){
        map_layers_id_nolari.splice(map_layers_id_nolari.indexOf(this.id_nosu),1)
        var a =Object.keys(this.layer._layers)[0]
        map.removeLayer(map._layers[a])
        map_layers.splice(map_layers.indexOf(a),1)
        var b = parseInt(a)+1
        map.removeLayer(map._layers[b])
        map_layers.splice(map_layers.indexOf(b),1)

      }
      // ---------------------objeye yaklaşmak için aşağıdaki fonksiyon kullanılır
      objeyeyaklas(){
        // objeye yaklaşılabilmesi için map'de etkin bir harita servisinin olması gerekmektedir.
        if (gecerli_tilelayer!==""){
        map.fitBounds(this.bounds);  //map'de etkin harita varsa fitbounds ile objeye yaklaşılır
        }
        else{
          //map'de etkin bir harita yoksa, kullanıcıya uyarı verilir
        alert("Katmana Yaklaşabilmek İçin Herhangi Bir Harita Servisinin Etkin Olması Gerekmektedir.");
        }
    }
        //point menüüsnden stil değiştir butonu, aşağıdaki fonksiyonu çalıştırır
      stildegistirme(){
        document.getElementById("sayfamesajlari").style.backgroundColor="black";
        document.getElementById("sayfamesajlari").innerText="Stil Türünü Seçiniz.";
        var nokta_buton=document.createElement("button");
        var sembol_buton=document.createElement("button");
        nokta_buton.setAttribute("class","nokta_buton");
        nokta_buton.setAttribute("onclick","window['"+this.id_nosu+"'].noktasalgosterim()") ; // nokta butonu, noktasalgosterim() fonksiyonunu çağırı
        nokta_buton.innerText="Nokta";
        sembol_buton.setAttribute("class", "sembol_buton");
        sembol_buton.setAttribute("onclick","window['"+this.id_nosu+"'].sembolgosterimiayarlari()") ;// sembol butonu, sembolgosterimiayarlari() fonksiyonunu çağırır
        sembol_buton.innerText="Sembol";
        document.getElementById("sayfamesajlari").appendChild(nokta_buton);
        document.getElementById("sayfamesajlari").appendChild(sembol_buton);
        var kapatbuton=document.createElement("button");
        kapatbuton.backgroundImage="url('../close_ikon.png')";
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        document.getElementById("sayfamesajlari").appendChild(kapatbuton);
      }
      sembolgosterimiayarlari(){
        
        document.getElementById("sayfamesajlari").style.backgroundColor="black";
        document.getElementById("sayfamesajlari").innerText="";
        var altsatir=document.createElement("br");
        document.getElementById("sayfamesajlari").innerText="İnternet Üzerinden Simge Ekleyebilirsiniz.\nÖrnek:www.asd.com/sembol.png";
        document.getElementById("sayfamesajlari").style.width="400px";
        //url ile sembol ekleme kısmı
        var form_element=document.createElement("form");
        form_element.setAttribute("class","formelementi");
        var label_element=document.createElement("label");
        label_element.setAttribute("for","alurl");
        label_element.innerText="\nResim Urlsi";
        var renksecici=document.createElement("input");
        renksecici.setAttribute("id","alurl");
        renksecici.setAttribute("type","url");
        renksecici.setAttribute("name","Url Al");
        renksecici.setAttribute("value","");
        var renkalma = document.createElement("input");
        renkalma.setAttribute("type","submit");
        renkalma.setAttribute("value","Uygula");
        renkalma.setAttribute("onclick","window['"+this.id_nosu+"'].sembolurluygula('"+this.id_nosu+"')");
        document.getElementById("sayfamesajlari").style.backgroundColor="black";
        document.getElementById("sayfamesajlari").appendChild(label_element);
        document.getElementById("sayfamesajlari").appendChild(renksecici);
        document.getElementById("sayfamesajlari").appendChild(renkalma);
        document.getElementById("sayfamesajlari").appendChild(altsatir);
        var ikincimetin=document.createTextNode("Semboller Butonu İle Yerel  \n Sembollerden Seçebilirsiniz.");
  
        //kütüphaneden sembol seçe kısmı
        
        var sembolsec_detail=document.createElement("details");
          sembolsec_detail.setAttribute("id",this.id_nosu+"detail");
          sembolsec_detail.style.height="25px";
          sembolsec_detail.style.width="85px";
          sembolsec_detail.style.borderRadius="5px";
          sembolsec_detail.style.backgroundColor="wheat";
          sembolsec_detail.style.color="black";
          sembolsec_detail.style.marginLeft="40%";
          sembolsec_detail.style.marginLeft="0px";
        var sembolsec_summary=document.createElement("summary");
        sembolsec_summary.innerText="Semboller";
          sembolsec_summary.setAttribute("id",this.id_nosu+"summary");
          sembolsec_summary.style.width="100px";
          sembolsec_summary.style.cursor="pointer";
          sembolsec_summary.style.listStyle="none";
          sembolsec_summary.style.backgroundColor="black";
          sembolsec_summary.style.color="white";
          sembolsec_summary.style.border="solid 5px white";
        var sembolsec_div=document.createElement("div");
          sembolsec_div.setAttribute("id",this.id_nosu+"div");
          sembolsec_div.style.backgroundColor="black";
          sembolsec_div.style.color="wheat";
          sembolsec_div.style.width="200px";
          sembolsec_div.style.marginTop="10px";
          sembolsec_div.style.height="200px";
          sembolsec_div.style.overflowY="scroll";
          sembolsec_div.style.overflowX="scroll";
          sembolsec_div.style.marginLeft="-200px";
          sembolsec_div.style.marginTop="-30px";
        document.getElementById("sayfamesajlari").appendChild(ikincimetin);
        document.getElementById("sayfamesajlari").appendChild(sembolsec_detail);
        document.getElementById(this.id_nosu+"detail").appendChild(sembolsec_summary);
        document.getElementById(this.id_nosu+"detail").appendChild(sembolsec_div);
        var c;
        for (c in symbol_list){
          var divsemboller=document.createElement("div");
          divsemboller.setAttribute("class",c+"semboldiv");
          divsemboller.style.width="180px";
          divsemboller.style.height="30px";
          divsemboller.style.borderStyle="solid";
          divsemboller.style.border="white;2px";
          divsemboller.style.backgroundColor="black";
          window[c+"symbol"] = document.createElement("button");
          var labelll = document.createElement("label");
          labelll.innerText=Object.values(symbol_list[c]);
          labelll.style.textAlign="center";
          labelll.style.width="auto";
          labelll.style.height="30px";
          labelll.style.fontSize="medium";
          window[c+"symbol"].style.backgroundImage="url('"+Object.keys(symbol_list[c])+"')";
          window[c+"symbol"].style.backgroundSize="contain";
          window[c+"symbol"].style.width="30px";
          window[c+"symbol"].style.height="30px";
          window[c+"symbol"].style.float="right";
          window[c+"symbol"].setAttribute("onclick","window['"+this.id_nosu+"'].semboluuygula('"+Object.keys(symbol_list[c])+"','"+this.id_nosu+"')");
          document.getElementById(this.id_nosu+"div").appendChild(divsemboller);
          document.getElementById(this.id_nosu+"div").getElementsByClassName(c+"semboldiv")[0].appendChild(labelll);
          document.getElementById(this.id_nosu+"div").getElementsByClassName(c+"semboldiv")[0].appendChild(window[c+"symbol"]);
        }
        var sembol_buyukluk_labelyazi = document.createElement("label");
        sembol_buyukluk_labelyazi.innerText="Sembol Büyüklüğünü Ayarla\n Örnek:(30 px x 30 px)";
        var sembol_buyukluk_label=document.createElement("label");
        sembol_buyukluk_label.setAttribute("for","sembolbuyukluken");
        sembol_buyukluk_label.innerText="En:(px)";
        var enuzunluk=document.createElement("input");
        enuzunluk.setAttribute("id","sembolbuyukluken");
        enuzunluk.setAttribute("type","number");
        var sembol_buyukluk_label2=document.createElement("label");
        sembol_buyukluk_label2.setAttribute("for","sembolbuyuklukboy");
        sembol_buyukluk_label2.innerText="Boy:(px)";
        var boyuzunluk=document.createElement("input");
        boyuzunluk.setAttribute("id","sembolbuyuklukboy");
        boyuzunluk.setAttribute("type","number");
       // var sembol_saydamlik  = document.createElement("button")
        var semboluzunluk_al = document.createElement("input");
        semboluzunluk_al.setAttribute("type","submit");
        semboluzunluk_al.setAttribute("value","Uygula");
        semboluzunluk_al.setAttribute("onclick","window['"+this.id_nosu+"'].sembolbuyuklukdegistir()");
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        document.getElementById("sayfamesajlari").appendChild(sembol_buyukluk_labelyazi);
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        document.getElementById("sayfamesajlari").appendChild(sembol_buyukluk_label);
        document.getElementById("sayfamesajlari").appendChild(enuzunluk);
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        document.getElementById("sayfamesajlari").appendChild(sembol_buyukluk_label2);
        document.getElementById("sayfamesajlari").appendChild(boyuzunluk);
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        document.getElementById("sayfamesajlari").appendChild(semboluzunluk_al);
        var sembolsaydamlik_yazi=document.createElement("label");
        sembolsaydamlik_yazi.innerText="Sembol Saydamlığını Ayarla (0-1)";
        sembolsaydamlik_yazi.setAttribute("for","sembolsaydamlik");
        var sembolsaydamlik_al=document.createElement("input");
        sembolsaydamlik_al.setAttribute("id","sembolsaydamlik");
        sembolsaydamlik_al.setAttribute("type","number");
        sembolsaydamlik_al.setAttribute("value","1");
        sembolsaydamlik_al.setAttribute("step","0.001");
        var sembolsaydamlik_buton=document.createElement("input");
        sembolsaydamlik_buton.setAttribute("value","Uygula");
        sembolsaydamlik_buton.setAttribute("type","submit");
        sembolsaydamlik_buton.setAttribute("onclick","window['"+this.id_nosu+"'].sembolsaydamlikdegistir()");
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        document.getElementById("sayfamesajlari").appendChild(sembolsaydamlik_yazi);
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        document.getElementById("sayfamesajlari").appendChild(sembolsaydamlik_al);
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        document.getElementById("sayfamesajlari").appendChild(sembolsaydamlik_buton);
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        var bitirbuton = document.createElement("button");
        bitirbuton.innerText="Kapat";
        bitirbuton.setAttribute("value","Kapat");
        bitirbuton.setAttribute("onclick","bekleme()");
        document.getElementById("sayfamesajlari").appendChild(bitirbuton);
      }
      // sembol ayarlarında, girilen sembol saydamlığı bu fonksiyonda işlem görür. sembol gösterimi etkin olmasa da bu fonksyion sorunsuz çalışır. eklenecek sembol, saydamlık değişikiğinden etkilenir
      sembolsaydamlikdegistir(){
        var saydamlikdegeri=document.getElementById("sembolsaydamlik").value ; //girilen değer alınır
        if (0<=parseFloat(saydamlikdegeri) && parseFloat(saydamlikdegeri)<=1){  //girilen değerin 0-1 arasında olması gerek. bu durum kontrol edilir
          this.bicim.fillOpacity=saydamlikdegeri ;   // objeye ait bicim değişkenine, kullanıcının verdiği değer atanır
          window[this.id_nosu].objeyiyenile(window[this.id_nosu]) ;//değişikliğin harita ekranında etkin olması için obje yenilenir.
        }
        else{
          // kullanıcı, uyumsuz veri girerse ekrana uyarı verilir
          alert("Girilen Değer 0-1 e Eşit Veya Arasında Olmalı");
        }
      }
      // kullanıcı, url ile sembol seçerse bu blok çalışır
      sembolurluygula(x){
        // URL kontrol bloğu
        var urlkontrol=isValidURL(document.getElementById("sayfamesajlari").getElementsByTagName("input")[0].value);
        if(urlkontrol===true && document.getElementById("sayfamesajlari").getElementsByTagName("input")[0].value!==""){
          this.gecerli_isaret="sembol";  // sembol değiştiği için, geçerli işaret değişkeni sembol olarak değiştirilir
          this.icon.iconUrl=document.getElementById("sayfamesajlari").getElementsByTagName("input")[0].value;  //kullanıcının girdiği url alınır 
          window[this.id_nosu].objeyiyenile(window[this.id_nosu]) ;// seembol değişikliğinden sonra obje yenilenir
          }
        else{
          //kullanıcı, uyumsuz url girerse uyarı verilir
          alert("Yanlış Biçimde Giriş Yapıldı. Lütfen Geçerli Bir Url Giriniz.");
        }
      }
      // 
      // kullanıcı, kütüphaneden bir sembol seçerse bu blok çalışır ve seçilen sembol objeye uygulanır
      semboluuygula(i,x){
        this.icon.iconUrl=i;
        this.gecerli_isaret="sembol";
        window[this.id_nosu].objeyiyenile(window[this.id_nosu]);
      }
      //  kullanıcıdan gelen sembol büyüklüğü, objenin icon değişkenine atılır ve obje yenilenerek eğer sembol seçildiyse sembol olarak, değilse nokta olarak eklenir
      sembolbuyuklukdegistir(){
        var en = document.getElementById("sembolbuyukluken").value;
        var boy = document.getElementById("sembolbuyuklukboy").value;
        var iconsize=[en,boy];
        this.icon.iconSize=iconsize;
        window[this.id_nosu].objeyiyenile(window[this.id_nosu]);
      }
  
      noktasalgosterim(){
        //Renk Değiştirmek İçin Gerekli Butonlar
        document.getElementById("sayfamesajlari").style.backgroundColor="black";
        document.getElementById("sayfamesajlari").innerText="";
        document.getElementById("sayfamesajlari").style.width="auto";
        var div1=document.createElement("div");
        div1.setAttribute("class","div1");
        div1.style.alignItems="center";
        div1.style.backgroundColor="red";
        var label_element=document.createElement("label");
        label_element.setAttribute("for","favcolor");
        label_element.innerText="Rengi Seçiniz";
        var renksecici=document.createElement("input");
        renksecici.setAttribute("id","favcolor");
        renksecici.setAttribute("type","color");
        renksecici.setAttribute("name","favcolor");
        renksecici.setAttribute("value",this.bicim.fillColor);
        var renkalma = document.createElement("input");
        renkalma.setAttribute("type","submit");
        renkalma.setAttribute("value","Değiştir");
        renkalma.setAttribute("onclick","window['"+this.id_nosu+"'].rengialma('"+this.id_nosu+"')");
        document.getElementById("sayfamesajlari").style.backgroundColor="black";
        document.getElementById("sayfamesajlari").appendChild(div1);
        document.getElementById("sayfamesajlari").getElementsByClassName("div1")[0].appendChild(label_element);
        document.getElementById("sayfamesajlari").getElementsByClassName("div1")[0].appendChild(renksecici);
        document.getElementById("sayfamesajlari").getElementsByClassName("div1")[0].appendChild(renkalma);
        //Büyüklük Ayarlama
        var div2=document.createElement("div");
        div2.setAttribute("class","div2");
        div2.style.alignItems="center";
        div2.style.backgroundColor="blue";
        var label_element2 = document.createElement("label");
        label_element2.setAttribute("for","buyukluksecim");
        label_element2.innerText="Noktanın Yarıçapını Giriniz.(Şuanki Yarıçap Değeri:'"+window[this.id_nosu].bicim.radius+"')";
        var input1 = document.createElement("input");
        input1.setAttribute("id","buyukluksecim");
        input1.setAttribute("type","number");
        input1.setAttribute("maxlenght","1000");
        input1.setAttribute("step","0.001");
        input1.required=true;
        var input2= document.createElement("input");
        input2.setAttribute("type","submit");
        input2.setAttribute("value","Değiştir");
        input2.setAttribute("onclick","window['"+this.id_nosu+"'].manuelbuyuklukalma('"+this.id_nosu+"')");
        document.getElementById("sayfamesajlari").appendChild(div2);
        document.getElementById("sayfamesajlari").getElementsByClassName("div2")[0].appendChild(label_element2);
        document.getElementById("sayfamesajlari").getElementsByClassName("div2")[0].appendChild(input1);
        document.getElementById("sayfamesajlari").getElementsByClassName("div2")[0].appendChild(input2);
        //saydamlık ayarlama,
        var div3=document.createElement("div");
        div3.setAttribute("class","div3");
        div3.style.alignItems="center";
        div3.style.backgroundColor="orange";
        var label_element3 = document.createElement("label");
        label_element3.setAttribute("for","saydamliksecim");
        label_element3.innerText="Saydamlık Değerini Giriniz.(0-1 Arasında:Şuanki Değer->'"+window[this.id_nosu].bicim.fillOpacity+"')";
        var input3 = document.createElement("input");
        input3.setAttribute("id","saydamliksecim");
        input3.setAttribute("type","number");
        input3.setAttribute("max","1");
        input3.setAttribute("min","0");
        input3.setAttribute("step","0.001");
        input3.setAttribute("maxlength","1");
        input3.required=true;
        var input4= document.createElement("input");
        input4.setAttribute("type","submit");
        input4.setAttribute("value","Değiştir");
        input4.setAttribute("onclick","window['"+this.id_nosu+"'].saydamlikdegistir('"+this.id_nosu+"')");
        var islemibitir = document.createElement("button");
        islemibitir.setAttribute("onclick","bekleme()");
        islemibitir.innerText="Bitir";
        islemibitir.alignItems="center";
        document.getElementById("sayfamesajlari").appendChild(div3);
        document.getElementById("sayfamesajlari").getElementsByClassName("div3")[0].appendChild(label_element3);
        document.getElementById("sayfamesajlari").getElementsByClassName("div3")[0].appendChild(input3);
        document.getElementById("sayfamesajlari").getElementsByClassName("div3")[0].appendChild(input4);
        document.getElementById("sayfamesajlari").appendChild(islemibitir);
      }
      // stil değiştir de nokta seçilirse, büyüklük ayarlarken aşağıdaki fonksiyon çalışır
      manuelbuyuklukalma(id_no){
        var buyuklukdegeri = document.getElementById("sayfamesajlari").getElementsByTagName("input")[2].value;
        this.gecerli_isaret="nokta";
        this.bicim.radius=buyuklukdegeri;
        this.objeyiyenile(window[this.id_nosu]);
      }
      // stil değiştirde nokta seçilirse, saydamlık alınması aşağıdaki fonksiyon ile gerçekleşir
      saydamlikdegistir(id_no){
        var saydamlikdegeri=(document.getElementById("sayfamesajlari").getElementsByTagName("input")[4].value);
        if (0<=parseFloat(saydamlikdegeri) && parseFloat(saydamlikdegeri)<=1){  // saydamlık değerinin, 0-1 arasında olup olmadığı kontrol edilir
          this.gecerli_isaret="nokta"; 
          this.bicim.fillOpacity=saydamlikdegeri;
          this.objeyiyenile(window[this.id_nosu]);
        }
        else {
          console.log("değer geçersiz.varsayılan değer uygulandı",saydamlikdegeri);
        }
      }
      // kullanıcının işaretlediği renk kodu, aşağıdaki buton ile objeye aktarılır
      rengialma(id_no){
        var renk = document.getElementById("sayfamesajlari").getElementsByTagName("input")[0].value;
        this.bicim.fillColor=renk;
        this.gecerli_isaret="nokta";
        this.objeyiyenile(window[this.id_nosu]);
        document.getElementById(this.id_nosu+"_summary").style.backgroundColor=this.bicim.fillColor;
          }
      // katman menüsünde, öznitelik görüntüle ve düzenle butonu ile aşağıdaki fonksiyonlar çalışır
      oznitelikgoruntulemeveduzenleme(){
        // öznitelik penceresinin en üstünde, obje featureid i ve kapat butonu eklenmesi
        document.getElementById("oznitelikpenceresi").innerText="";
        document.getElementById("oznitelikpenceresi").style.overflowX="scroll";
        var sdd;
        var ustsekme=document.createElement("div");
        ustsekme.innerText=this.id_nosu;
        ustsekme.setAttribute("id",this.id_nosu+"kapat");
        ustsekme.style.height="30px";
        ustsekme.style.backgroundColor="white";
        ustsekme.style.border="5px solid black";
        ustsekme.style.textAlign="center";
        ustsekme.style.fontSize="large";
        ustsekme.style.fontWeight="bolder";
        var kapatbuton=document.createElement("button");
        kapatbuton.setAttribute("onclick","window['"+this.id_nosu+"'].oznitelikpenceresikapat()");
        kapatbuton.setAttribute("value","Kapat");
        kapatbuton.style.width="100px";
        kapatbuton.style.height="30px";
        kapatbuton.innerText="Kapat";
        kapatbuton.style.float="right";
        document.getElementById("oznitelikpenceresi").appendChild(ustsekme);
        document.getElementById(this.id_nosu+"kapat").appendChild(kapatbuton);
        // özniteliklerin eklenmesi için, öznitelik değişkenindeki tüm keyler for ile döner ve teker teker eklenir
        for (sdd in this.properties){
            //kolon adı ve içeriğinin yer alacağı div kısmı 
            var kolonbir=document.createElement("div");
            kolonbir.setAttribute("id",sdd);
            kolonbir.style.width="auto";
            kolonbir.style.height="180px";
            kolonbir.style.float="left";
            kolonbir.style.backgroundColor="black";
            kolonbir.style.overflowX="scroll";
            kolonbir.style.fontSize="medium";
            kolonbir.style.fontWeight="bold";
          //kolon adı ile ilgili menü
          //kolon adına tıklayınca açılacak menü ve işlevleri
            var kolonmenu = document.createElement("details");
            kolonmenu.setAttribute("id",sdd+"details");
            kolonmenu.style.width="140px";
            kolonmenu.style.height="50px";
            var kolonmenu_summary=document.createElement("summary");
            kolonmenu_summary.innerText=sdd;
            kolonmenu_summary.style.cursor="pointer";
            kolonmenu_summary.style.listStyle="none";
            kolonmenu_summary.style.color="red";
            kolonmenu_summary.style.backgroundColor="black";
            kolonmenu_summary.style.width="140px";
            kolonmenu_summary.style.height="50px";
            kolonmenu_summary.setAttribute("id",sdd+"summary");
            document.getElementById("oznitelikpenceresi").appendChild(kolonbir);
            document.getElementById(sdd).appendChild(kolonmenu);
            document.getElementById(sdd+"details").appendChild(kolonmenu_summary);
            var menudiv=document.createElement("div");
            menudiv.setAttribute("id",sdd+"menudiv");
            menudiv.style.width="200px";
            menudiv.style.height="110px";
            menudiv.style.border="red solid 5px";
            menudiv.style.marginLeft="0px";
            menudiv.style.position="absolute";
            menudiv.style.backgroundColor="black";
            menudiv.style.overflowY="scroll";
            var kolonmenu_duzenle=document.createElement("button");
            kolonmenu_duzenle.setAttribute("value","Düzenle");
            kolonmenu_duzenle.innerText="Düzenle";
            var kolonmenu_sil=document.createElement("button");
            kolonmenu_sil.setAttribute("value","Sil");
            kolonmenu_sil.innerText="Sil";
            var kolonmenu_ozellikler=document.createElement("button");
            kolonmenu_ozellikler.setAttribute("value","Özellikler");
            kolonmenu_ozellikler.innerText="Özellikler";
            var saga_kolon_ekle=document.createElement("button");
            saga_kolon_ekle.setAttribute("value","Sağına Kolon Ekle");
            saga_kolon_ekle.innerText="Sağına Kolon Ekle";
            saga_kolon_ekle.setAttribute("onclick","window['"+this.id_nosu+"'].sagakolonekle('"+sdd+"')");
            kolonmenu_ozellikler.setAttribute("onclick","window['"+this.id_nosu+"'].oznitelikmenuozellikler('"+sdd+"')");
            // featureid, Geometri Tipi, X Koordinatı(Enlem) ve Y Koordinatı(Boylam) öznitelikleri değiştirilemez niteliklerdir. Bu yüzden bu 
            // niteliklerin kolon adı ve niteliği değiştirilemez.
            if (sdd!=="featureid" && sdd !=="Geometri Tipi" && sdd !=="X Koordinatı(Enlem)" && sdd !== "Y Koordinatı(Boylam)"){
  
              kolonmenu_duzenle.setAttribute("onclick","window['"+this.id_nosu+"'].oznitelikkolonduzenle('"+sdd+"')");
              kolonmenu_sil.setAttribute("onclick","window['"+this.id_nosu+"'].oznitelikkolonsil('"+sdd+"')");
              
            }
            else{
              kolonmenu_duzenle.setAttribute("onclick","alert('"+sdd+"' +' kolonu düzenlenemez')");
              kolonmenu_sil.setAttribute("onclick","alert('"+sdd+"'+' kolonu düzenlenemez')");
            }
            document.getElementById(sdd+"details").appendChild(menudiv);
            document.getElementById(sdd+"menudiv").appendChild(kolonmenu_duzenle);
            document.getElementById(sdd+"menudiv").appendChild(document.createElement("br"));
            document.getElementById(sdd+"menudiv").appendChild(kolonmenu_sil);
            document.getElementById(sdd+"menudiv").appendChild(document.createElement("br"));
            document.getElementById(sdd+"menudiv").appendChild(kolonmenu_ozellikler);
            document.getElementById(sdd+"menudiv").appendChild(document.createElement("br"));
            document.getElementById(sdd+"menudiv").appendChild(saga_kolon_ekle);
            document.getElementById(sdd).appendChild(document.createElement("br"));
            var kolonicerik_detail=document.createElement("details");
            kolonicerik_detail.setAttribute("id",sdd+"kolonicerik_detail");
            kolonicerik_detail.style.width="140px";
            kolonicerik_detail.style.height="50px";
            var dfs = document.createElement("summary");
            var genislik = document.getElementById(sdd).getElementsByTagName("details")[0].clientWidth;
            dfs.setAttribute("id",sdd+"iceriksummary");
            dfs.innerText=this.properties[sdd];
            dfs.style.color="white";
            dfs.style.width="140px";
            dfs.style.height="50px";
            dfs.style.cursor="pointer";
            dfs.style.listStyle="none";
            dfs.style.backgroundColor="black";
            document.getElementById(sdd).appendChild(kolonicerik_detail);
            document.getElementById(sdd+"kolonicerik_detail").appendChild(dfs);
            var kolonicerik_menu=document.createElement("button");
            kolonicerik_menu.innerText="Düzenle";
            kolonicerik_menu.style.width="auto";
            kolonicerik_menu.style.hei="auto";
            kolonicerik_menu.style.border="solid red 5px";
            kolonicerik_menu.style.marginLeft="0px";
            kolonicerik_menu.style.position="absolute";
            kolonicerik_menu.style.color="white";
            kolonicerik_menu.style.backgroundColor="black";
            kolonicerik_menu.setAttribute("onclick","window['"+this.id_nosu+"'].kolonicerikdegistir('"+sdd+"')");
            if (sdd!=="featureid" && sdd !=="Geometri Tipi" && sdd !=="X Koordinatı(Enlem)" && sdd !== "Y Koordinatı(Boylam)"){
              kolonicerik_menu.setAttribute("onclick","window['"+this.id_nosu+"'].oznitelikicerikdegistir('"+sdd+"')");
            }
            else{
              kolonicerik_menu.setAttribute("onclick","alert('"+sdd+"'+' kolonu düzenlenemez')");
            }
            document.getElementById(sdd+"kolonicerik_detail").appendChild(kolonicerik_menu);
          //kolona ait div
      }
    }
      oznitelikkolonduzenle(i){
        document.getElementById(i+"details").removeAttribute("open");
        //bilgilerin sayfa mesajlarına yazılması
        var sayfamesajlari=document.getElementById("sayfamesajlari");
        sayfamesajlari.style.backgroundColor="black";
        sayfamesajlari.innerText="";
        var labelbir = document.createElement("label");
        labelbir.innerText="Kolon Adı:";
        labelbir.setAttribute("for","kolonadiduzenle");
        var kolonadigir=document.createElement("input");
        kolonadigir.setAttribute("id","kolonadiduzenle");
        kolonadigir.setAttribute("type","Kolon Adı");
        kolonadigir.setAttribute("value",i);
        sayfamesajlari.appendChild(labelbir);
        sayfamesajlari.appendChild(kolonadigir);
        sayfamesajlari.appendChild(document.createElement("br"));
        // veri tipinin seçimi
        var div_tip=document.createElement("div");
        div_tip.setAttribute("id","tipsecim");
        var labeliki=document.createElement("label");
        labeliki.innerText="Veri Tipi:";
        labeliki.setAttribute("for","cevap");
        var veritip_bir=document.createElement("input");
        veritip_bir.setAttribute("type","radio");
        veritip_bir.setAttribute("class","cevap");
        veritip_bir.setAttribute("name","cevap1");
        veritip_bir.setAttribute("value","text");
        var veritip_iki=document.createElement("input");
        veritip_iki.setAttribute("type","radio");
        veritip_iki.setAttribute("class","cevap");
        veritip_iki.setAttribute("name","cevap1");
        veritip_iki.setAttribute("value","tam sayı");
        var veritip_uc=document.createElement("input");
        veritip_uc.setAttribute("type","radio");
        veritip_uc.setAttribute("class","cevap");
        veritip_uc.setAttribute("name","cevap1");
        veritip_uc.setAttribute("value","ondalıklı sayı");
        sayfamesajlari.appendChild(div_tip);
        document.getElementById("tipsecim").appendChild(document.createTextNode("Metin"));
        document.getElementById("tipsecim").appendChild(veritip_bir);
        document.getElementById("tipsecim").appendChild(document.createTextNode("Tam Sayı"));
        document.getElementById("tipsecim").appendChild(veritip_iki);
        document.getElementById("tipsecim").appendChild(document.createTextNode("Ondalıklı Sayı"));
        document.getElementById("tipsecim").appendChild(veritip_uc);
        document.getElementById("tipsecim").appendChild(document.createElement("br"));
        var uygula_buton=document.createElement("input");
        uygula_buton.setAttribute("type","submit");
        uygula_buton.innerText="Uygula";
        uygula_buton.setAttribute("onclick","window['"+this.id_nosu+"'].oznitelikdegisiklikuygula('"+i+"')");
        document.getElementById("tipsecim").appendChild(uygula_buton);
  
      }
      oznitelikdegisiklikuygula(i){
        document.getElementById("sayfamesajlari").innerText="";

        var a = document.getElementById("kolonadiduzenle").value;
        if (a!==i && a!==""){
          this.properties[a]=this.properties[i];
          delete this.properties[i];
          console.log("\""+i+"\" Kolonunun İsmi \""+a+ "\" Olarak Değiştirildi");
          try {
            var veri_tip=document.querySelector('input[name = cevap1]:checked').value;
            if (document.querySelector('input[name = cevap1]:checked').value==="text"){
              this.properties[a]=this.properties[a].toString();
            }
            else if(document.querySelector('input[name = cevap1]:checked').value==="tam sayı"){
              this.properties[a]=parseInt(this.properties[a]);
              if (isNaN(this.properties[a])){
                this.properties[a]=null;
              }
            }
            else if(document.querySelector('input[name = cevap1]:checked').value==="ondalıklı sayı"){
              this.properties[a]=parseFloat(this.properties[a]);
              if (isNaN(this.properties[a])){
                this.properties[a]=null;
              }
            }
            window[this.id_nosu].oznitelikgoruntulemeveduzenleme();
            window[this.id_nosu].objeyiyenile(window[this.id_nosu]);
            bekleme();
            }
            catch(err){
              console.log("Tip Seçilmeden İşlem Yapıldı. Kolon Tipi Aynı Kaldı");
              this.properties[a]=this.properties[a];
              window[this.id_nosu].objeyiyenile(window[this.id_nosu]);
              window[this.id_nosu].oznitelikgoruntulemeveduzenleme();
              bekleme();
            }
        }
        else if (a===""){
          alert("Kolon Adı Boş Bırakılamaz.");
          bekleme();
        }
        else{
          try {
            var veri_tip=document.querySelector('input[name = cevap1]:checked').value;
            if (document.querySelector('input[name = cevap1]:checked').value==="text"){
              this.properties[i]=this.properties[i].toString();
            }
            else if(document.querySelector('input[name = cevap1]:checked').value==="tam sayı"){
              this.properties[i]=parseInt(this.properties[i]);
              if (isNaN(this.properties[i])){
                this.properties[i]=null;
              }
            }
            else if(document.querySelector('input[name = cevap1]:checked').value==="ondalıklı sayı"){
              this.properties[i]=parseFloat(this.properties[i]);
              if (isNaN(this.properties[i])){
                this.properties[i]=null;
              }
            }
            window[this.id_nosu].objeyiyenile(window[this.id_nosu]);
            window[this.id_nosu].oznitelikgoruntulemeveduzenleme();
            bekleme();
            }
            catch(err){
              console.log("Tip Seçilmeden İşlem Yapıldı. Kolon Tipi Aynı Kaldı");
              this.properties[i]=this.properties[i];
              window[this.id_nosu].objeyiyenile(window[this.id_nosu]);
              window[this.id_nosu].oznitelikgoruntulemeveduzenleme();
              bekleme();
            }
        }
        bekleme();
      }
        
    oznitelikmenuozellikler(k){
        var sayfamesajlari=document.getElementById("sayfamesajlari");
        sayfamesajlari.style.backgroundColor="black";
        sayfamesajlari.innerText="";
        var kolonadi=document.createElement("label");
        kolonadi.innerText="Kolon Adı=     "+k;
        var kolontip=document.createElement("label");
        if (typeof this.properties[k]==="string"){
          kolontip.innerText="Kolon Veri Tipi=     Metin";
        }
        else if (Number.isInteger(this.properties[k])===true){
          kolontip.innerText="Kolon Veri Tipi=     Tam Sayı";
        }
        else if (typeof this.properties[k]!=="string" && Number.isInteger(this.properties[k])===false ){
          kolontip.innerText="Kolon Veri Tipi=     Ondalıklı Sayı";
        }
        document.getElementById("sayfamesajlari").appendChild(kolonadi);
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        document.getElementById("sayfamesajlari").appendChild(kolontip);
        document.getElementById("sayfamesajlari").appendChild(document.createElement("br"));
        var kapatbutonu=document.createElement("button");
        kapatbutonu.setAttribute("value","Kapat");
        kapatbutonu.setAttribute("onclick","bekleme()");
        kapatbutonu.innerText="Kapat";
        document.getElementById("sayfamesajlari").appendChild(kapatbutonu);
      }
      oznitelikkolonsil(l){
        delete this.properties[l];
        window[this.id_nosu].oznitelikgoruntulemeveduzenleme();
        window[this.id_nosu].objeyiyenile(window[this.id_nosu]);
      }
      sagakolonekle(v){
        //bilgilerin sayfa mesajlarına yazılması
        var sayfamesajlari=document.getElementById("sayfamesajlari");
        sayfamesajlari.style.backgroundColor="black";
        sayfamesajlari.innerText="";
        var labelbir = document.createElement("label");
        labelbir.innerText="Kolon Adı:";
        labelbir.setAttribute("for","kolonadiduzenle");
        var kolonadigir=document.createElement("input");
        kolonadigir.setAttribute("id","kolonadiduzenle");
        kolonadigir.setAttribute("type","Kolon Adı");
        sayfamesajlari.appendChild(labelbir);
        sayfamesajlari.appendChild(kolonadigir);
        sayfamesajlari.appendChild(document.createElement("br"));
        // veri tipinin seçimi
        var div_tip=document.createElement("div");
        div_tip.setAttribute("id","tipsecim");
        var labeliki=document.createElement("label");
        labeliki.innerText="Veri Tipi:";
        labeliki.setAttribute("for","cevap");
        var veritip_bir=document.createElement("input");
        veritip_bir.setAttribute("type","radio");
        veritip_bir.setAttribute("class","cevap");
        veritip_bir.setAttribute("name","cevap1");
        veritip_bir.setAttribute("value","text");
        var veritip_iki=document.createElement("input");
        veritip_iki.setAttribute("type","radio");
        veritip_iki.setAttribute("class","cevap");
        veritip_iki.setAttribute("name","cevap1");
        veritip_iki.setAttribute("value","tam sayı");
        var veritip_uc=document.createElement("input");
        veritip_uc.setAttribute("type","radio");
        veritip_uc.setAttribute("class","cevap");
        veritip_uc.setAttribute("name","cevap1");
        veritip_uc.setAttribute("value","ondalıklı sayı");
        sayfamesajlari.appendChild(div_tip);
        document.getElementById("tipsecim").appendChild(document.createTextNode("Metin"));
        document.getElementById("tipsecim").appendChild(veritip_bir);
        document.getElementById("tipsecim").appendChild(document.createTextNode("Tam Sayı"));
        document.getElementById("tipsecim").appendChild(veritip_iki);
        document.getElementById("tipsecim").appendChild(document.createTextNode("Ondalıklı Sayı"));
        document.getElementById("tipsecim").appendChild(veritip_uc);
        document.getElementById("tipsecim").appendChild(document.createElement("br"));
        var nitelikalmalabeli=document.createElement("label");
        nitelikalmalabeli.setAttribute("for","nitelikalma");
        nitelikalmalabeli.innerText="Nitelik: (Secilen Veri Tipine Dikkat Ediniz";
        var nitelikalmainput=document.createElement("input");
        nitelikalmainput.setAttribute("id","nitelikalma");
        nitelikalmainput.setAttribute("value","Nitelik");
        document.getElementById("tipsecim").appendChild(nitelikalmalabeli);
        document.getElementById("tipsecim").appendChild(document.createElement("br"));
        document.getElementById("tipsecim").appendChild(nitelikalmainput);
        document.getElementById("tipsecim").appendChild(document.createElement("br"));
        //ekle butonu
        var uygula_buton=document.createElement("input");
        uygula_buton.setAttribute("type","submit");
        uygula_buton.innerText="Ekle";
        uygula_buton.setAttribute("onclick","window['"+this.id_nosu+"'].sagakolonekleson('"+v+"')");
        document.getElementById("tipsecim").appendChild(uygula_buton);
      }
      sagakolonekleson(m){
        var kolonadi = document.getElementById("kolonadiduzenle").value;
        var kolonniteligi=document.getElementById("nitelikalma").value;
        var key_list=Object.keys(this.properties);
        var iii;
        try {
            var veri_tip=document.querySelector('input[name = cevap1]:checked').value;
            if (document.querySelector('input[name = cevap1]:checked').value==="text"){
              kolonniteligi=kolonniteligi.toString();
            }
            else if(document.querySelector('input[name = cevap1]:checked').value==="tam sayı"){
              kolonniteligi=parseInt(kolonniteligi);
              if (isNaN(kolonniteligi)){
                kolonniteligi=null;
  
              }
            }
            else if(document.querySelector('input[name = cevap1]:checked').value==="ondalıklı sayı"){
              kolonniteligi=parseFloat(kolonniteligi);
              if (isNaN(kolonniteligi)){
                kolonniteligi=null;
              }
            }
            for (iii in key_list){
              if (key_list[iii]===m){
                var kolonindexi=parseInt(iii)+1;
                var keyValues=Object.entries(this.properties);
                keyValues.splice(kolonindexi,0,[kolonadi,kolonniteligi]);
                this.properties=null;
                this.properties=Object.fromEntries(keyValues);
              }
            }
            window[this.id_nosu].oznitelikgoruntulemeveduzenleme();
            window[this.id_nosu].objeyiyenile(window[this.id_nosu]);
            }
            catch(err){
              for (iii in key_list){
              if (key_list[iii]===m){
                var kolonindexi=parseInt(iii)+1;
                var keyValues=Object.entries(this.properties);
                keyValues.splice(kolonindexi,0,[kolonadi,null]);
                this.properties=null;
                this.properties=Object.fromEntries(keyValues);
              }
            }
              console.log("Tip Seçilmeden İşlem Yapıldı. Kolon Tipi Aynı Kaldı");
              window[this.id_nosu].objeyiyenile(window[this.id_nosu]);
              window[this.id_nosu].oznitelikgoruntulemeveduzenleme();
            }
      }
      oznitelikicerikdegistir(i){
        var sayfamesajlari=document.getElementById("sayfamesajlari");
        sayfamesajlari.innerText="";
        sayfamesajlari.style.backgroundColor="black";
        var kolonicerik_bilgi=document.createElement("label");
        kolonicerik_bilgi.setAttribute("for","kolonicerikal");
        var icerikalma=document.createElement("input");
        icerikalma.setAttribute("id","kolonicerikal");
  
        if (typeof this.properties[i]==="string"){
          kolonicerik_bilgi.innerText="Kolon Veri Tipi: Metin";
          icerikalma.setAttribute("type","text");
          icerikalma.setAttribute("value",this.properties[i]);
        }
        else if (Number.isInteger(this.properties[i])===true){
          kolonicerik_bilgi.innerText="Kolon Veri Tipi: Tam Sayı";
          icerikalma.setAttribute("type","number");
          icerikalma.setAttribute("value",this.properties[i]);
        }
        else if (typeof this.properties[i]!=="string" && Number.isInteger(this.properties[i])===false ){
          kolonicerik_bilgi.innerText="Kolon Veri Tipi: Ondalıklı Sayı";
          icerikalma.setAttribute("type","number");
          icerikalma.setAttribute("step","0.001");
          icerikalma.setAttribute("value",this.properties[i]);
  
        }
        sayfamesajlari.appendChild(kolonicerik_bilgi);
        sayfamesajlari.appendChild(document.createElement("br"));
        sayfamesajlari.appendChild(icerikalma);
        var degistir_buton=document.createElement("input");
        degistir_buton.setAttribute("type","submit");
        degistir_buton.setAttribute("value","Değiştir");
        degistir_buton.setAttribute("onclick","window['"+this.id_nosu+"'].oznitelikicerikdegistir_butonlaal('"+i+"','"+kolonicerik_bilgi.innerText+"')");
        sayfamesajlari.appendChild(degistir_buton);
      }
      oznitelikicerikdegistir_butonlaal(i,b){
        var aaa=document.getElementById("kolonicerikal").value;
        if (b==="Kolon Veri Tipi: Metin"){
          this.properties[i]=aaa.toString();
        }
        else if (b==="Kolon Veri Tipi: Tam Sayı"){
          this.properties[i]=parseInt(aaa);
        }
        else if (b==="Kolon Veri Tipi: Ondalıklı Sayı"){
          this.properties[i]=parseFloat(aaa);
        }
      document.getElementById(i+"iceriksummary").innerText=this.properties[i];
      bekleme();
      }    
      oznitelikpenceresikapat(){
        document.getElementById('sayfamesajlari').style.backgroundColor  = "unset";
        document.getElementById('sayfamesajlari').innerText = "";
        document.getElementById("oznitelikpenceresi").innerText="";
        document.getElementById("oznitelikpenceresi").style.backgroundColor="unset  ";
      }
    }
  
  async function katman_sil(i){
    document.getElementById('sayfamesajlari').style.backgroundColor  = "black";
    document.getElementById('sayfamesajlari').innerText = "Katman Siliniyor";
    await sleep(500);
    document.getElementById('sayfamesajlari').innerText = "Katman Silindi";
    await sleep(500);
    document.getElementById('sayfamesajlari').style.backgroundColor  = "unset";
    document.getElementById('sayfamesajlari').innerText = "";
    window[i].haritadansil();
    delete window[i];
    document.getElementById(i).remove();
  }

  //-------------------url olup olmadığına dair kontrol 
var elm;
function isValidURL(u){
  if(u!==""){
      if(!elm){
      elm = document.createElement('input');
      elm.setAttribute('type', 'url');
      }
  elm.value = u;
  return elm.validity.valid;
  }
  else{
      console.log("Url Adresi Boş Girilemez.");
  }
}
//----
const symbol_list={
    agac:{"point_sembols/tree_black.png":"Ağaç"},
    havaalani:{"point_sembols/airport_black.png":"Hava Alanı"},
    lamba:{"point_sembols/lamba.png":"Lamba"},
    liman:{"point_sembols/liman.png":"Liman"},
    fabrika:{"point_sembols/fabrika.png":"Fabrika"}
    };
    var renk_listesi = [
    ' #f8f8ff ',
    ' #f5f5f5 ',
    ' #dcdcdc ',
    ' #ffffff ',
    ' #000000 ',
    ' #808080 ',
    ' #908f8f ',
    ' #666666 ',
    ' #5f5f5f ',
    ' #696969 ',
    ' #dddddd ',
    ' #d3d3d3 ',
    ' #bebebe ',
    ' #1c1c1c ',
    ' #363636 ',
    ' #4f4f4f ',
    ' #696969 ',
    ' #828282 ',
    ' #9c9c9c ',
    ' #b5b5b5 ',
    ' #cfcfcf ',
    ' #e8e8e8 ',
    ' #a9a9a9 ',
    ' #778899 ',
    ' #708090 ',
    ' #c6e2ff ',
    ' #b9d3ee ',
    ' #9fb6cd ',
    ' #6c7b8b ',
    ' #2f4f4f ',
    ' #97ffff ',
    ' #8deeee ',
    ' #79cdcd ',
    ' #528b8b ',
    ' #4a804d ',
    ' #6f804a ',
    ' #8b658b ',
    ' #eee8aa ',
    ' #fffaf0 ',
    ' #fafad2 ',
    ' #8b4513 ',
    ' #a0522d ',
    ' #fdf5e6 ',
    ' #faf0e6 ',
    ' #ffefd5 ',
    ' #ffebcd ',
    ' #ffe4b5 ',
    ' #cd853f ',
    ' #f5f5dc ',
    ' #f4a460 ',
    ' #fffafa ',
    ' #eee9e9 ',
    ' #cdc9c9 ',
    ' #8b8989 ',
    ' #fff5ee ',
    ' #eee5de ',
    ' #cdc5bf ',
    ' #8b8682 ',
    ' #faebd7 ',
    ' #ffefdb ',
    ' #eedfcc ',
    ' #cdc0b0 ',
    ' #8b8378 ',
    ' #ffe4c4 ',
    ' #eed5b7 ',
    ' #cdb79e ',
    ' #8b7d6b ',
    ' #ffdab9 ',
    ' #eecbad ',
    ' #cdaf95 ',
    ' #8b7765 ',
    ' #ffdead ',
    ' #eecfa1 ',
    ' #cdb38b ',
    ' #8b795e ',
    ' #fffacd ',
    ' #eee9bf ',
    ' #cdc9a5 ',
    ' #8b8970 ',
    ' #fff8dc ',
    ' #eee8cd ',
    ' #cdc8b1 ',
    ' #8b8878 ',
    ' #fffff0 ',
    ' #eeeee0 ',
    ' #cdcdc1 ',
    ' #8b8b83 ',
    ' #f5fffa ',
    ' #f0fff0 ',
    ' #e0eee0 ',
    ' #c1cdc1 ',
    ' #838b83 ',
    ' #fff0f5 ',
    ' #eee0e5 ',
    ' #cdc1c5 ',
    ' #8b8386 ',
    ' #e6e6fa ',
    ' #ffe4e1 ',
    ' #eed5d2 ',
    ' #cdb7b5 ',
    ' #8b7d7b ',
    ' #f0ffff ',
    ' #e0eeee ',
    ' #c1cdcd ',
    ' #838b8b ',
    ' #f0f8ff ',
    ' #8470ff ',
    ' #7b68ee ',
    ' #6a5acd ',
    ' #836fff ',
    ' #7a67ee ',
    ' #6959cd ',
    ' #473c8b ',
    ' #483d8b ',
    ' #4169e1 ',
    ' #4876ff ',
    ' #436eee ',
    ' #3a5fcd ',
    ' #27408b ',
    ' #0000ff ',
    ' #0000ee ',
    ' #00008b ',
    ' #1c0f45 ',
    ' #000080 ',
    ' #191970 ',
    ' #6495ed ',
    ' #0000cd ',
    ' #b0e0e6 ',
    ' #087EB0 ',
    ' #1e90ff ',
    ' #1c86ee ',
    ' #1874cd ',
    ' #104e8b ',
    ' #4682b4 ',
    ' #63b8ff ',
    ' #5cacee ',
    ' #4f94cd ',
    ' #36648b ',
    ' #00bfff ',
    ' #00b2ee ',
    ' #009acd ',
    ' #00688b ',
    ' #87ceeb ',
    ' #87ceff ',
    ' #7ec0ee ',
    ' #6ca6cd ',
    ' #4a708b ',
    ' #87cefa ',
    ' #b0e2ff ',
    ' #a4d3ee ',
    ' #8db6cd ',
    ' #607b8b ',
    ' #b0c4de ',
    ' #cae1ff ',
    ' #bcd2ee ',
    ' #a2b5cd ',
    ' #6e7b8b ',
    ' #add8e6 ',
    ' #bfefff ',
    ' #b2dfee ',
    ' #9ac0cd ',
    ' #68838b ',
    ' #1b8bb4 ',
    ' #e0ffff ',
    ' #d1eeee ',
    ' #b4cdcd ',
    ' #7a8b8b ',
    ' #5f9ea0 ',
    ' #98f5ff ',
    ' #8ee5ee ',
    ' #7ac5cd ',
    ' #53868b ',
    ' #afeeee ',
    ' #bbffff ',
    ' #aeeeee ',
    ' #96cdcd ',
    ' #668b8b ',
    ' #48d1cc ',
    ' #00ced1 ',
    ' #40e0d0 ',
    ' #00f5ff ',
    ' #00e5ee ',
    ' #00c5cd ',
    ' #00868b ',
    ' #00ffff ',
    ' #00eeee ',
    ' #00cdcd ',
    ' #008b8b ',
    ' #1c6071 ',
    ' #7fffd4 ',
    ' #76eec6 ',
    ' #66cdaa ',
    ' #458b74 ',
    ' #8fbc8f ',
    ' #c1ffc1 ',
    ' #b4eeb4 ',
    ' #9bcd9b ',
    ' #698b69 ',
    ' #2e8b57 ',
    ' #54ff9f ',
    ' #4eee94 ',
    ' #43cd80 ',
    ' #98fb98 ',
    ' #9aff9a ',
    ' #90ee90 ',
    ' #7ccd7c ',
    ' #548b54 ',
    ' #00ff7f ',
    ' #00ee76 ',
    ' #00cd66 ',
    ' #008b45 ',
    ' #00ff00 ',
    ' #00ee00 ',
    ' #00cd00 ',
    ' #008b00 ',
    ' #006400 ',
    ' #4ba123 ',
    ' #3cb371 ',
    ' #20b2aa ',
    ' #90ee90 ',
    ' #7cfc00 ',
    ' #00fa9a ',
    ' #adff2f ',
    ' #32cd32 ',
    ' #9acd32 ',
    ' #228b22 ',
    ' #7fff00 ',
    ' #76ee00 ',
    ' #66cd00 ',
    ' #458b00 ',
    ' #6b8e23 ',
    ' #c0ff3e ',
    ' #b3ee3a ',
    ' #9acd32 ',
    ' #698b22 ',
    ' #556b2f ',
    ' #caff70 ',
    ' #bcee68 ',
    ' #a2cd5a ',
    ' #6e8b3d ',
    ' #fff68f ',
    ' #eee685 ',
    ' #cdc673 ',
    ' #8b864e ',
    ' #bdb76b ',
    ' #eedd82 ',
    ' #ffec8b ',
    ' #eedc82 ',
    ' #cdbe70 ',
    ' #8b814c ',
    ' #ffffe0 ',
    ' #eeeed1 ',
    ' #cdcdb4 ',
    ' #8b8b7a ',
    ' #ffff00 ',
    ' #eeee00 ',
    ' #cdcd00 ',
    ' #8b8b00 ',
    ' #ffc000 ',
    ' #ffd700 ',
    ' #eec900 ',
    ' #cdad00 ',
    ' #8b7500 ',
    ' #ffe413 ',
    ' #daa520 ',
    ' #ffc125 ',
    ' #eeb422 ',
    ' #cd9b1d ',
    ' #8b6914 ',
    ' #b8860b ',
    ' #ffb90f ',
    ' #eead0e ',
    ' #cd950c ',
    ' #bc8f8f ',
    ' #ffc1c1 ',
    ' #eeb4b4 ',
    ' #cd9b9b ',
    ' #8b6969 ',
    ' #cd5c5c ',
    ' #ff6a6a ',
    ' #ee6363 ',
    ' #cd5555 ',
    ' #8b3a3a ',
    ' #ff8247 ',
    ' #ee7942 ',
    ' #cd6839 ',
    ' #8b4726 ',
    ' #deb887 ',
    ' #ffd39b ',
    ' #eec591 ',
    ' #cdaa7d ',
    ' #8b7355 ',
    ' #f5deb3 ',
    ' #ffe7ba ',
    ' #eed8ae ',
    ' #cdba96 ',
    ' #8b7e66 ',
    ' #d2b48c ',
    ' #ffa54f ',
    ' #ee9a49 ',
    ' #cd853f ',
    ' #8b5a2b ',
    ' #d2691e ',
    ' #ff7f24 ',
    ' #ee7621 ',
    ' #cd661d ',
    ' #8b4513 ',
    ' #b22222 ',
    ' #ff3030 ',
    ' #ee2c2c ',
    ' #cd2626 ',
    ' #8b1a1a ',
    ' #a52a2a ',
    ' #ff4040 ',
    ' #ee3b3b ',
    ' #cd3333 ',
    ' #8b2323 ',
    ' #fa8072 ',
    ' #ff8c69 ',
    ' #ee8262 ',
    ' #cd7054 ',
    ' #8b4c39 ',
    ' #ffa07a ',
    ' #ee9572 ',
    ' #cd8162 ',
    ' #8b5742 ',
    ' #ffa500 ',
    ' #ee9a00 ',
    ' #cd8500 ',
    ' #8b5a00 ',
    ' #ee7e15 ',
    ' #ff8c00 ',
    ' #ff7f00 ',
    ' #ee7600 ',
    ' #cd6600 ',
    ' #8b4500 ',
    ' #f08080 ',
    ' #ff7f50 ',
    ' #ff7256 ',
    ' #ee6a50 ',
    ' #cd5b45 ',
    ' #8b3e2f ',
    ' #ff6347 ',
    ' #ee5c42 ',
    ' #cd4f39 ',
    ' #8b3626 ',
    ' #ff4500 ',
    ' #ee4000 ',
    ' #cd3700 ',
    ' #cc5a11 ',
    ' #ff0000 ',
    ' #ee0000 ',
    ' #cd0000 ',
    ' #a40000 ',
    ' #8b0000 ',
    ' #c60000 ',
    ' #dc143c ',
    ' #ff1493 ',
    ' #ee1289 ',
    ' #cd1076 ',
    ' #8b0a50 ',
    ' #ff69b4 ',
    ' #ff6eb4 ',
    ' #ee6aa7 ',
    ' #cd6090 ',
    ' #8b3a62 ',
    ' #ffc0cb ',
    ' #ffb5c5 ',
    ' #eea9b8 ',
    ' #cd919e ',
    ' #8b636c ',
    ' #ffb6c1 ',
    ' #ffaeb9 ',
    ' #eea2ad ',
    ' #cd8c95 ',
    ' #8b5f65 ',
    ' #db7093 ',
    ' #ff82ab ',
    ' #ee799f ',
    ' #cd6889 ',
    ' #8b475d ',
    ' #800000 ',
    ' #b03060 ',
    ' #ff34b3 ',
    ' #ee30a7 ',
    ' #cd2990 ',
    ' #8b1c62 ',
    ' #d02090 ',
    ' #ff3e96 ',
    ' #ee3a8c ',
    ' #cd3278 ',
    ' #8b2252 ',
    ' #ff00ff ',
    ' #ee00ee ',
    ' #cd00cd ',
    ' #8b008b ',
    ' #da70d6 ',
    ' #ff83fa ',
    ' #ee7ae9 ',
    ' #cd69c9 ',
    ' #8b4789 ',
    ' #dda0dd ',
    ' #ffbbff ',
    ' #eeaeee ',
    ' #cd96cd ',
    ' #8b668b ',
    ' #ba55d3 ',
    ' #e066ff ',
    ' #d15fee ',
    ' #b452cd ',
    ' #7a378b ',
    ' #9932cc ',
    ' #bf3eff ',
    ' #b23aee ',
    ' #9a32cd ',
    ' #68228b ',
    ' #c71585 ',
    ' #ee82ee ',
    ' #9400d3 ',
    ' #8a2be2 ',
    ' #800080 ',
    ' #a020f0 ',
    ' #9b30ff ',
    ' #912cee ',
    ' #7d26cd ',
    ' #551a8b ',
    ' #9370db ',
    ' #ab82ff ',
    ' #9f79ee ',
    ' #8968cd ',
    ' #5d478b ',
    ' #d8bfd8 ',
    ' #ffe1ff ',
    ' #eed2ee ',
    ' #cdb5cd ',
    ' #8b7b8b ',
    ' #ddc488 ',
    ' #ffde66 ',
    ' #ecab53 ',
    ' #c0c0c0 ',
    ' #008080 ',
    ' #ffcc99 '
    ];
    