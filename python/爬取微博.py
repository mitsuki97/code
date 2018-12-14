# -*- coding:utf-8 -*-
import requests
from pymongo import MongoClient

ACCESS_TOKEN = '2.00mqO8xBiNZKcC0451645de9eLHRUE'
URL = 'https://api.weibo.com/2/statuses/public_timeline.json'


def run():
#授权

    while True:
        #调用statuses__public_timeline的api接口
        params = {
            'access_token': ACCESS_TOKEN
        }

        statuses = requests.get(url=URL, params=params).json()['statuses']
        length = len(statuses)
        #这是后来我为了查看获取微博条数设置的
        print ("length")
        #连接mongodb,不需要本地的额外配置
        Monclient = MongoClient('localhost', 27017)
        db = Monclient['Weibo']
        WeiboData = db['HadSelected']

        #获取的各个数据名应该可以清楚的看出来对应的是什么数据
        for i in range(0, length):
            created_at = statuses[i]['created_at']
            id = statuses[i]['user']['id']
            province = statuses[i]['user']['province']
            city = statuses[i]['user']['city']
            followers_count = statuses[i]['user']['followers_count']
            friends_count = statuses[i]['user']['friends_count']
            statuses_count = statuses[i]['user']['statuses_count']
            url = statuses[i]['user']['url']
            geo = statuses[i]['geo']
            comments_count = statuses[i]['comments_count']
            reposts_count = statuses[i]['reposts_count']
            nickname = statuses[i]['user']['screen_name']
            desc = statuses[i]['user']['description']
            location = statuses[i]['user']['location']
            text = statuses[i]['text']

            #插入mongodb
            WeiboData.insert_one({
                'created_at': created_at,
                'id': id,
                'nickname': nickname,
                'text': text,
                'province': province,
                'location': location,
                'description': desc,
                'city': city,
                'followers_count': followers_count,
                'friends_count': friends_count,
                'statuses_count': statuses_count,
                'url': url,
                'geo': geo,
                'comments_count': comments_count,
                'reposts_count': reposts_count
                })
if __name__ == "__main__":
    run()