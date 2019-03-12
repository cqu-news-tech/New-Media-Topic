# New-Media-Topic

重庆大学新闻网新媒体选题微信小程序

## 目录结构

```bash
.
├── client  #小程序前端代码
└── server  #小程序后端代码
    ├── docker  #Dockerfile目录
    ├── scripts
    │   ├── docker-compose.yml
    │   ├── Linux   #容器备份、迁移等脚本（待完成）
    │   └── windows #镜像打包、发布等脚本（待完成）
    └── src #小程序api
        ├── api.py  #入口文件
        ├── config.py   #flask配置文件
        ├── docker-entrypoint.sh    #Dockerfile ENTRYPOINT文件
        ├── gunicorn.conf   #gunicorn配置
        ├── Pipfile #pipenv依赖
        ├── Pipfile.lock
        ├── requirements.txt    #Pipfile导出的依赖文件
        ├── common  #数据模型定义、响应类、工具函数等
        └── resources   #API资源
            ├── admin   #管理员相关api
            ├── topic   #选题操作相关api
            └── user    #用户相关api
```
