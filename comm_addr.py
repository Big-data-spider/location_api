'''

根据小区名查询经纬度坐标

'''
import requests
import re


def get_addr(com_name):
    key = '2AuUSWRQArFyXa4w0YlKE3mg4yGvPaHc'
    search_info = com_name.replace(' ', '')
    info_json = requests.get(
        'http://api.map.baidu.com/geocoder?address=%s&output=json&key=%s' % (search_info, key)).text

    pattern_lng = re.compile(r'"lng":(\d+.\d+),')
    pattern_lat = re.compile(r'"lat":(\d+.\d+)')
    try:
        res_lng = re.findall(pattern_lng, info_json)
        res_lat = re.findall(pattern_lat, info_json)

        output = [float(res_lng[0]), float(res_lat[0])]
        print(output)
    except:
        output = None
        print(output)

    return output

# get_addr('重庆南岸区海棠晓月')
