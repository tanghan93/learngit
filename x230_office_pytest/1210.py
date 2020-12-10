import json
from json import loads,load
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
import random
import time

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
plt.grid(alpha=0.4)
x_tick_labe=['{}yearold'.format(i) for i in x]
plt.legend(loc='upper right')
plt.xticks(x,x_tick_labe,rotation=45)
plt.show()
'''

'''
x = np.arange(1,100)

fig,axes = plt.subplots(2,2)
ax1 = axes[0,0]
ax2 = axes[0,1]
ax3 = axes[1,0]
ax4 = axes[1,1]

fig = plt.figure(figsize=(20,10),dpi=80)

ax1.plot(x,x)
ax2.plot(x,-x)
ax3.plot(x,x**2)
ax3.grid(color='r',linestyle='--',linewidth=1,alpha=0.3)
ax4.plot(x,np.log(x))
plt.show()
'''

'''
x = np.arange(0,100)

fig = plt.figure(figsize=(20,10),dpi=80)

ax1 = fig.add_subplot(2,2,1)

ax1.plot(x,x)
ax3 = fig.add_subplot(2,2,2)
ax3.plot(x,x**2)
ax3.grid(color='r',linestyle='--',linewidth=1,alpha=0.3)
ax4=fig.add_subplot(2,2,3)
ax4.plot(x,np.log(x))
plt.show()
'''

'''
y = []
x=range(1,32)
for i in range(1,32):
    y.append(random.randint(11,32))
    ++i

print(y)

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y,label='Machr',marker='o')

x_ticks_labels =['March/{}'.format(i) for i in x]

plt.xticks(x[::3],x_ticks_labels[::3],rotation=45)
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Chart')
plt.legend(loc='upper right')
plt.show()
'''

'''
a= ['Fast & Furious','God Father','Captain America：The First Avenger','Iron Man','baiThe Shawshank Redemption','Casablanca']
b = [38.13,19.84,13.98,11.38,4.5,6.47]

rects = plt.bar(range(len(a)),b,width=0.3,color='red')
plt.xticks(range(len(a)),a,rotation=45)
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2,height+0.3,str(height),ha="")

plt.show()
'''

'''
time =[]
for i in range(1,100):
    time.append(random.randint(1,100))
    ++i
print(time)

plt.figure(figsize=(20,8),dpi=100)
distance =2
group_name = int((max(time)-min(time))/distance)

plt.hist(time,bins=group_name)

plt.xticks(range(min(time),max(time))[::2])

plt.grid(linestyle="--",alpha=0.5)

plt.xlabel("Film Length")
plt.ylabel("Film Count")
plt.show()
'''

'''
label_list = ["Part One","Part tow","Part, three"]

size =[55,35,10]

color = ['red','green','blue']

explode = [0,0.05,0]

patches,l_text,p_text = plt.pie(
    size,explode=explode,colors=color,
    labels=label_list,labeldistance=1.1,autopct="%1.1f%%",
    shadow=False,startangle=90,pctdistance=0.6
)
plt.axis("equal")
plt.legend()
plt.show()
'''

a = []
for i in  range(10000000000):
    a.append(random.random())

t1 =time.time()
sum1=sum(a)
t2 =time.time()

b=np.array(a)
t4=time.time()
sum3 =np.sum(b)
t5 =time.time()
print(t2-t1,t5-t4)







