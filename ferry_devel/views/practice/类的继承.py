#介绍
class Introduce:
    #类的初始化函数
    def __init__(self,Name,Age,Sex,Weight):
        self.ch_name = Name
        self.age = Age
        self.sex = Sex
        self.weight = Weight

    def introduce(self):
        print("大家好，我是%s，今年%d岁，性别%s，体重%.1f千克"
              %(self.ch_name,self.age,self.sex,self.weight))

#继承介绍类
class JieIntroduce(Introduce):
    hobby = "编程"
    def jie_introduce(self):
        print("大家好，我是%s，今年%d岁，性别%s，体重%.1f千克，爱好是%s。"
              %(self.ch_name,self.age,self.sex,self.weight,self.hobby))

j = JieIntroduce("罗凡林",25,"男",63)
j.jie_introduce()