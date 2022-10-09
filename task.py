"""#Questions
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
1 . Try to reverse a list
2. try to access 234 out of this list
3 . try to access 456
4 . Try to extract only a list collection form list l
5 . Try to extract "sudh"
6 . Try to list all the key in dict element available in list
7 . Try to extract all the value element from dict available in list
"""
import logging
import logging as lg
lg.basicConfig(filename='log.log',level=lg.INFO,format = '%(name)s - %(asctime)s - %(levelname)s - %(message)s')
class task_to_perform:
    def __init__(self,input_list):
        self.input_list=input_list
    def logger(self,log):
        lg.info(log)
    def reverse_a_list(self):
        """reversing the list"""
        try:
            if type(self.input_list)==list:
                self.logger("reversed the list successfully")
                return self.input_list[::-1]

            else:
                 self.logger("failed to reversed the list")
        except Exception as e:
            self.logger(e)
    def int_extracter(self,int_input):
        try:
            for i in self.input_list:
                if type(i)==int:
                    if i==int_input:
                        self.logger("integer extracted")
                        return i
                if type(i)==list or type(i)==set or type(i)==dict:
                    for j in i:
                        if j==int_input:
                            return j
        except Exception as e:
            self.logger(e)
    def list_extractor(self):
        try:
            a=[]
            for i in self.input_list:
                if type(i)==list:
                    a.append(i)
                    for j in i:
                        if type(j)==list:
                            a.append(j)
                if type(i)==dict:
                    for j in i.values():
                        if type(j)==list:
                            a.append(j)
            return a
        except Exception as e:
            self.logger(e)
    def string_extractor(self,str_input):
        try:
            a=[]
            for i in self.input_list:
                if type(i)==str:
                    if i==str_input:
                        return i
                if type(i)==dict:
                    for j in i.keys():
                        if type(j)==str:
                            if j == str_input:
                                a.append(j)
                    for j in i.values():
                        if type(j)==str:
                            if j==str_input:
                                a.append(j)
                if type(i)==tuple:
                    for j in i:
                        if type(j)==str:
                            a.append(j)
            return a
        except Exception as e:
            self.logger(e)
    def dict_key_extracter(self):
        try:
            a=[]
            for i in self.input_list:
                if type(i)==dict:
                    for j in i.keys():
                        a.append(j)
            return a
        except Exception as e:
            self.logger(e)
    def dict_value_extracter(self):
        try:
            a=[]
            for i in self.input_list:
                if type(i)==dict:
                    for j in i.values():
                        a.append(j)

            return a
        except Exception as e:
            self.logger(e)
a=task_to_perform([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])
print(a.reverse_a_list())















