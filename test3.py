"""
 * Project name(项目名称)：Python实例方法_静态方法和类方法
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 21:10
 * Version(版本): 1.0
 * Description(描述)： Python类静态方法
 静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间（类命名空间）中，而函数则定义在程序所在的空间（全局命名空间）中。
静态方法没有类似 self、cls 这样的特殊参数，因此 Python 解释器不会对它包含的参数做任何类或对象的绑定。也正因为如此，类的静态方法中无法调用任何类属性和类方法。
 """


class C:
    @staticmethod
    def f1():
        """
        静态方法
        :return:
        """
        print("静态方法")


if __name__ == '__main__':
    c = C()
    c.f1()
    C.f1()
