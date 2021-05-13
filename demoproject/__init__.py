# 配置mysql，取代默认的mysqldb

import pymysql
#修改版本号，防止报错
pymysql.version_info = (1,4,13,'final',0)
pymysql.install_as_MySQLdb()