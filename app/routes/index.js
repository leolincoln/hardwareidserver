// routes/index.js

const idRoutes = require('./id_routes');

module.exports = function(app,db){

    idRoutes(app,db);
};
