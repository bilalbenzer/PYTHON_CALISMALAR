


import {get as getProjection} from 'ol/proj';
import {getTopLeft, getWidth} from 'ol/extent';

const projection = getProjection('EPSG:2320');
const projectionExtent = projection.getExtent();
const size = getWidth(projectionExtent) / 256;
const resolutions = new Array(19);
const matrixIds = new Array(19);
for (let z = 0; z < 19; ++z) {
  // generate resolutions and matrixIds arrays for this WMTS
  resolutions[z] = size / Math.pow(2, z);
  matrixIds[z] = z;
}



console.log(projection)