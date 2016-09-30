# coding=utf-8

import requests

headers = { 
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "dataType": "json",
    "Connection": "keep-alive",
    "contentType": "application/json;charset=UTF-8",
    "Referer": "http://zzfws.bjjs.gov.cn/enroll/home.jsp",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko)",
}

def login_do(cookies):
    url = 'http://zzfws.bjjs.gov.cn:80/enroll/dyn/login.json'
    postdata = {
        'username' : 'chinyy',
        'password' : '784512963c',
        'checkcode' : '',
    }
    post_do(url, postdata, cookies)

def check_code(cookies):
    url = 'http://zzfws.bjjs.gov.cn:80/enroll/dyn/checkcode.json'
    postdata = {
        'active_type': '2',
    }
    post_do(url, postdata, cookies)

def post_do(url, payload, cookies):
    s = requests.session()
    response = s.post(url, params=payload, headers=headers, cookies=cookies)

    print response.content

def get_cookies(url):
    r = requests.get(url, headers=headers)
    return r.cookies

if __name__ == '__main__':
    cookies = get_cookies("http://zzfws.bjjs.gov.cn/enroll/home.jsp") 
    #login_do(cookies)
    check_code(cookies)
