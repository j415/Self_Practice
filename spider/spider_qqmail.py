# author:aspiring


import requests

session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

post_url = "https://mail.qq.com/"
post_data = {"u": "1114130086", "p": "1439880614"}

session.post(post_url, data=post_data, headers=headers)

cookies = "pgv_pvi=5597574144; RK=w+itOZ2VOF; ptcz=6ae418815a400eba47bd900279f0115ef4db990f8b0ab9200f1f5f2d4447ec27; pgv_pvid=3892221568; eas_sid=i1P5j3S8v6I5T1I0N6o1x0u9a1; edition=mail.qq.com; webp=1; CCSHOW=000001; pgv_si=s6361389056; ptisp=cnc; ptui_loginuin=1114130086; pt2gguin=o1114130086; wimrefreshrun=0&; qm_flag=0; qqmail_alias=1114130086@qq.com; qm_domain=https://mail.qq.com; foxacc=1114130086&0; _qpsvr_localtk=0.06716124200292217; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; pgv_info=ssid=s1477113617; uin=o1114130086; skey=@MTSv7YGD5; p_uin=o1114130086; pt4_token=R0Ff-FwZkMCLbEOjk0GO4xQim0chNKXy6Uz5R9nlTec_; p_skey=3QPlq7N0IGdQgmK*5oxBza18e2Vjz7d1MQ08Jsaxaeo_; sid=1114130086&ee75786ac6f76bbf800c90d63d1f2d01,qM1FQbHE3TjBJR2RRZ21LKjVveEJ6YTE4ZTJWano3ZDFNUTA4SnNheGFlb18.; qm_username=1114130086; qm_ptsk=1114130086&@MTSv7YGD5; ssl_edition=sail.qq.com; qm_loginfrom=1114130086&wpt; username=1114130086&1114130086; new_mail_num=1114130086&27"

cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
print(cookies)

get_url = "https://mail.qq.com/cgi-bin/frame_html?sid=G70k1ZOYnPRMaCpx"
response = session.get(get_url, headers=headers)
print(response.status_code)

with open("files/qqmail.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode("gbk"))
