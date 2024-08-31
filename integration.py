import matplotlib.pyplot as plt

x = []
y = []
start_point = 1
endpoint = 2
for parts in range(2 , 1000):

    length = endpoint-start_point
    delta_x = length/parts  #length
    area =0
    dist = delta_x  

    for i in range(parts):

        quadfun_val = ((start_point+ dist)**2)*delta_x

        dist= dist+ delta_x

        area +=quadfun_val
    x.append(parts)
    y.append(area)


plt.plot(x,y , color = 'red')
print(min(y))
x=[]
y =[]

for parts in range(2 , 1000):

# parts = 3

    length = endpoint-start_point

    delta_x = length/parts  #length

    area =0

    dist = 0  

    for i in range(parts):

        quadfun_val = ((start_point+ dist)**2)*delta_x

        dist= dist+ delta_x

        area +=quadfun_val


    x.append(parts)
    y.append(area)


print(max(y))


plt.title("Area function of $x^2$", weight='bold')


plt.xlabel('\u0394x --> 0', weight='bold')
plt.ylabel('Area', weight='bold')


plt.plot(x,y , color = 'blue')
plt.show()