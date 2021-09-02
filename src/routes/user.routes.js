module.exports = app => {

    const express = require('express');
    const user_controller = require('../controllers/user.controllers');

    const router = express.Router();

    router.get('/', user_controller.list);
    router.post('/', user_controller.create);

    router.get('/:id', user_controller.retrieve);
    router.delete('/:id', user_controller.destroy);
    router.put('/:id', user_controller.update);
    router.patch('/:id', user_controller.partial_update);

    app.use('/api/user', router);
};