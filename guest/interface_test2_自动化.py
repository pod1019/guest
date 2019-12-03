import requests
import unittest
class GetEventListTest(unittest.TestCase):
    '''查询发布会接口测试'''
    def setUp(self):
        self.url = "http://127.0.0.1:8001/api/get_event_list/"

    def test_get_event_null(self):
        '''发布会id为空'''
        r = requests.get(self.url,params={'eid':''})
        result = r.json() # 转成字典，方便下面断线时候根据键，来取值
        print('发布会id为空：{0}'.format(result))
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],"parameter error参数错误")


    def test_get_event_success(self):
        '''发布会id为1，查询成功'''
        r = requests.get(self.url,params={'eid':'1'})
        result = r.json()
        print('22222',result,'ddddd')
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "success")
        self.assertEqual(result['data']['name'], "华为 P90 发布会")
        self.assertEqual(result['data']['address'], "国家体育馆")
        self.assertEqual(result['data']['start_time'], '2019-12-22T10:30:00')

if __name__ == '__main__':
    unittest.main()