import requests
import os, csv

he = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "119",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "apache=bbfde8c184f3e1c6074ffab28a313c87; lss=f7cb2cf4b1607aec30e411e90d47c685; _ulta_id.CM-Prod.ccc4=855b5e34c5b2ad5a; _ulta_ses.CM-Prod.ccc4=48b60bf2c73643cf; _ulta_id.ECM-Prod.ccc4=dd9bc9054a8d3fda; _ulta_ses.ECM-Prod.ccc4=1d800ea664a210a7; AlteonP10=CVNjFSw/F6x8+z82bPTAHg$$",
    "Host": "iftp.chinamoney.com.cn",
    "Origin": "https://iftp.chinamoney.com.cn",
    "Pragma": "no-cache",
    "Referer": "https://iftp.chinamoney.com.cn/english/bdInfo/",
    "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
for pp in range(1,6):
    print('当前爬取{}页'.format(pp))
    data = {
        "pageNo": pp,
        "pageSize": "15",
        "isin": "",
        "bondCode": "",
        "issueEnty": "",
        "bondType": "100001",
        "couponType": "",
        "issueYear": "2023",
        "rtngShrt": "",
        "bondSpclPrjctVrty": ""
    }
    resp = requests.post('https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN', data=data,
                         headers=he).json()
    print(resp["data"]["resultList"][0]["isin"])
    print(resp["data"]["resultList"][0]["bondCode"])
    print(resp["data"]["resultList"][0]["entyFullName"])
    print(resp["data"]["resultList"][0]["bondType"])
    print(resp["data"]["resultList"][0]["issueEndDate"])
    print(resp["data"]["resultList"][0]["debtRtng"])
    path_file_name = '../文件/中国交易中心2.csv'
    for kk in range(len(resp["data"]["resultList"])):
        if not os.path.exists(path_file_name):
            print('新建并且写入')
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    ['isin', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'])
                writer.writerow(
                    [resp["data"]["resultList"][kk]["isin"], resp["data"]["resultList"][kk]["bondCode"],
                     resp["data"]["resultList"][kk]["entyFullName"], resp["data"]["resultList"][kk]["bondType"],
                     resp["data"]["resultList"][kk]["issueEndDate"],
                     resp["data"]["resultList"][kk]["debtRtng"]])
        else:
            with open(path_file_name, "a+", encoding='utf_8_sig', newline='') as csvfile:
                print('新建完成后写入')
                writer = csv.writer(csvfile)
                writer.writerow(
                    [resp["data"]["resultList"][kk]["isin"], resp["data"]["resultList"][kk]["bondCode"],
                     resp["data"]["resultList"][kk]["entyFullName"], resp["data"]["resultList"][kk]["bondType"],
                     resp["data"]["resultList"][kk]["issueEndDate"],
                     resp["data"]["resultList"][kk]["debtRtng"]])