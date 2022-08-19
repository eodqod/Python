from urllib import parse

url = parse.urlparse('https://brownbears.tistory.com?name=불곰&params=123')

query = parse.parse_qs(url.query)
result = parse.urlencode(query, doseq=True)
print(query)
print(result)

# {'name': ['불곰'], 'params': ['123']}
# name=%EB%B6%88%EA%B3%B0&params=123

print(parse.quote("한사람"));
print(parse.unquote(parse.quote("한사람")));

# %ED%95%9C%EC%82%AC%EB%9E%8C
# 한사람