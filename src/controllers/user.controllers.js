module.exports = (app, db) => {
    const User = db.User;
    const user_controller = {}

    user_controller.list = async(req, res) => {
        res.json({msg: 'ok'});
    };

    user_controller.create = async(req, res) => {
        res.json({msg: 'ok'});
    };

    user_controller.retrieve = async(req, res) => {
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

    user_controller.update = async(req, res) => {
        res.json({msg: "OK"});
    };

    user_controller.partial_update = async(req, res) => {
        res.json({msg: "OK"});
    };

    user_controller.destroy = async(req, res) => {
        res.json({msg: "OK"});
    };

    return user_controller;
};
