const express = require('express');
const cors = require('cors');
const morgan = require('morgan');

const db = require('./models');
const user_routes = require('./routes/user.routes');


const app = express();

app.use(cors({ origin: '*' }));

db.sequelize.sync({ force: true }).then(() => {
  console.log("Drop and re-sync db");
});

// setup the logger
app.use(morgan('dev'));

// parse requests of content-type - application/json
app.use(express.json());

// parse requests of content-type - application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true }));

// simple route
app.get("/healthcheck", (req, res) => {
  res.json({ message: "OK" });
});

// Registar todas as rotas
user_routes(app);


// set port, listen for requests
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on: http://localhost:${PORT}`);
});
