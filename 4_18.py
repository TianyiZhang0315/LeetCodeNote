#今天继续学pyspark
#flatmap()和map()的区别是，当有N个RDD，map的返回数量与RDD数量相等，而flatmap返回数量为所有每一行的平铺
#sample(replacement是否放回, fraction抽样大小, seed随机种子)会在给定的RDD上随机抽样
#distinct()返回独特元素，非常耗时
#储存结果的文件夹里的part文件，每一个是一个运行单元的结果，可以是线程或是计算机
#parallelize(data)将输入的data转化为RDD

#Common actions:
#collect()取得RDD全部内容，可以先用filter建立新的小型RDD，然后储存在local
#count()数元素个数，countbyvalue数独特元素个数
#take(n)返回前n个元素
#saveAsTextFile()可以存储在本地或云端
#reduce(function)重复地执行function知道RDD被聚合为一个元素，例子[1,2,3,4,5].reduce(lambda x,y:x*y)会返回列表种元素的乘积
from pyspark import SparkContext,SparkConf
import re
COMMA_DELIMITER = re.compile(''',(?=(?:[^"]*"[^"]*")*[^"]*$)''')
def splitComma(line:str)->str:
    splits = COMMA_DELIMITER.split(line)
    return "{},{}".format(splits[0],splits[1])
if __name__ == "__main__":
    #flatmap()相关
    # sc = SparkContext("local[3]","word_count")
    # sc.setLogLevel("ERROR")
    # lines = sc.textFile("in/word_count.txt")
    # words = lines.flatMap(lambda line:line.split(" "))#这里如果使用map会返回包含每行单词的list，就没办法进行下一步的count
    # wordc = words.countByValue()
    # for word,count in wordc.items():
    #     print("{}:{}".format(word,count))
    #------------------------------------------#

    #union相关
    # conf = SparkConf().setAppName("union").setMaster("local[1]")
    # sc = SparkContext(conf = conf)
    # union1 = sc.textFile("in/union1.txt")
    # union2 = sc.textFile("in/union2.txt")
    # res = union1.intersection(union2)
    # res.saveAsTextFile("out/inter.csv")
    #---------------------------------------------#

    #collect()相关
    # conf = SparkConf().setAppName("collect").setMaster("local[1]")
    # sc = SparkContext(conf = conf)
    # words = ["a","b"]
    # rdd = sc.parallelize(words)
    # res = rdd.collect()
    # for re in res:
    #     print(re)
    #-----------------------------------------------#

    #提取RDD中前N个数字并求和
    # conf = SparkConf().setAppName("firstN").setMaster("local[*]")
    # sc = SparkContext(conf = conf)
    # lines = sc.textFile("in/number.txt")
    # num = lines.flatMap(lambda line: line.split(" "))
    # valid = num.filter(lambda number: number)#这里是因为前面如果有两个空格相连，
    #                                          #结果会得到空格，python中的空格会返回false，用这个lambda去掉空格
    # int_num =valid.map(lambda number:int(number))#转化为同一类型
    # res = int_num.reduce(lambda x,y:x+y)
    # print("sum:{}".format(res))
    #-------------------------------------------------#

    #用presist()储存生成的rdd以减少在原rdd上计算的次数
    # from pyspark import StorageLevel
    # conf = SparkConf().setAppName("firstN").setMaster("local[*]")
    # sc = SparkContext(conf = conf)
    # inputint = [1,2]
    # rdd = sc.parallelize(inputint)
    # rdd.persist(StorageLevel.MEMORY_ONLY)#这个rdd会出存在内存
    # rdd.reduce(lambda x,y:x+y)#第一次action
    # rdd.count()#第二次action会直接调用内存中rdd，而不是再次生成
    #对python来说，可以储存在disk或memory，对java和scala来说，额外的，可以储存为序列化对象
    #若内存已经达到上限，则使用LRU算法，即least recently used，释放最不常用的partition
    #无论怎样，spark不会因超出内存而抛出错误信息
    #------------------------------------------#

    #知识点复习map(function,data),filter(function,data),reduce(function,n)
    #返回data中每个元素输入function后的返回值
    #n = [1,2,3]
    #res = list(map(lambda x: 2*x, n))
    #等价于res = [2*x for x in n]

    #filter()相似于map()，使用lambda构筑一个条件来过滤data，只有满足条件的data中的元素会出现在结果中
    #res = list(filter(lambda x: x==2, n))
    #等价于res = [x for x in n if x == 2]

    #reduce()和spark的类似，需要一个多个输入元素的function，重复地将data输入这个function，最后返回一个元素
    #res = reduce(lambda x,y: x+y),res = 6
    import functools
    a = [1,2,3,4]
    print(functools.reduce(lambda x:2*x,a))


