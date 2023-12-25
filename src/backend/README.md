# 启动命令
uvicorn app.main:app --reload

# 参考链接
https://fastapi.tiangolo.com/zh/tutorial/bigger-applications/#api

# 区分不同的环境
使用环境变量，赋予不同的值
```shell
export FASTAPI_ENV_FILE=.env.production
```

# alembic使用

安装
```bash
pip3 install alembic
```

初始化
```bash
alembic init alembic
```
修改alembic.ini文件

在文件中添加一行version_path_separator = os 和sqlalchemy.url 地址(如下图),其他地方不需要进行更改。

初始化数据库脚本
```shell
alembic revision --autogenerate -m "initial"
```

运行数据库脚本
```shell
alembic upgrade head
```