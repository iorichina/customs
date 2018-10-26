# -*- coding: utf-8 -*-

import export2file

csv_file = export2file.export2file()
csv_file.init("customs67735.csv", 'gbk')
boundary = '----WebKitFormBoundaryXVBkrQ2Hq3TUBnAG'
boundary_form = '--' + boundary
# source or excel
csv_format = 'excel'


def setCsvFormat(csv_f):
    global csv_format
    csv_format = csv_f


def exportTitle(document):
    global csv_format
    # print('exportTitle')
    selecterth = '#ess_ctr182767_TariffContentSearch_gvSearch > tr.headStyle > th'
    # print(document.select(selecterth))
    title = '页码'
    for thidx in range(1, 7):
        thstr = document.select(
            selecterth + ':nth-of-type('+str(thidx)+')')[0].string
        if "excel" == csv_format and thstr.startswith('-'):
            title += ',="' + thstr + '"'
        else:
            title += ','+thstr
    title += '\n'
    csv_file.write(title)


def exportPage(document):
    global csv_format
    # print('exportPage')
    selectertr = '#ess_ctr182767_TariffContentSearch_gvSearch > tr'
    for tr in document.select(selectertr):
        if 'class' in tr.attrs and 'headStyle' in tr.attrs['class']:
            pass
        else:
            if len(tr.select('td')) <= 1:
                pass
            else:
                # print(tr)
                selecterpageindex = '#ess_ctr182767_TariffContentSearch_gvSearch_ctl23_lblCurrentPage'
                selectertd = 'td:nth-of-type'
                content = document.select(selecterpageindex)[0].string
                for tdidx in range(1, 7):
                    tdstr = tr.select(selectertd+'('+str(tdidx)+')')[0].string
                    if "excel" == csv_format and tdstr.startswith('-'):
                        content += ',="' + tdstr + '"'
                    else:
                        content += ',' + tdstr
                content += '\n'
                csv_file.write(content)


def finish():
    csv_file.close()


def getFormHeaders():
    DEFAULT_REQUEST_HEADERS = {
        'Host': 'www.customs.gov.cn',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://www.customs.gov.cn',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': "multipart/form-data; boundary=" + boundary,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://www.customs.gov.cn/tabid/67735/default.aspx',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': '.ASPXANONYMOUS=2nCOI3mf1AEkAAAAOGY5MGM4OGUtOTFlOC00ZGJhLTk1NjEtOWVjMThhOGY3NTFi0; language_0=en-US'
    }
    return DEFAULT_REQUEST_HEADERS


def getFormBody(page_index):
    body = boundary_form + '''
Content-Disposition: form-data; name="__EVENTTARGET"


'''+boundary_form+'''
Content-Disposition: form-data; name="__EVENTARGUMENT"


'''+boundary_form+'''
Content-Disposition: form-data; name="__VIEWSTATE"

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
'''+boundary_form+'''
Content-Disposition: form-data; name="ScrollTop"


'''+boundary_form+'''
Content-Disposition: form-data; name="__essVariable"


'''+boundary_form+'''
Content-Disposition: form-data; name="ess$ctr182767$TariffContentSearch$txtCodeTs"


'''+boundary_form+'''
Content-Disposition: form-data; name="ess$ctr182767$TariffContentSearch$txtGName"


'''+boundary_form+'''
Content-Disposition: form-data; name="ess$ctr182767$TariffContentSearch$gvSearch$ctl23$txtRd"

'''+str(page_index)+'''
'''+boundary_form+'''
Content-Disposition: form-data; name="ess$ctr182767$TariffContentSearch$gvSearch$ctl23$btnRd"

跳转
'''+boundary_form+'''
Content-Disposition: form-data; name="select"

中国政府网
'''+boundary_form+'''
Content-Disposition: form-data; name="select1"

国务院部门网站
'''+boundary_form+'''
Content-Disposition: form-data; name="select2"

地方政府网站
'''+boundary_form+'''
Content-Disposition: form-data; name="select3"

驻港澳机构网站
'''+boundary_form+'''
Content-Disposition: form-data; name="select4"

世界海关组织
'''+boundary_form+'''
Content-Disposition: form-data; name="select5"

在京直属事业单位
'''+boundary_form+'''
Content-Disposition: form-data; name="select6"

社会团体
'''+boundary_form+'''
Content-Disposition: form-data; name="select6"

资讯网
'''+boundary_form+'''
Content-Disposition: form-data; name="select8"

媒体
'''+boundary_form+'--'
    return body
