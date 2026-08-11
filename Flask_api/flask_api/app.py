from flask import Flask
from flask_api.routes.auth_route import auth_bp
from flask_api.routes.product_route import product_bp
from flask_api.helper_fun import *
app=Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
@app.before_request
def authenticate():
    if request.path == "/login":
        return 
    token=verify_token()
    if token == None:
        return {"message":"could'nt identify token"},401
    tokendata=token_data(token)
    if tokendata == None:
        return {"message":"invalid token"},401
    verified_token_data,error=validate_token_schema(tokendata)
    if error:
        return {"message":"invalid token"},401
    g.user=verify_user_presence(verified_token_data)
    if g.user==None:
        return {"message":"invalid user token"},401
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )