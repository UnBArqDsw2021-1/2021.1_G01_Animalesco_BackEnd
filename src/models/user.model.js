module.exports = (sequelize, Sequelize) => {

    const User = sequelize.define("User", {
        email: {
            type: Sequelize.STRING,
            unique: true,
            allowNull: false,
        },

        username: {
            type: Sequelize.STRING,
            unique: true,
            allowNull: false,
        },

        password: {
            type: Sequelize.STRING,
            allowNull: false,
        }
    }, {});

    User.associate = function (models) {
        // associations can be defined here
    };

    return User;
};