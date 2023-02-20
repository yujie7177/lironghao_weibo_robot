import requests
import json
import time
import datetime
from subprocess import call


def main():
    old_wb_list = get_wb_list()
    printlist(old_wb_list)
    while True:
        new_wb_list = get_wb_list()
        if new_wb_list != old_wb_list:
            print("有新微博！！")
            print(new_wb_list[0])
            cmd = "display notification \" 有新微博！！ \" with title \"lironghao_weibo_robot\""
            call(["osascript", "-e", cmd])
            old_wb_list = new_wb_list
        else:
            now_time = datetime.datetime.now()
            time1_str = datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
            print("无更新" + time1_str)
        time.sleep(60)


def get_wb_list():
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'
    cookie = 'WBPSESS=a_YZA6I5qCR3U8i3RfvlpsrpGwQHeNUc2eArqQgOpt-Rl1_D3N9nydGSiiwo9VHKJAwL1pbtCO2MJXMX198e8AI7GPbNk6lxdt3o5fTonNeSh5mq67Rvc-xsPe5qZt3BrKd8Ete_q0KWPX6WRGqe3Ky7MATldHjAfar3OUwG7FY=; Apache=6525185814266.414.1676858016781; ULV=1676858016785:3:3:1:6525185814266.414.1676858016781:1676526011689; UOR=,,login.sina.com.cn; _s_tentry=passport.weibo.com; wb_view_log=1440*9002; cross_origin_proto=SSL; login_sid_t=cbaaa0b5cb613d9098346596dd3e6234; SUB=_2AkMUrl2uf8NxqwJRmP0RzWrnZYxzyQvEieKi8qx1JRMxHRl-yT9vqmsrtRB6Py5zQUGGpFaHqWGjIQqCGV_yZuAV5O7v; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWTKkl.S7SQlnOX0RMY44J8; XSRF-TOKEN=f0Kv3lQb3TAjNl1B8TYEAVWq; ALF=1679117967; SCF=AjbmsrhkFRatWd4_l5eg6-PkCRe9GWSGMLvh9rHiDA1eKTsugb0yyMxsfnbnVIBub60Q18D3dTMoBi70GLTtSI0.; SINAGLOBAL=8570383411451.81.1676255207981'
    header = {'User-Agent': user_agent, 'Cookie': cookie}
    xhr_url = 'https://weibo.com/ajax/statuses/mymblog?uid=5662880560&page=1&feature=0'
    wb_list = []
    try:
        r = requests.get(xhr_url, headers=header)
        # r.encoding = 'utf-8'
        if r.status_code == 200:
            dict_r = json.loads(r.text)
            dict_r_list = dict_r['data']['list']
            for i in range(len(dict_r_list)):
                wb_list.append(
                    dict_r_list[i]['text_raw'] + '     ' + dict_r_list[i]['created_at'])
    except Exception as ex:
        print(ex)
    return wb_list


def printlist(list):
    for i in list:
        print(i)
        print('#######################################################')


if __name__ == "__main__":
    main()
