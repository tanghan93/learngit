import json
from json import loads,load
import matplotlib.pyplot as plt

import random

'''
dict = {
    'Code':200,
    'Count':656,
    'Posts':[

        {
            'Id':0,
            'PostId':'1123178321664806912',
            'RecruitPostId':49691
        },
        {
            'Id':0,
            'PostId':"1123178321664806912",
            'RecruitPostId':49791
        }
    ]
}

json_dict = json.dumps(dict)
print(dict)
print('--------------')
print(json_dict)
print(type(json_dict))

with open('./a.json','w') as f:
    json_dict1 = json.dump(dict,fp=f)
    print(json_dict1)
    print(type(json_dict1))
'''

'''
dic = json.loads('{"name":"Tom","age":23}')
print(dic)
print(type(dic))

with open("./a.json","r",encoding='utf-8') as f:
    aa = json.load(f)
    print(aa)
    print(type(aa))
'''

#%matplotlib inline
'''
plt.plot([1,0,9],[4,5,6])

plt.show()
'''

'''
x =range(1,8)
y = [17,17,18,15,11,11,13]
y1 = []
i=0
while i<7:
    print(i)
    y1.append(random.randint(1,20))
    print(y1)
    i = i+1

print(type(y1))

plt.plot(y,y1,color='red',alpha=0.5,linestyle='--',linewidth=3,marker='o')
plt.show()

'''

'''
x =range(2,26,2)
#print(lambda :for i in  x)
y=[random.randint(15,30)for i in x]

plt.figure(figsize=(20,8),dpi=80)

#plt.xticks(range(1,25))
x_ticks_label=["{}:00".format(i) for i in x]
y_ticks_lable = ["{}C".format(i) for i in range(min(y),max(y)+1)]
plt.xticks(x,x_ticks_label,rotation=45)
plt.yticks(range(min(y),max(y)+1),y_ticks_lable)
plt.xlabel('x标题测试',fontproperties ='simHei',fontsize=20)
plt.ylabel('y标题测试',fontproperties ='simHei',fontsize=10)
plt.title('Title')
plt.plot(x,y)

#plt.savefig('./t1.png')
plt.show()
'''
i =0

y1 = []
y2 = []
while i<10:
    y1.append(random.randint(0,10))
    y2.append(random.randint(0,10))
    i =i+1

x =range(21,31)

plt.plot(x,y1,color='red',label='me')
plt.plot(x,y2,color='green',label='college')

x_tick_labe=['{}yearold'.format(i) for i in x]

plt.xticks(x,x_tick_labe,rotation=45)
plt.show()