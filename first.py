# 把找到的链接做成字符串。
# 把这个字符串保存在url的变量中
# 使用requests的get功能 向URL发起请求 得到相应res

import requests

url = 'https://v2.kwaicdn.com/upic/2022/09/28/12/BMjAyMjA5MjgxMjAzMDlfMTQ5OTAwMDY2OF84NTE2Mzc4NTYwOV8xXzM=_hd15_B5e9ef64dc84d2f31aa62f1a6453880f1.mp4?pkey=AAVqv-G4A5IwbVMNKnGq9UgCpvtvk-J7ICgf05xloyQ1FGj4GMhJQUnIGhttRC3BCXIZJcezNofJFo3rNYiIlSXcKPDkj5HdJxnAJBVrRwzspN4EmiwvHRjn0YeMuvVc9wo&tag=1-1669637562-unknown-0-plaqusrza6-b85f1000ec2e08ee&clientCacheKey=3xxd9taat6yh584_hd15.mp4&di=ddd88ca7&bp=14944&tt=hd15&ss=vp'

res = requests.get(url)

# res-响应：响应是这个网址给我们的一堆数据
# res.status_code  # 响应码
# res.text         # 访问一个网页 给我们的源代码
# res.content      # 访问一个资源 给我们的二进制数据

print(res.content)  # 得到的视频的数据

# 创建一个空的视频文件--存储数据

# 文件的读和写 open('文件名'，'打开方式')
open('1.mp4', 'wb').write(res.content)
# 打开方式：
#                  文本txt     二进制 mp3 mp4 jpg png
# 读 从文件中读取数据 r(read)    rb()
# 写 向文件中写入数据 w(write)   wb()


