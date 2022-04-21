
import React from 'react'
import {BrowserRouter as  Router, Routes,  Route} from 'react-router-dom'
import Home from './Home'
import Cbs_Map from './Cbs_Map'

export default function RouterPage() {
  return (
    <div>
        <Router>
            <Routes>
                <Route exact path="/" element={<Home/>}/>
                <Route exact path="/Cbs_Map" element={<Cbs_Map/>}/>
            </Routes>
        </Router>
    </div>
  )
}

