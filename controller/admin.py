from flask import request, render_template, session, current_app, redirect, url_for, Blueprint
from model import db
from model.admin import admin_account
from model.driver import driver_account
from model.adv import *
import hashlib

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/')
@admin_bp.route('/home')
@admin_bp.route('/index.html')
def index():
    return render_template('Management module/index.html', name=session['admin_account_name'])


@admin_bp.route('/login')
def login():
    return render_template('Management module/login.html')


@admin_bp.route('/check_login', methods=['POST'])
def check_login():
    account_name = request.form['account']
    password = request.form['password']
    admin = admin_account.query.filter_by(account_name=account_name).first()
    if admin == None:
        return '<script>alert("用户名或密码错误");location.href="/admin/login"</script>'
    else:
        if admin.check(password):
            session['admin_account_id'] = admin.account_ID
            session['admin_account_name'] = admin.account_name
            return redirect(url_for('admin.index'))
        else:
            return '<script>alert("用户名或密码错误");location.href="/admin/login"</script>'


@admin_bp.route('/show_drivers')
def show_drivers():
    return render_template('Management module/drivers.html')


@admin_bp.route('/drivers_ajax')
def drivers_ajax():
    drivers = driver_account.query.all()
    ajax = []
    for driver in drivers:
        dic = {}
        dic["account_ID"] = driver.account_ID
        dic["user_name"] = driver.user_name
        dic["phone"] = driver.phone
        dic["check_flag"] = str(driver.check_flag)
        ajax.append(dic)
    return str(ajax)


@admin_bp.route('/show_driver/<int:ID>')
def show_driver(ID):
    if ID == None:
        return redirect(url_for('admin.show_drivers'))
    else:
        driver = driver_account.query.filter_by(account_ID=ID).first()
        return render_template('Management module/driver.html', phone=driver.phone, flag=str(driver.check_flag),
                               name=driver.user_name, user_id=driver.user_ID, permit_image=driver.permit_pic,
                               ID_card_image=driver.card_pic)


@admin_bp.route('/check_driver', methods=['GET'])
def check_driver():
    phone = request.args['phone']
    flag = bool(int(request.args['flag']))
    driver = driver_account.query.filter_by(phone=phone).first()
    driver.check_flag = flag
    db.session.commit()
    return "success"


@admin_bp.route('/show_advs')
def show_advs():
    return render_template('Management module/ads.html')

@admin_bp.route('/advs_ajax')
def advs_ajax():
    advs=adv_info.query.all()
    ajax=[]
    for adv in advs:
        dic={}
        dic['adv_ID']=adv.adv_ID
        dic['']

@admin_bp.route('/show_adv')
def show_adv():
    return render_template('Management module/ad.html')


@admin_bp.route('/show_advters')
def show_advters():
    return render_template('Management module/adusers.html')


@admin_bp.route('/advters_ajax')
def advters_ajax():
    advters = adv_account.query.all()
    ajax = []
    for advter in advters:
        dic = {}
        dic["account_ID"] = advter.account_ID
        dic["charge_name"] = advter.charge_name
        dic["company_name"] = advter.company_name
        dic["check_flag"] = str(advter.check_flag)
        ajax.append(dic)
    return str(ajax)


@admin_bp.route('/show_advter/<int:account_ID>')
def show_advter(account_ID):
    if account_ID == None:
        return redirect(url_for('admin.show_advters'))
    else:
        advter = adv_account.query.filter_by(account_ID=account_ID).first()
        return render_template('Management module/aduser.html', account_ID=account_ID, flag=advter.check_flag,
                               company=advter.company_name, amount=advter.adv_amount, name=advter.charge_name,
                               phone=advter.phone,remark=advter.remark)


@admin_bp.route('/check_advter', methods=['GET'])
def check_advter():
    account_ID = request.args['account_ID']
    flag = bool(int(request.args['flag']))
    advter = adv_account.query.filter_by(account_ID=account_ID).first()
    advter.check_flag = flag
    db.session.commit()
    return "success"
