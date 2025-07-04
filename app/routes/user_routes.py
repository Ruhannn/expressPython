from ..controllers.user_controllers import (register_user, login, get_users, get_user)

def handel_user_routes(app):
    # register user (options and post)
    @app.options("/register")
    def route(req):
         req.send(204, "")

    @app.post("/register")
    def route(req):
        return register_user(req)


    # register user (options and post)
    @app.options("/login")
    def route(req):
         req.send(204, "")

    @app.post("/login")
    def route(req):
        return login(req)

    # get user by id
    @app.get("/get-user/:id")
    def route(req):
        return get_user(req)

    # get users
    @app.get("/get-users")
    def route(req):
        return get_users(req)
