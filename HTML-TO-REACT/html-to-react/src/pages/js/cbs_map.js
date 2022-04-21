async function bekleme(){
    await sleep(500)
    document.getElementById('sayfamesajlari').style.backgroundColor  = "unset";
    document.getElementById('sayfamesajlari').innerText ="";
    
  }

  // bekletme fonksiyonu
  function sleep(ms)  {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  //baslangic fonksiyonu
  
  async function baslangic(){
    
    await sleep(500);
    document.getElementById('sayfamesajlari').style.backgroundColor  = "black";
    document.getElementById('sayfamesajlari').innerText = "Çizim Ekranı Oluşturuluyor..";
  
    await sleep(2500);
    document.getElementById('map_screen').style.backgroundColor = "white";
    show_coordints()
    await sleep(800);
    document.getElementById('sayfamesajlari').innerText ="............";
    await sleep(500)
    document.getElementById('sayfamesajlari').style.backgroundColor  = "unset";
    document.getElementById('sayfamesajlari').innerText =""
    
  }
  
  baslangic()
  
  // Fetch all the details element. // üst sekmelerden birini açınca diğerinin kapanması
  const details = document.querySelectorAll("details");
  
  // Add the onclick listeners.
  details.forEach((targetDetail) => {
    targetDetail.addEventListener("click", () => {
      // Close all the details that are not targetDetail.
      details.forEach((detail) => {
        if (detail !== targetDetail) {
          detail.removeAttribute("open");
        }
      });
    });
  });
  
  