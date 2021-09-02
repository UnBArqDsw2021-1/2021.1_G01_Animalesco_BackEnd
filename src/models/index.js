module.exports = (app) => {

    const Sequelize = require('sequelize');

    const sequelize = new Sequelize(
        process.env.POSTGRES_DB,
        process.env.POSTGRES_USER,
        process.env.POSTGRES_PASSWORD,
        {
            host: process.env.POSTGRES_HOST,
            dialect: 'postgres',
            operatorsAliases: false,
        }
    );

    const db = {};

    db.Sequelize = Sequelize;
    db.sequelize = sequelize;

    // Injeção de dependências
    db.User = require('./user.model')(sequelize, Sequelize);
    // Other models here

    db.sequelize.sync({ force: true }).then(() => {
        console.log("Drop and re-sync db");
    });

    return db;
};