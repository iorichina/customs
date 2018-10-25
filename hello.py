import page67735
import requests
from bs4 import BeautifulSoup

hello = "hello"
python = "进出口税则查询"
print(hello, python, sep='-')

page_url = 'http://www.customs.gov.cn/tabid/67735/default.aspx'

page_session = requests.Session()
response = page_session.get(page_url)
document = BeautifulSoup(response.text, 'html.parser')
total_page_str = document.select(
    '#ess_ctr182767_TariffContentSearch_gvSearch_ctl23_lblPageCount')[0].string
print('共'+total_page_str+'页')
print('1. 第' + document.select('#ess_ctr182767_TariffContentSearch_gvSearch_ctl23_lblCurrentPage')
      [0].string + '页')

page67735.exportTitle(document)
page67735.exportPage(document)

page_headers = page67735.getFormHeaders()
total_page = int(total_page_str)
for page_index in range(2, total_page + 1):
    page_body = page67735.getFormBody(page_index)
    try:
        response = page_session.post(
            page_url, headers=page_headers, data=page_body.encode("utf-8"))
    except Exception:
        try:
            response = page_session.post(
                page_url, headers=page_headers, data=page_body.encode("utf-8"))
        except Exception:
            try:
                response = page_session.post(
                    page_url, headers=page_headers, data=page_body.encode("utf-8"))
            except Exception:
                response = page_session.post(
                    page_url, headers=page_headers, data=page_body.encode("utf-8"))
    document = BeautifulSoup(response.text, 'html.parser')
    print(str(page_index)+'. 第' + document.select(
        '#ess_ctr182767_TariffContentSearch_gvSearch_ctl23_lblCurrentPage')[0].string + '页')
    page67735.exportPage(document)

page67735.finish()

# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)
# print(response.content)
# print(response.content.decode("utf-8"))
