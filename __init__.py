from app_config import app
import controller
from flask import render_template

app.register_blueprint(controller.admin_bp, url_prefix='/admin')
app.register_blueprint(controller.adv_bp, url_prefix='/adv')
app.register_blueprint(controller.driver_bp, url_prefix='/driver')


@app.route('/')
def index():
    return render_template('default.html')


if __name__ == '__main__':
    app.run(debug=True)
