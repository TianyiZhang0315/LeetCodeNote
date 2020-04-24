#spark相关, 再做点SQL， 写到world tutorial 第十题
#udf：user defined function是spark的function，当需要使用spark来执行分布式运算时需要把
#python的function转化为udf

# example data
# df_pd = pd.DataFrame(
#     data={'integers': [1, 2, 3],
#      'floats': [-1.0, 0.5, 2.7],
#      'integer_arrays': [[1, 2], [3, 4, 5], [6, 7, 8, 9]]}
# )
# df = spark.createDataFrame(df_pd) #创建spark df
# df.printSchema()
# df.show()

# def square(x):
#     return x**2 #将这里改为return int(x**2) 来避免例如数据中的float类型使用该udf使产生null----（1）
# from pyspark.sql.types import IntegerType
# square_udf_int = udf(lambda z: square(z), IntegerType())#当定义udf时，需要提供函数返回的数据类型
#若函数返回的类型与udf的返回类型不同，该运算会产生null。解决办法为，将python函数的返回步骤种的数据类型和udf的返回类型相统一，查看（1）

#--------------------------------------------------------------#
#如果返回一个list，udf则应返回例如ArrayType(int())
#如果返回一个复合的类型，例如tuple中包含一个数字和一个字符，则使用StructType()函数去构造一个相同模板的数据结构，然后传给udf
#例如

# def convert_ascii(number):
#     return [number, string.ascii_letters[number]]
# array_schema = StructType([
#     StructField('number', IntegerType(), nullable=False),
#     StructField('letters', StringType(), nullable=False)
# ])
#
# spark_convert_ascii = udf(lambda z: convert_ascii(z), array_schema)
#--------------------------------------------------------------------#
#常见error，Py4JJavaError，原因是python函数输出类型与udf不符，常发生于第三方lib自带的类，例如np.array
#如果udf执行过慢，尝试使用repartition()重新划分数据

#----------------------------------------------------------------------#
#pandas在一个列的数据基础上创建另一列
# df["bee1"] = df.bee.apply(lambda x:x+1)
#在spark里应转化为udf再创建新列
# import pyspark.sql.functions as F #使用udf需要先import
# fn = F.udf(lambda x:x+1, DoubleType())
# df.withColumn("bee1",fn(df.bee))

#pandas合并两个df，使用merge(left_df,right_df,on = key, how = [inner,left,right,outter])
#spark使用join(参数相同)
#若以不同的key来合并，pandas left.merge(right,left_on = "a", right_on = "b")
#spark left.join(right, left.a == right.b)

#pivot table透视表相当于一个筛选并展示数据的表格，详见https://zhuanlan.zhihu.com/p/31952948
#pd.pivot_table(df,index = [列名称，作为索引],value = [列名称，作为内容], aggfunc = [聚合方式，可用np.sum等]，\
# colmuns = [列名称，是列层次，比如放入城市在列可得到每个城市的sum])
#与groupby类似，下面的两行等价
# pd.pivot_table(df,index=[字段1],values=[字段2],aggfunc=[函数],fill_value=0)
# df.groupby([字段1])[字段2].agg(函数).fillna(0)

#生成表后可以使用query来进一步过滤数据
#table.query('列名 == ["具体列"]')

#spark pivot: df.groupBy("A", "B").pivot("c").sum("D")等价于
#pd.pivot_table(df,value = "D", index = ["A", "B"], columns = ["C"],aggfunc = np.sum)

#histogram pandas : df.hist()
#spark: df.sample(False, 0.1).toPandas().hist()

#SQL pandas：没有
#spark: df.createOrReplaceTempView("foo")
#df2 = spark.sql("select * from foo")