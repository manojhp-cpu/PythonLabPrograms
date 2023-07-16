from matplotlib import pyplot as plt

course=['BCA','BCOM','BBA','MCOM']
result=[68,74,82,88]
ex=[0.2,0.1,0.1,0.1]
fig=plt.figure(figsize=(10,5))
plt.pie(result,labels=course,explode=ex)
plt.title('MIT First grade college Student Result')
plt.show()