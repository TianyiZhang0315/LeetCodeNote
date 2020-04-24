#sql基础知识点

#表格设计的第一到第三范式和BCNF（boyce codd normal form）ref：https://www.zhihu.com/question/24696366
# 总结：
# 1NF： 字段是最小的的单元不可再分 （不能出现‘地址’这种可以分的列）
# 2NF：满足1NF,表中的字段必须完全依赖于全部主键而非部分主键 (例如系主任依赖于（学号，课名）中的学号，是依赖于部分主键，主键也称为码，所以将大表拆为小表来解决）
# 3NF：满足2NF,非主键外的所有字段必须互不依赖（消除传递函数依赖，例如系主任依赖于系名，而系名依赖于学号，将这个依赖的连锁拆开即可）
# 4NF：满足3NF,消除表中的多值依赖（例如仓库表格中，仓库名（主属性）依赖于（管理员，物品名）这个码，实际上是消除主属性对于码的部份依赖，产生的原因是仓库名和管理员
# 实际上为一对一，在这个表中保留其一即可）

# 一些最重要的 SQL 命令
# SELECT - 从数据库中提取数据
# UPDATE - 更新数据库中的数据
# DELETE - 从数据库中删除数据
# INSERT INTO - 向数据库中插入新数据
# CREATE DATABASE - 创建新数据库
# ALTER DATABASE - 修改数据库
# CREATE TABLE - 创建新表
# ALTER TABLE - 变更（改变）数据库表
# DROP TABLE - 删除表
# CREATE INDEX - 创建索引（搜索键）
# DROP INDEX - 删除索引

# INSERT INTO table_name (column, column1, column2, column3, ...)
# VALUES (value, value1, value2, value3 ...)
#
# UPDATE table_name
# SET column=value, column1=value1,...
# WHERE someColumn=someValue（类似于query之后执行）
#
# DELETE FROM tableName
# WHERE someColumn = someValue
#
# CREATE UNIQUE INDEX index_name
# ON table_name ( column1, column2,...columnN);
#
# TRUNCATE TABLE table_name;（清空表，与delete的直接将表删除不同）

#rollback可以回滚 insert, update和delete这种改变内容的语句，不能回滚create或drop