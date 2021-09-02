// Módulo responsável por todas as configurações
module.exports = (app) => {

    // cors access
    const cors = require('cors');
    app.use(cors({ origin: '*' }));

    // setup the logger
    const morgan = require('morgan');
    app.use(morgan('dev'));

    const express = require('express');
    // parse requests of content-type - application/json
    app.use(express.json());
    // parse requests of content-type - application/x-www-form-urlencoded
    app.use(express.urlencoded({ extended: true }));
};