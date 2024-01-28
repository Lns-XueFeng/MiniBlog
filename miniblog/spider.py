# 实现网站与公众号文章同步功能
import re
import requests

PASSAGE_PYSHARE_URL = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg5ODYxMTg0NA==&action=getalbum&" \
                      "album_id=2457108742094864388&scene=173&from_msgid=2247483958&" \
                      "from_itemidx=1&count=3&nolastread=1#wechat_redirect"
PASSAGE_WEBDEV_URL = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg5ODYxMTg0NA==&action=getalbum&" \
                     "album_id=2886040672825442312&scene=173&from_msgid=2247484199&" \
                     "from_itemidx=1&count=3&nolastread=1#wechat_redirect"
PASSAGE_SPIDER_URL = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg5ODYxMTg0NA==&action=getalbum&" \
                     "album_id=2061865102428995584&subscene=159&subscene=19&scenenote=https%3A%2F%2Fmp.weixin.qq.com" \
                     "%2Fs%3F__biz%3DMzg5ODYxMTg0NA%3D%3D%26mid%3D2247484026%26idx%3D1%26sn" \
                     "%3Df1bbdd40af6ff2eb6a1d8fe7833250b7%26scene%3D19%23wechat_redirect&nolastread=1#wechat_redirect"
PASSAGE_DISCUSS_URL = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg5ODYxMTg0NA==&" \
                      "action=getalbum&album_id=2173572752933257219#wechat_redirect"


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
}


def __download_sourcecode():
    PYSHARE_CODE = requests.get(PASSAGE_PYSHARE_URL, headers=headers).text
    WEBDEV_CODE = requests.get(PASSAGE_WEBDEV_URL, headers=headers).text
    SPIDER_CODE = requests.get(PASSAGE_SPIDER_URL, headers=headers).text
    DISCUSS_CODE = requests.get(PASSAGE_DISCUSS_URL, headers=headers).text
    return PYSHARE_CODE, WEBDEV_CODE, SPIDER_CODE, DISCUSS_CODE


def __match_need_data(string):
    title = re.findall("title: '(.*?)'", string)[2:]
    psg_url = re.findall("url: '(.*?)'", string)[:-1]
    return title, psg_url


def __get_finally_data(li_1, li_2):
    assert len(li_1) == len(li_2)
    need_dict = {li_1[c]: li_2[c] for c in range(len(li_1))}
    return need_dict


def offer_finally_data():
    # 得到四个页面的源代码
    PY_CODE, WEB_CODE, SPI_CODE, DIS_CODE = __download_sourcecode()
    # 匹配到四个页面相应的数据
    PY_TITLE_LI, PY_PSG_URL_LI = __match_need_data(PY_CODE)
    WEB_TITLE_LI, WEB_PSG_URL_LI = __match_need_data(WEB_CODE)
    SPI_TITLE_LI, SPI_PSG_URL_LI = __match_need_data(SPI_CODE)
    DIS_TITLE_LI, DIS_PSG_URL_LI = __match_need_data(DIS_CODE)
    # 得到最终要使用的数据结构
    PASSAGE_PY = __get_finally_data(PY_TITLE_LI, PY_PSG_URL_LI)
    PASSAGE_WEB = __get_finally_data(WEB_TITLE_LI, WEB_PSG_URL_LI)
    PASSAGE_SPIDER = __get_finally_data(SPI_TITLE_LI, SPI_PSG_URL_LI)
    PASSAGE_DISCUSS = __get_finally_data(DIS_TITLE_LI, DIS_PSG_URL_LI)
    return PASSAGE_PY, PASSAGE_WEB, PASSAGE_SPIDER, PASSAGE_DISCUSS
