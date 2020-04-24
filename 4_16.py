#今天学pyspark
from pyspark import SparkContext,SparkConf
import re
COMMA_DELIMITER = re.compile(''',(?=(?:[^"]*"[^"]*")*[^"]*$)''')
def splitComma(line:str)->str:
    splits = COMMA_DELIMITER.split(line)
    return "{},{}".format(splits[0],splits[1])
if __name__ == "__main__":
    # sc = SparkContext("local[3]","word_count")
    # sc.setLogLevel("ERROR")
    # lines = sc.textFile("in/word_count.txt")
    # words = lines.flatMap(lambda line:line.split(" "))
    # wordc = words.countByValue()
    # for word,count in wordc.items():
    #     print("{}:{}".format(word,count))
#每次创建一个新的RDD分布式储存单元，lines = sc.textFile("in/word_count.txt")，这里Lines就是
#每个RDD可以被transform，然后take action
#transform主要有两种，filter（function）和map（function），例如filter(lambda line：line.strip（）)
#map（）的返回类型不需要和输入类型一样，例如length = lines.map（lambda line: len(line)）

    conf = SparkConf().setAppName("airports").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    airports = sc.textFile("in/fake_airport.txt")
    print(airports)
    #这个分隔符号会检测到两组引号之间的逗号，但不会检测到一组引号之内的逗号
    filtered = airports.filter(lambda line : COMMA_DELIMITER.split(line)[0] == "1")
    res = filtered.map(splitComma)
    res.saveAsTextFile("out/save4_16.txt")
#map的结果会存储在文件夹里的part文件


