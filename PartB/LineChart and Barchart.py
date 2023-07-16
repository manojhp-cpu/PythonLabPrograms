import matplotlib.pyplot as plt

# BarChart
course = ['BCA', 'BCOM', 'BBA', 'MCOM']
student_admitted = [120, 140, 60, 40]
fig = plt.figure(figsize=(10, 5))
plt.bar(course, student_admitted, color='blue', width=0.4)
plt.xlabel('Course offered')
plt.ylabel('Number of student admitted')
plt.show()

# Line Chart
year = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
college_strength = [1600, 1400, 1200, 1000, 900, 700, 200]
college_strength.reverse()
plt.title('student strength of MIT FGC,Mysore')
plt.plot(year, college_strength, color='red', marker='o')
plt.show()
