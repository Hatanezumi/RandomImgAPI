# -*- coding: utf-8 -*-
'''
@Author  : Hatanezumi
@Contact : Hatanezumi@chunshengserver.cn
'''
import argparse
from src import main
from src.Constant import *
from waitress import serve

debug = True

parser = argparse.ArgumentParser()
parser.add_argument('--host', help='绑定的地址', default='0.0.0.0')
parser.add_argument('-p', '--port', help='绑定的端口', default=80, type=int)
parser.add_argument('--workdir', help='指定工作目录', default=None)
parser.add_argument('--hosturl', help='指定网站域名', default=None)
args = parser.parse_args()

if args.workdir is not None:
    BASEDIR = Path(args.workdir)
    IMGDIR = BASEDIR / 'imgs'
    main.imgdir = IMGDIR
if args.hosturl is not None:
    main.host_url = args.hosturl

if debug:
    main.app.run(port=args.port, debug=True)
else:
    serve(main.app, host=args.host, port=args.port)