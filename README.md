# py_apollo_cli


## 入门使用:

* 见demo目录

## 功能点：
* apollo配置中心拉取配置
* 支持回调接口
* secret认证
* 支持灰度发布
* 支持本地文件缓存
* 默认开启热更新，参数配置可以不开启热更新
* 同时支持python2.x和python3.x，详情见./apollo/下的python_2x.py和python_3x.py文件



## Usage
```python

from py_apollo_cli import apollo

apollo.start(app_id="<app_id>", env="local")
client = apollo.get_config()

val = client.get_value("logger.config", default_val="{}")
print(val)

```
