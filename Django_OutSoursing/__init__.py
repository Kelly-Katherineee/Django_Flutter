import pymysql   #导入pymysql包，里面的所有功能便可以使用了，不需要单独一个个导入pymysql下的功能模块了
pymysql.install_as_MySQLdb()   #当成mysqldb使用，没有这个就会使用pymysql的方式，这个主要是便于之前2.x版本用习惯了mysqldb的人使用（3.x版本后无法使用mysqldb）