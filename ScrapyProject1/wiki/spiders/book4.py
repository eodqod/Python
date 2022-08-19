import scrapy

class Book4Spider(scrapy.Spider):
  name = 'book4'
  allowed_domains = ['wikibook.co.kr']
  start_urls = [
    'https://wikibook.co.kr/list'
  ]

  def parse(self, response):
    li_list = response.css('.book-url')
    # 위키북스 사이트에 부담을 주지 않게 5개만 다운로드 합니다.
    for a in li_list[:5]:
      href = a.css('::attr(href)').extract_first()
      yield response.follow(
        response.urljoin(href), self.parse_book
      )

  def parse_book(self, response):
    title = response.url.split("/")[-2]
    img_url = response.css('.book-image-2d::attr(src)').extract_first()
    # 다운로드를 지시합니다. --- (※1)
    req = scrapy.Request(
      response.urljoin(img_url),
      callback=self.parse_img
    )
    # 함수끼리 데이터를 전송하는 방법입니다. --- (※2)
    req.meta["title"] = title
    yield req

  # 이미지 다운로드 --- (※3)
  def parse_img(self, response):
    print("이미지 정보 : ", response.meta)
    # 전달된 데이터를 받습니다. --- (※4)
    title = response.meta["title"]
    print("타이틀1 : ", title)
    # title = title.replace(r'[\/:*?"<>|.]+', '_').strip()
    # print("타이틀2 : ", title)
    fname = title + '.jpg'
    print("파일이름 : ", fname)
    # 파일을 저장합니다. --- (※5)
    with open(fname, 'wb') as f:
      f.write(response.body)
