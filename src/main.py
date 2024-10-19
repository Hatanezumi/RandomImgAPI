# -*- coding: utf-8 -*-
'''
@Author  : Hatanezumi
@Contact : Hatanezumi@chunshengserver.cn
'''
import json
import random
from PIL import Image
from .Constant import *
from flask import Flask, redirect, render_template, request, send_file, url_for

app = Flask(__name__)

imgdir = IMGDIR
host_url = None

@app.route('/')
def page_index():
    return redirect(url_for('page_random'))

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('page_404'))

@app.route('/404')
def page_404():
    return render_template('404.html'), 404

@app.route('/imgs/<store_name>/<img_name>', methods=['GET'])
def page_img(store_name: str, img_name:str):
    if store_name not in STORENAMES:
        return redirect(url_for('page_404'))
    store_dir = imgdir / store_name
    if not store_dir.exists() or not store_dir.is_dir():
        return redirect(url_for('page_404'))
    imgs = list(store_dir.iterdir())
    if img_name not in [i.name for i in imgs]:
        return redirect(url_for('page_404'))
    return send_file(store_dir / img_name)

@app.route('/random', methods=['GET'])
def page_random():
    store_name = request.args.get('store_name', default='pics')
    use_json = True if request.args.get('json', default='False') == 'True' else False
    use_redirect = True if request.args.get('redirect', default='False') == 'True' else False
    if store_name not in STORENAMES:
        return redirect(url_for('page_404'))
    store_dir = imgdir / store_name
    if not store_dir.exists() or not store_dir.is_dir():
        return redirect(url_for('page_404'))
    imgs = list(store_dir.iterdir())
    if len(imgs) == 0:
        return redirect(url_for('page_404'))
    img = random.choice(imgs)
    url = request.host_url if host_url is None else host_url
    url += f'imgs/{store_dir.name}/{img.name}'
    if not use_json: # 直接返回
        return (send_file(img), 200) if not use_redirect else redirect(url)
    width, height = Image.open(img).size
    dic = {
        'name': img.name,
        'width': width,
        'height': height,
        'url': url
    }
    return json.dumps(dic, ensure_ascii=False)
