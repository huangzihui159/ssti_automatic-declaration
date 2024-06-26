import requests
import time

now_time = time.strftime('%Y-%m-%d %H:%M:%S')

date = time.strftime('%Y-%m-%d')

url='https://ty.ssti.net.cn/Declare/Api/MedicalObHandle.ashx?action=add'

Cookie='ltToken=xxxx' #使用Fiddler抓取的参数


header={
        'Cookie':Cookie,
        'User-Agent':'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1',
        'content-type':'application/x-www-form-urlencoded',
        "Referer":"https://ty.ssti.net.cn/Declare/Pages/Stu/EpidemicApply.aspx"
    }

data={
        "Address":"广东省深圳市深圳技师学院", #定位的位置
        "CurrentEnUserCode":"xxxxxxxxxxxxxxxx", #使用Fiddler抓取的参数
        'CurrentUserCode':"2019xxxxx",    #学号
        "CurrentUserName":"xxx",        #姓名
        "ispicker":1,
        "latitude":22.7475,    #纬度 目前是学校的纬度
        "longitude":114.2343, #经度  目前是学校的经度
        "Mobile":'xxxxxxxxxxx',   #手机号码
        "opentime":now_time,
        "source":"xswx",
        "Temp1":1,
        "Temp10":'',
        "Temp10_Begin":"",
        "Temp10_End":"",
        "Temp11":-1,
        "Temp12":-1,
        "Temp13":1,
        "Temp14":-1,
        "Temp15":-1,
        "Temp16":"xxxxxxxxxxxxxxxxxxxxx", #家庭住址
        "Temp17":"",
        "Temp18":-1,
        "Temp19":"",
        "Temp2":"",
        "Temp20":19,
        "Temp22":7,
        "Temp24":3,
        "Temp25":date,
        "Temp26":1,
        "Temp29":-1,
        "Temp3":'',
        "Temp31":-1,
        "Temp32":-1,
        "Temp33":-1,
        "Temp34":-1,
        "Temp35":-1,
        "Temp36":-1,
        "Temp4":'',
        "Temp41":1,
        "Temp42":36.5,
        "Temp44":36.5,
        "Temp46":36.5,
        "Temp5":1,
        "Temp6":'',
        "Temp7":1,
        "Temp8":-1,
        "Temp9":""
    }


response=requests.post(url=url,data=data,headers=header)
print(response.text)
with open('./test.log','a',encoding='utf-8') as f:
    f.write(now_time+" "+response.text]+'\n')
    f.close()