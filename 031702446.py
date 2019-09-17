#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:dell
@file: 最终版.py
@time: 2019/09/{DAY}
"""
import re
import json

#李四,福建省福州13756899511市鼓楼区鼓西街道湖滨路110号湖滨大厦一层.
dic1 = {}
res = []
#切姓名和电话号码
str1 = input()
name = re.search('(.*?,)', str1)
phone_number = re.search('\d+', str1)
#print(name , phone_number)
#name.group()

name = re.sub(',', '', name.group())

dic1['姓名'] = name
dic1['手机'] = phone_number.group()

#名字电话号码用‘’替换
str2 = re.sub('\.', '', str1)
str2 = re.sub('(\d{5}\d+)', '', str2)
str2 = re.sub('(.*,)', '', str2)
#切地址

#直辖市
data = ['上海', '北京', '天津', '上海']

if (str2[:2]in data ):
    res.append(str2[:2])
    res.append(str2[:2]+'市')
    str2 = str2.replace(str2[:2]+'市', '', 1)
    county = re.search('.*?[县|区]', str2)
    if county == None:
        res.append('')
    else:
        res.append(county.group())
        str2 = re.sub('.*?[县|区]', '', str2)

    town = re.search('.*[街道|镇|乡]', str2)
    if town == None:
        res.append('')
    else:
        res.append(town.group())
        str2 = re.sub('.*[街道|镇|乡]', '', str2)

    road = re.search('.*[街|路|巷]', str2)
    if road == None:
        res.append('')
    else:
        res.append(road.group())
        str2 = re.sub('.*[街|路|巷]', '', str2)

    num = re.search('.*号', str2)
    if num == None:
        res.append('')
    else:
        res.append(num.group())
        str2 = re.sub('.*号', '', str2)


#省
else:
    provice = re.search('.*?省', str2)
    if provice == None:
        res.append(str2[0:2]+'省')

        str2= str2[2:]
    else:
        res.append(provice.group())
        str2 = re.sub('(.*省)', '', str2)
#市
    city = re.search('.*?市', str2)
    if city == None:
        res.append(str2[0:2]+'市')
        str2 = str2[2:]
    else:
        res.append(city.group())
        str2 = re.sub('.*?市', '', str2)

#区县
    county =re.search('.*?[县|区]', str2)
    if county == None:
        res.append('')
    else:
        res.append(county.group())
        str2 = re.sub('.*?[县|区]', '', str2)

#镇乡街道
    town = re.search('.*[街道|镇|乡]', str2)
    if town == None:
        res.append('')
    else:
        res.append(town.group())
        str2 = re.sub('.*[街道|镇|乡]','',str2)
#路
    road = re.search('.*?[街|路|巷]',str2)
    if road == None:
        res.append('')
    else:
        res.append(road.group())
        str2 = re.sub('.*?[街|路|巷]','', str2)

#号
    num = re.search('.*?号', str2)
    if num == None:
        res.append('')
    else:
        res.append(num.group())
        str2 = re.sub('.*?号', '', str2)



res.append(str2)

dic1['地址'] = res

j1 =json.dumps(dic1,ensure_ascii = False)
print(j1)