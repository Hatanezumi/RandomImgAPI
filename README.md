# 随机图片API

*只是简单的实现了*

## 访问

使用`GET`方法访问`<你的域名>/random`即可获取一个随机图片

### 参数
| 参数 | 值 | 含义| 默认 |
| ---- | -- | ---- | ---- |
| json | True/False | 是否返回Json | False |
| redirect | True/False | 是否重定向至图片链接 | False |
| store_name | [store_name] | 指定图片库 | pics |


## 部署方法

pip安装Flask, waitress

将代码拉取下来

在根目录(`run.py`所在的目录)下创建`imgs`并在`imgs`下创建`pics`文件夹

将图片放入`pics`文件夹

__将`run.py`中的`debug = True`改为`debug = False`__

运行`run.py`

访问`localhost:80`

## 添加库

在`src`下创建新的库

将`src\Constant.py`中的`STORENAMES`添加新的库名