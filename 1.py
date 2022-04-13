from selenium import webdriver
from time import sleep

# https://blog.csdn.net/qq_38161040/article/details/108161221?spm=a2c6h.12873639.article-detail.12.1503ce4dStdDn8
# --remote-debugging-port=5003 --user-data-dir="C:\Py_selenium\auto"

# 另一个导入chrome参数的方法
# from selenium.webdriver.chrome.options import Options
# options = Options()

options = webdriver.ChromeOptions()
# 后台运行，不弹出浏览器
options.add_argument('--headless')
options.add_experimental_option("debuggerAddress", "127.0.0.1:5003")
# driver_path = "./chromedriver"
# options=options
bro = webdriver.Chrome(executable_path='./chromedriver', options=options)
# BV号 空格分隔
# 提取链接
# https://zhuanlan.zhihu.com/p/349819745?ivk_sa=1024320u
# for (var a of document.getElementsByTagName('a')) { console.log(a.href) }
names = []
li = names.split()
print(len(li))
c = 1
for i in li:
    bro.get('https://bilibili.com/' + i)
    print(bro.title)
    print(c)
    c = c + 1
    sleep(6)
    btn = bro.find_element_by_class_name('collect')
    sleep(1.5)
    btn.click()
    sleep(1.5)
    # 一个叫test的收藏夹
    btn = bro.find_element_by_xpath("//span[@title='test'][@class='fav-title']")
    btn.click()
    sleep(1.5)
    btn = bro.find_element_by_xpath("//button[@class='btn submit-move']")
    btn.click()
    sleep(1.5)

