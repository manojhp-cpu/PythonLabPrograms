# 11.Read and Write into File
file_path = '../read/ReadWritefile.txt'

with open(file_path, 'w') as file:
    file.write('Hello,World')
    file.write('I am coding in python\n')
    file.write('Artificial Intelligence\n')
print('Data written successful')

with open(file_path, 'r') as file:
    content = file.read()

print('content of the file')
print(content)
