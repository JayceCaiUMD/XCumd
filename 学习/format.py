site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site)) #python中只有字典是映射型，format需要加**

my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{name}，地址 {url}".format(name="菜鸟教程",url="www.runoob.com"))