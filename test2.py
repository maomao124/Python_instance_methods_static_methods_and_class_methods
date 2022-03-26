"""
 * Project name(项目名称)：Python实例方法_静态方法和类方法
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 21:06
 * Version(版本): 1.0
 * Description(描述)： Python类方法
 Python 类方法和实例方法相似，它最少也要包含一个参数，只不过类方法中通常将其命名为 cls，
 Python 会自动将类本身绑定给 cls 参数（注意，绑定的不是类对象）。也就是说，我们在调用类方法时，无需显式为 cls 参数传参。
 和 self 一样，cls 参数的命名也不是规定的,可以随意命名
 和实例方法最大的不同在于，类方法需要使用＠classmethod修饰符进行修饰
 如果没有 ＠classmethod，则 Python 解释器会将 fly() 方法认定为实例方法，而不是类方法。
 """


class C:

    def f1(self):
        """
        实例方法
        :return:
        """
        print("实例方法")

    @classmethod
    def f2(cls):
        """
        类方法
        :return:
        """
        print("类方法")


if __name__ == '__main__':
    c = C()
    c.f1()
    c.f2()
    C.f1(c)
    C.f2()
