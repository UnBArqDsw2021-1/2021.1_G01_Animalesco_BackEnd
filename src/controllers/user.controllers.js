const db = require('../models');

const User = db.User;

exports.list = async(req, res) => {
    res.json({msg: 'ok'});
};

exports.create = async(req, res) => {
    res.json({msg: 'ok'});
};

exports.retrieve = async(req, res) => {
    res.json({msg: "OK"});

    // const id = req.params.id;
    // try {
    //     const user = await User.FindByPk(id);
    // }

    // catch(error) {
    //     res.status(500);
    //     res.json({ message: `Error retrieving User with id = ${id}` });
    // }
};

exports.update = async(req, res) => {
    res.json({msg: "OK"});
};

exports.partial_update = async(req, res) => {
    res.json({msg: "OK"});
};

exports.destroy = async(req, res) => {
    res.json({msg: "OK"});
};

