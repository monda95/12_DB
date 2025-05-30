import requests
search =input("검색을 원하는 키워드를 입력해주세요 : ")
# ★★★★★ input 값으로 입력을 받게되면 무조건 데이터타입은 문자형이다

url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="

D = url + search

req = requests.get(D)

print(req.text)
