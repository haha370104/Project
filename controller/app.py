from flask import Blueprint

from model.adv import adv_info

app_bp = Blueprint('app', __name__)


@app_bp.route('/get_all_advs')
def get_all_adv():
    advs = adv_info.query.all()
    ajax = []
    for adv in advs:
        dic = {}
        dic['adv_ID'] = adv.adv_ID
        dic['points'] = adv.location
        ajax.append(dic)
    return str(ajax)


