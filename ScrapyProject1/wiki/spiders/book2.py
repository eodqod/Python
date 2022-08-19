import scrapy

class Book2Spider(scrapy.Spider):
  name = 'book2'
  start_urls = [
    'https://wikibook.co.kr/list/'
  ]

  def parse(self, response):
    # 도서 목록 추출하기 --- ( ※ 1)
    li_list = response.css('.book-url')  # 클래스이름이 book-url을 모두 찾는다.
    for a in li_list:  # 반복
      # href 속성과 텍스트 추출하기 --- ( ※ 2)
      href = a.css('::attr(href)').extract_first()  # 속성 찾기
      text = a.css('::text').extract_first()  # 내용 얻기
      # print(href, text)
      # 절대 경로로 변환하기 --- ( ※ 3)
      href2 = response.urljoin(href)
      # 결과 내기 --- ( ※ 4)
      yield {
        'text': text,
        'url': href2
      }
