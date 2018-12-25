# encoding=utf-8

import random as r
import sys
from faker import Faker

#初始化 faker
fake = Faker (locale='zh_CN')
# 需要生成的数量
count = int(sys.argv[1])

# 银行信息
bank = '622588'
bank_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# 生成姓名
def random_name():
    name = fake.name()
    return name


# 生成手机号
def random_mobile():
    mobile = fake.phone_number() 
    return mobile


# 生成身份证号
def random_idcard():
    idcard =fake.ssn (min_age=18, max_age=70) 
    return idcard


def random_bankNum():
    bankNum = bank + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num)
    return bankNum


if __name__ == "__main__":
    for i in range (count):
        if int(sys.argv[3])==1:
            print (random_name () + "," + random_mobile () + "," + random_idcard () + "," + random_bankNum () + "," + "招商银行|CMB")
            with open(sys.argv[2],"a+") as f:
                f.write(random_name () + "," + random_mobile () + "," + random_idcard () + "," + random_bankNum () + "," + "招商银行|CMB\n")
                f.close()
        if int(sys.argv[3])==2:
            print (random_name () + "," + random_mobile () + "," + random_idcard () + "," + random_bankNum () + "," + random_bankNum () + "," +"招商银行|CMB")
            with open(sys.argv[2],"a+") as f:
                f.write(random_name () + "," + random_mobile () + "," + random_idcard () + "," + random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB\n")
                f.close()
        if int(sys.argv[3])==3:
            print (random_name () + "," + random_mobile () + "," + random_idcard () + "," + random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB")
            with open(sys.argv[2],"a+") as f:
                f.write(random_name () + "," + random_mobile () + "," + random_idcard () + "," + random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB\n")
                f.close()
        if int(sys.argv[3])==4:
            print (random_name () + "," + random_mobile () + "," + random_idcard () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + random_bankNum () + "," + "招商银行|CMB")
            with open(sys.argv[2],"a+") as f:
                f.write(random_name () + "," + random_mobile () + "," + random_idcard () + "," + random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB\n")
                f.close()
        if int(sys.argv[3])==5:
            print (random_name () + "," + random_mobile () + "," + random_idcard () + "," + random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB")
            with open(sys.argv[2],"a+") as f:
                f.write(random_name () + "," + random_mobile () + "," + random_idcard () + "," + random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB\n")
                f.close()
