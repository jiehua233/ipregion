## IP归属地查询

### 环境搭建 

安装依赖包

    $ pip install -r etc/requirements.txt 

从[17monip](http://www.ipip.net)中获取ip数据源

    $ python main.py --parse17monip

从[淘宝](http://ip.taobao.com)抓取详细ip数据

    $ python main.py --scrapytbip

将数据导入MySQL

    $ python main.py --loaddb

服务测试

    $ python server.py

采用gunicorn运行服务

    $ gunicorn server:app -c config.py

### 数据来源

* 基于17monip(www.ipip.net免费版数据库)
* 采集apnic的数据
* 采集淘宝IP库

### 查询结果

* 外国:只返回国家
* 中国:尽可能的详细......

