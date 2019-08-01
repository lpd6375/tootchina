#一个简单的数据展示实现
本项目用作简单的数据展示，读取远程数据库中的数据并进行可视化。使用到的技术如下：

- Django 2.2
- Python 3.7
- PyEcharts
- BootStrap
- Mysql 5.7

##说明
原本打算把数据库中的表导入进 Django 的Models 模型中，但发现其数据查询方式满足不了项目的实际需求，
于是改为使用 SQL 进行查询，处理完结果后把数据进行格式化后再由 PyEcharts 进行渲染然后返回给前端。
