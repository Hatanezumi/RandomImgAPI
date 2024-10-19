# -*- coding: utf-8 -*-
'''
@Author  : Hatanezumi
@Contact : Hatanezumi@chunshengserver.cn
'''
from src import main
from waitress import serve

debug = True

if debug:
    main.app.run(port=80, debug=True)
else:
    serve(main.app, host='0.0.0.0', port=80)