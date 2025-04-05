import matplotlib.pyplot as plt

#Histograms
ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89,12,6,9,48,68,18]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages,bins,histtype="bar",rwidth=0.8)
plt.xlabel("bins")
plt.ylabel("ages")
plt.show()

#Scatter Graph
x = [1,2,3,4,5,6,7,8,9]
y = [0,1,0,1,0,1,0,1,0]

plt.scatter(x,y,color="blue",s=50,label="Scatter graph")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#Pie graph
slices = [23,45,15,7,2,8]
category = ["wind energy","Coal","Nuclear power","Bio","Solar","Tidal"]
col=["grey","black","green","purple","yellow","blue"]

plt.pie(slices,labels=category,colors=col)
plt.title("Source of energy")
plt.show()

#Stack plot
days = [1,2,3,4,5]
sleep = [8,6,7,4,10]
eating = [1,0.45,0.55,1,1.5]
studying = [2,3,2.5,2.7,2.3]
playing = [1.5,2.5,2,2.2,1.8]
plt.plot([],[],color="black",label="sleep")
plt.plot([],[],color="green",label="eating")
plt.plot([],[],color="blue",label="studying")
plt.plot([],[],color="red",label="playing")
plt.stackplot(days,sleep,eating,studying,playing,colors=["black","green","blue","red"])
plt.xlabel("days")
plt.ylabel("activity")
plt.legend() #adds a key
plt.show()

#sub plots
plt.subplot(221)
ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89,12,6,9,48,68,18]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages,bins,histtype="bar",rwidth=0.8)
plt.xlabel("bins")
plt.ylabel("ages")

plt.subplot(222)
x = [1,2,3,4,5,6,7,8,9]
y = [0,1,0,1,0,1,0,1,0]
plt.scatter(x,y,color="blue",s=50,label="Scatter graph")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(223)
slices = [23,45,15,7,2,8]
category = ["wind energy","Coal","Nuclear power","Bio","Solar","Tidal"]
col=["grey","black","green","purple","yellow","blue"]
plt.pie(slices,labels=category,colors=col)
plt.title("Source of energy")

plt.subplot(224)
days = [1,2,3,4,5]
sleep = [8,6,7,4,10]
eating = [1,0.45,0.55,1,1.5]
studying = [2,3,2.5,2.7,2.3]
playing = [1.5,2.5,2,2.2,1.8]
plt.plot([],[],color="black",label="sleep")
plt.plot([],[],color="green",label="eating")
plt.plot([],[],color="blue",label="studying")
plt.plot([],[],color="red",label="playing")
plt.stackplot(days,sleep,eating,studying,playing,colors=["black","green","blue","red"])
plt.xlabel("days")
plt.ylabel("activity")

plt.show()
