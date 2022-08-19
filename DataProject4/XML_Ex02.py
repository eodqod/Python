# XML로 저장하기

from xml.etree.ElementTree import Element, SubElement,ElementTree

# 루트 태그 만들기
root = Element("countries")
# 태그 만들기
element1 = Element("korea")
# 루트 태그에 자식으로 붙이기
root.append(element1)

# 자식태그 만들기
sub_element1 = SubElement(element1, 'City')
# 태그안에 내용 넣기
sub_element1.text = '서울'
# 태그에 속성 추가
sub_element1.set('attr1','값1')
sub_element1.set('attr2','값2')

element2 = Element("japanese")
root.append(element2)

sub_element2 = SubElement(element2, 'City')
sub_element2.text = 'Tokyo'
sub_element2.set('attr1','값1')
sub_element2.set('attr2','값2')

tree = ElementTree(root)
with open("ex.xml","wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)
    print("저장완료!!!")



