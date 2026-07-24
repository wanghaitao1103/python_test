redaFile = open('test.yaml', 'r+')
readContent = redaFile.read()
print('first read:', readContent)
redaFile.write('ceshi:890')
redaFile.seek(0)  # 重置文件指针到开头
newContent = redaFile.read()
print('second read:', newContent)
redaFile.close()




