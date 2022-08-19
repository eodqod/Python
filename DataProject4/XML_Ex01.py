# XML 파일을 다뤄보자
# 1. 라이브러리 가져오기
import xml.etree.ElementTree as ET

# 2. 파일을 해석하기
tree = ET.parse('books.xml')

# 루트값 얻기
root = tree.getroot()

# 타입 출력
print(type(tree))
print(type(root))

# 태그와 속성을 확인하기
print(root.tag)
print(root.attrib)

# 자식노드 조회하기
for child in root:
    print(child.tag, child.attrib)

# 값 확인하기
# 첫번쨰 자식의 두번째 자식의 값 확인
print(root[0][1].text)

# 속성값 가져오기
book1  = root[0]  # 첫번째 자식 얻기
print(book1.get('id'))  # 속성의 값만
print(book1.keys())   # 속성의 key만 리스트로
print(book1.items())  # 속성의 (키,값) 튜플 리스트
print("-" * 50)

# 태그내의 text출력하기
for child in root[0]:
    print(child.tag, " : ", child.text)

print("-" * 50)
# 전체 텍스트 출력
for book_text in root[0].itertext():
    print(book_text)

print("-" * 50)

# 특정 태그 값에 해당하는 element 찾기
for book in root.findall('book'):
    author = book.find('author').text
    title = book.find('title').text
    genre = book.find('genre').text
    print(author," | ", title, " | ",genre)

print("-" * 50)
# 전체 내용 보기
print(ET.dump(tree))