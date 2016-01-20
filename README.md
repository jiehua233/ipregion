## IP归属地查询

### 环境搭建 

Infobright新建数据库

```sql
CREATE DATABASE IF NOT EXISTS `ipregion` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `ipregion`;
```

### 数据来源

* 基于17monip(www.ipip.net免费版数据库)
* 采集apnic的数据
* 采集淘宝IP库

### 查询结果

* 外国:只返回国家
* 中国:尽可能的详细......

