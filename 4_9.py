#反转字符串中的单词顺序
#首先split,剩下有效单词和""
#遍历split后的列表
def rev(s):
    return " ".join(reversed(s.split()))
#双指针，先strip去除前后空格，i从后向前遍历，j只有当i碰到空格后再碰到非空格时更新
#i位置的字符为空格时，s[i+1:j+1]放入列表
#设置一个bool，默认false，当i碰到空格并推入字符串时设置为true.
#当这个bool为true时，i遇到空格则不做任何事并跳过，只有当再遇到非空格时，j=i
#bool再次设置为false
#note:strip后字符串开头加一个空格，这样就不用为了i=0时设置特例
def rev2(s):
    s = s.strip()
    s = " "+s
    j = len(s)-1
    res = []
    find = False
    for i in range(len(s)-1,-1,-1):#逆向遍历
        if s[i] == " ":#当i遇到空格
            if not find:#非寻找j更新点的状态
                res.append(s[i+1:j+1])#推入
                find = True#进入寻找j更新点的状态
        else:#i遇到非空格
            if find:#若为寻找更新点的状态
                j = i#更新j
                find = False#返回非寻找状态

    return " ".join(res)
for item in rev2("a good   example"):
    print("----"+item+"----")
    
#不做第二题了，学习一些python类的魔术方法
#这里使用了__call__方法来使得实例可以像函数一样被调用
class enti:
    def __init__(self,x,y):
        self.x, self.y = x,y
    def __call__(self,x,y):
        self.x, self.y = x,y
a = enti(1,2)
print(a.x)
a(2,1)
print(a.x)

#使用__enter__和__exit__来使得类可以使用with.... as...
#exit方法同时可以处理一些异常，如果异常被成功处理，返回true
class Closer:
'''通过with语句和一个close方法来关闭一个对象的会话管理器'''

def __init__(self, obj):
    self.obj = obj

def __enter__(self):
    return self.obj # bound to target

def __exit__(self, exception_type, exception_val, trace):
    try:
        self.obj.close()
    except AttributeError: # obj isn't closable
        print 'Not closable.'
        return True
#后面几行为前面类的例子
##>>> from magicmethods import Closer
##>>> from ftplib import FTP
##>>> with Closer(FTP('ftp.somesite.com')) as conn:
##...     conn.dir()
##...
##>>> conn.dir()
##>>> with Closer(int(5)) as i:
##...     i += 1
##...
##Not closable.
    
#描述器discriptor
#是一个存储着变量的类,至少定义__del__。__get__或__set__其中的一个也需要被定义。
#另外的类可以作为owner拥有描述器的类
class Meter(object):
'''Descriptor for a meter.'''

    def __init__(self, value=0.0):
    self.value = float(value)
    def __get__(self, instance, owner):
    return self.value
    def __set__(self, instance, value):
    self.value = float(value)

class Foot(object):
    '''Descriptor for a foot.'''

    def __get__(self, instance, owner):
    return instance.meter * 3.2808
    def __set__(self, instance, value):
    instance.meter = float(value) / 3.2808

class Distance(object):
    '''Class to represent distance holding two descriptors for feet and
    meters.'''
    meter = Meter()
    foot = Foot()
#类的序列化以及逆序列化
#可以使用pickle存储一个类并且保存当前的状态，在类中定义_getstate_和_setstate_来
#决定序列化和逆序列化所存储和还原的状态
import time

class Slate:
    '''Class to store a string and a changelog, and forget its value when
    pickled.'''

    def __init__(self, value):
        self.value = value
        self.last_change = time.asctime()
        self.history = {}

    def change(self, new_value):
        # Change the value. Commit last value to history
        self.history[self.last_change] = self.value
        self.value = new_value
        self.last_change = time.asctime()

    def print_changes(self):
        print 'Changelog for Slate object:'
        for k, v in self.history.items():
            print '%s\t %s' % (k, v)

    def __getstate__(self):
        # Deliberately do not return self.value or self.last_change.
        # We want to have a "blank slate" when we unpickle.
        return self.history

    def __setstate__(self, state):
        # Make self.history = state and last_change and value undefined
        self.history = state
        self.value, self.last_change = None, None
