

# from abc import ABC, abstractmethod
# from dataclasses import dataclass
#
# @dataclass
# class A(ABC):
#     __na :str
#     __age :int
#     def __init__(self,na :str,age :int):
#         self.__na :str
#         self.__age :int
#
# @dataclass
# class B():
#     __na :str
#     __age :int
#     def __init__(self, na,age, course:str):
#         #super().__init__(na,age)
#         self.__na :str=na
#         self.__age :int=age
#         self.__course = course
#         # self.__getattribute__(
#         #     self.__na
#         # )
#
#     def check_method(self):
#         print(self.__na)
#         #print(self.__setattr__(self.__na, na))
#         #print(getattr(self.__class__,self.__na))
#         #print(self.__getattribute__(self.__na))
#
# if __name__ == '__main__':
#     res = B("dee",10, "python")
#     print(res.check_method())