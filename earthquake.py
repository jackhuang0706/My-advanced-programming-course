def earth_quake():
    result = []
    code = 'CWA-66C0912B-B99B-436E-B63B-8005F28532C8' #爬蟲金鑰
    try:
        # 小區域地震資料
        url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={code}'
        req1 = requests.get(url) #抓取資料
        data1 = req1.json() #解析資料
        eq1 = data1['records']['Earthquake'][0] #取得最新地震資訊
        t1 = eq1['EarthquakeInfo']['OriginTime'] #紀錄發生時間

        # 有感地震
        url2 = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization={code}'
        req2 = requests.get(url2)
        data2 = req2.json()
        eq2 = data2['records']['Earthquake'][0]
        t2 = eq2['EarthquakeInfo']['OriginTime']

        result = [eq1['ReportContent'], eq1['ReportImageURI']] #顯示小地震資料
        if t2 > t1: #有感地震較晚發生
            result = [eq2['ReportContent'], eq2['ReportImageURI']] #更新為有感地震資料
    except Exception as e: #抓取失敗
        print(e)
        result = ['抓取失敗...', '']
    return result
