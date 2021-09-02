const express = require('express');

const app = express();

// Configurações do servidor
settings_config = require('./config/settings');
settings_config(app);

const model_register = require('./models/index');
const db = model_register(app);

// Registro de endpoints do servidor
const urls_register = require('./routes/index.routes');
urls_register(app, db);

// set port, listen for requests
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on: http://localhost:${PORT}`);
});
