import React, { Component } from 'react';
import './UstSekme.css';
import logo from './static/logo.png'
export class UstSekme extends Component {
  render() {
    return (
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
    )
  }
}

export default UstSekme 