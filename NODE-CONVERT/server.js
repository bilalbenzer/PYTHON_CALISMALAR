// Load Node modules
var express = require('express');
const ejs = require('ejs');
// Initialise Express
var app = express();
// Render static files
app.use(express.static('views/static'));
// Set the view engine to ejs
app.set('view engine', 'ejs');
// Port website will run on
app.listen(1453);
// *** GET Routes - display pages ***
// Root Route
app.get('/', function (req, res) {
    res.render('pages/anasayfa');
});
app.get('/anasayfa', function (req, res) {
    res.render('pages/anasayfa');
});
app.get('/cbs_map', function (req, res) {
    res.render('pages/cbs_map');
});