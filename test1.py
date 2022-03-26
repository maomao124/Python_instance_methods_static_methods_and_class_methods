"""
 * Project name(项目名称)：Python实例方法_静态方法和类方法
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 21:03
 * Version(版本): 1.0
 * Description(描述)： 实例方法
 通常情况下，在类中定义的方法默认都是实例方法
 类的构造方法理论上也属于实例方法，只不过它比较特殊。
 """


class C:
    def __init__(self):
        print("__init__实例方法")

    def f1(self):
        print("f1实例方法")


if __name__ == '__main__':
    c = C()
    c.f1()
    # Python 也支持使用类名调用实例方法，但此方式需要手动给 self 参数传值
    C.f1(c)
