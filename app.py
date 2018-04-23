import flask
import views
import conf

app =flask.Flask(__name__)


law_prefix = "/api/v1/law"
app.register_blueprint(views.web_law, url_prefix=law_prefix)

shop_prefix="/api/v1/shop"
app.register_blueprint(views.api_shop,url_prefix=shop_prefix)

user_prefix="/api/v1/usercenter"
app.register_blueprint(views.api_user,url_prefix=user_prefix)

if __name__ == '__main__':
    app.run(debug=True,port=5006,host='0.0.0.0')