import re
import json


def get_addr_cq():
    f = open('sub.json', 'r', encoding='utf-8')
    info_json = json.load(f)
    f.close()
    # print(type(info_json))
    res = []
    res1 = []
    for i in info_json:
        # for line_nub,value in i.items():
        station_list = i.get('stations')
        for l in station_list:
            print(l)
            # output = {res_name: [float(res_lng[0]), float(res_lat[0])]}
            # print(output)
            # res1.append(output)
            name = l.get('name')
            p = l.get('location')
            lng = p.get('lng')
            lat = p.get('lat')
            output = {name: [lng, lat]}
            res1.append(output)
        out1 = {i.get('line'): res1}
        res.append(out1)

    print(res)

    f = open('res.json', 'w', encoding='utf-8')
    f.write(json.dumps(res, ensure_ascii=False, indent=4))
    f.close()


get_addr_cq()
