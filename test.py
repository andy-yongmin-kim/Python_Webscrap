import requests

r = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84+%EB%84%A4%EC%9D%B4%EB%B2%84&oquery=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94&tqi=U%2Ff0fsp0Jy0sshQVvblssssst1G-211338')

print(r.text)