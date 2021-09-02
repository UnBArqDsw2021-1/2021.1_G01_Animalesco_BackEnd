module.exports = {
    HOST: process.env.POSTGRES_HOST || "postgres",
    USER: process.env.POSTGRES_USER || "postgres",
    PASSWORD: process.env.POSTGRES_PASSWORD || "postgres",
    DB: process.env.POSTGRES_DB || "postgres",
    dialect: "postgres",
};