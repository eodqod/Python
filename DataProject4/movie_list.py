import json

import requests

url = "https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"\
      "?key=f5eef3421c602c6cb7ea224104795888"

# 데이터 가져오기
r = requests.get(url)
# print(r.text)

# json으로 변환
data = json.loads(r.text)  ## python은 dict타입
# print(data)

print("전체개수 : ", data['movieListResult']['totCnt'], "개", sep="")

# itemPerPage=100&curPage=2
itemPerPage=100
total_page = (int(data['movieListResult']['totCnt'])-1)//itemPerPage + 1
print("전체페이지 : {}페이지".format(total_page))

# 저장할 리스트
mList = []
print("시간이 좀 걸립니다. 기다려 주세요!!!!")
for curPage in range(1, total_page+1):
      address = url + "&itemPerPage=100&curPage=" + str(curPage)
      # 데이터 가져오기
      r = requests.get(address)
      # print(r.text)
      # json으로 변환
      data = json.loads(r.text)  ## python은 dict타입
      movie_list = data['movieListResult']['movieList']
      for movie in movie_list:
            # 영화 1개의 정보를 저장할 맵
            mdict = {}
            # print(movie['movieNm'])
            mdict['movieNm'] = movie['movieNm']
            mdict['prdtYear'] = movie['prdtYear']
            mdict['nationAlt'] = movie['nationAlt']
            mdict['genreAlt'] = movie['genreAlt']
            mdict['typeNm'] = movie['typeNm']
            mdict['directors'] = movie['directors']
            # print(mdict)
            # 리스트에 추가
            mList.append(mdict)
      # 개수 출력
      # print(len(mList), "개 읽음")
print("전체 : ", len(mList), "개 읽음")

# json파일로 저장해보자
with open("./movie_list.json",'w') as file:
      json.dump(mList, file)
      print('저장완료!!!')


