#encoding:utf-8
import requests
import unittest
import json

class TestLoginYXT(unittest.TestCase):
    def setUp(self):
        self.host = "http://test-01.biostime.us"
        self.port = 80
        self.timeout = 1.0
    #登录营销通APP
    def test_01_login_YXT(self):
        headers = {"Content-Type":"application/json","AccessKeyId":"SVNodVZlQnpmdWFP","Signature":"94d24144b3e34c80fd579496a345e595cd919f49","Timestamp":"1569374123550"}
        datas = {"functionId":0,
                 "interceptParam":None,
                 "intervalTime":5000,
                 "needIntercept":False,
                 "request":{
                     "device":
                         {"appVer":141,"appVerName":"8.4.2.1","brand":"OnePlus","devToken":None,"deviceId":"869897031963639","dpi":None,"height":2074,"model":"ONEPLUS A6000","os":"android","osVer":"9","width":1080},
                        "isMixPassword":True,"operator":"13964293010","password":"6e0fc086c40cebeedf45c0dbc4c2a81d","passwordLength":6},
                     "seqNo":"1569374123541",
                     "sourceSystem":"MKT_ANDROID",
                     "url":"https://test-01.biostime.us/merchant-server/merchant/system/login/login",
                     "version":None
                 }
        d = json.dumps(datas,separators = (",",":"))
        print(d)

        self.url = self.host+"/merchant-server/merchant/system/login/login"
        response = requests.post(self.url,headers=headers,data = d,timeout=float(self.timeout))
        self.result = response.json()
        print(self.result)
        self.assertEqual(self.result['code'],100)
        self.assertEqual(self.result['desc'],'成功')
        return self.result['response']['token']

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()


