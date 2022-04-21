import React from 'react'
import logo from './static/logo.png'
import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <React.Fragment>
        <div id="header"> 
        <div id="main_title">
          <div className="background">
          </div>
          <h1 id="main_head" >COĞRAFİ BİLGİ SİSTEMLERİ WEB UYGULAMASI</h1>
        </div>
        <div className="logo2">
          <img className="logo3" src={logo} alt="logo"/>
        </div>
      </div>
      <div id="nav"> 
        <ul style={{listStyle:"none"}}>
          <li id="homepage" ><Link to="/">ANASAYFA</Link></li>


          <li id="gis_view"><Link to="/Cbs_Map">HARİTA</Link></li>
          <li id="about_us">HAKKIMIZDA</li>
          <li id="contact">İLETİŞİM</li>
        </ul>
      </div>

      <div id="container">
        <div id="updates_and_news">
          <ol id="news">
            <li>Web Tasarımına Başlanıldı.</li>
            <li>asdasdasd</li>
            <li>asdasdasd</li>
          </ol>
        </div>
        <div id="images"></div>
      </div>

      <div id="footer"> 
        <p id="altyazi">Bu website, Bilal Benzer tarafından oluşturulmuştur.</p>
      </div>
    </React.Fragment>
  )
}
