'''
utf-8
f = open('D:\\python\\test.txt', 'r')
f.read()
f.readline()
f.readlines()
f.read(size)
'abc\n中国\ncc'
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
f.close()
'''

'''
二进制文件
f = open('/Users/michael/test.jpg', 'rb')
f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节

'''
'''
gbk
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
f.read()
'''

'''
忽略错误编码
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
'''

'''
写文件
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
'''

'''
查看当前目录的绝对路径:
 os.path.abspath('.')
'/Users/michael'
在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
 os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
然后创建一个目录:
 os.mkdir('/Users/michael/testdir')
删掉一个目录:
os.rmdir('/Users/michael/testdir')
os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')

# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')

>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']

'''






















