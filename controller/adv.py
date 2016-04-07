from flask import Blueprint, render_template, request, session, redirect, url_for, current_app
from model.adv import *
from datetime import datetime
import time
from werkzeug.utils import secure_filename
import os
import json
from model.LBS import *

app = current_app
adv_bp = Blueprint('adv', __name__)


@adv_bp.route('/')
def index():
    if 'adv_charge_name' not in session:
        return redirect(url_for('adv.login'))
    else:
        return redirect(url_for('adv.home'))


@adv_bp.route('/check_login', methods=['POST'])
def check_login():
    phone = request.form['phone']
    password = request.form['password']
    advter = adv_account.query.filter_by(phone=phone).first()
    if advter == None:
        return '<script>alert("用户名或密码错误");location.href="login"</script>'
    else:
        if advter.check(password):
            session['adv_account_id'] = advter.account_ID
            session['adv_charge_name'] = advter.charge_name
            # 这里应该写个token
            return '<script>location.href="/adv/home"</script>'
        else:
            return '<script>alert("用户名或密码错误");location.href="login"</script>'


@adv_bp.route('/check_adv_submit', methods=['POST'])
def check_adv_submit():
    print('123')
    adv_text = request.form['adv_text']
    adv_pic = request.files['adv_pic']
    adv_count = int(request.form['adv_count'])
    location = json.loads(request.form['location'])
    gcj02_loc = []
    for point in location:
        gcj02_loc.append(bd09togcj02(point[0], point[1]))
    date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    start_time = time.strptime(request.form['start_time'], '%H:%M')
    end_time = time.strptime(request.form['end_time'], '%H:%M')
    cost = float(request.form['cost'])
    adv_filename = secure_filename(adv_pic.filename)
    adv_pic.save((os.path.join(app.root_path, 'static/image/adv_pic', adv_filename)))
    adv = adv_info(cost, adv_count, date, start_time, end_time, str(gcj02_loc), session['adv_account_id'], adv_text,
                   adv_filename)
    db.session.add(adv)
    db.session.commit()
    return '<script>alert("发布成功");location.href="home"</script>'


@adv_bp.route('/adv_submit')
def adv_submit():
    return render_template('Users module/ad_submit.html', name=session['adv_charge_name'])


@adv_bp.route('/login')
def login():
    return render_template('Users module/login.html')


@adv_bp.route('/home')
def home():
    return render_template('Users module/ad_home.html', name=session['adv_charge_name'])
