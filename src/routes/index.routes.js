module.exports = (app, db) => {

    app.get("/healthcheck", (req, res) => {
        res.json({ message: "OK" });
    });

    // Registrando as rotas de User
    require('./user.routes')(app, db);

};