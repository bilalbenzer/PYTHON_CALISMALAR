import React, { Component } from 'react';
import UstSekme from '../components/mainpage/Ustsekme';
import UstMenu  from '../components/mainpage/UstMenu';
import UstMenuContainer from '../components/mainpage/UstMenuContainer';
import MainPageAltKisim from '../components/mainpage/MainPageAltKisim';
import './MainPage.css'

export class MainPage extends Component {
  render() {
    return (
        <div>
        <UstSekme/>
        <UstMenu/>
        <UstMenuContainer/>
        <MainPageAltKisim/>
        </div>
    )   
  }
}

export default MainPage