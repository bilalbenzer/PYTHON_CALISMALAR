import React, { Component } from 'react'
import './UstMenu.css'
export class UstMenu extends Component {
  render() {
    return (
        <div id="nav"> 
            <ul style={{listStyle: "none"}}>
                <a a href="index.html">
                    <li id="homepage" >ANASAYFA </li>
                </a>
                <a href="cbs_map.html">
                <li id="gis_view">HARİTA</li></a>
                <li id="about_us">HAKKIMIZDA</li>
                <li id="contact">İLETİŞİM</li>
            </ul>
      </div>
    )
  }
}

export default UstMenu