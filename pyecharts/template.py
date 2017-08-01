#!/usr/bin/env python
#coding=utf-8
import os

_mapindex = {
    "安徽": "anhui: '//oog4yfyu0.bkt.clouddn.com/anhui'",
    "澳门": "aomen: '//oog4yfyu0.bkt.clouddn.com/aomen'",
    "北京": "beijing: '//oog4yfyu0.bkt.clouddn.com/beijing'",
    "重庆": "chongqing: '//oog4yfyu0.bkt.clouddn.com/chongqing'",
    "福建": "fujian: '//oog4yfyu0.bkt.clouddn.com/fujian'",
    "甘肃": "gansu: '//oog4yfyu0.bkt.clouddn.com/gansu'",
    "广东": "guangdong: '//oog4yfyu0.bkt.clouddn.com/guangdong'",
    "广西": "guangxi: '//oog4yfyu0.bkt.clouddn.com/guangxi'",
    "贵州": "guizhou: '//oog4yfyu0.bkt.clouddn.com/guizhou'",
    "海南": "hainan: '//oog4yfyu0.bkt.clouddn.com/hainan'",
    "河北": "hebei: '//oog4yfyu0.bkt.clouddn.com/hebei'",
    "黑龙江": "heilongjiang: '//oog4yfyu0.bkt.clouddn.com/heilongjiang'",
    "河南": "henan: '//oog4yfyu0.bkt.clouddn.com/henan'",
    "湖北": "hubei: '//oog4yfyu0.bkt.clouddn.com/hubei'",
    "湖南": "hunan: '//oog4yfyu0.bkt.clouddn.com/hunan'",
    "江苏": "jiangsu: '//oog4yfyu0.bkt.clouddn.com/jiangsu'",
    "江西": "jiangxi: '//oog4yfyu0.bkt.clouddn.com/jiangxi'",
    "吉林": "jilin: '//oog4yfyu0.bkt.clouddn.com/jilin'",
    "辽宁": "liaoning: '//oog4yfyu0.bkt.clouddn.com/liaoning'",
    "内蒙古": "neimenggu: '//oog4yfyu0.bkt.clouddn.com/neimenggu'",
    "宁夏": "ningxia: '//oog4yfyu0.bkt.clouddn.com/ningxia'",
    "青海": "qinghai: '//oog4yfyu0.bkt.clouddn.com/qinghai'",
    "山东": "shandong: '//oog4yfyu0.bkt.clouddn.com/shandong'",
    "上海": "shanghai: '//oog4yfyu0.bkt.clouddn.com/shanghai'",
    "山西": "shanxi: '//oog4yfyu0.bkt.clouddn.com/shanxi'",
    "四川": "sichuan: '//oog4yfyu0.bkt.clouddn.com/sichuan'",
    "台湾": "taiwan: '//oog4yfyu0.bkt.clouddn.com/taiwan'",
    "天津": "tianjin: '//oog4yfyu0.bkt.clouddn.com/tianjin'",
    "香港": "xianggang: '//oog4yfyu0.bkt.clouddn.com/xianggang'",
    "新疆": "xinjiang: '//oog4yfyu0.bkt.clouddn.com/xinjiang'",
    "西藏": "xizang: '//oog4yfyu0.bkt.clouddn.com/xizang'",
    "云南": "yunnan: '//oog4yfyu0.bkt.clouddn.com/yunnan'",
    "浙江": "zhejiang: '//oog4yfyu0.bkt.clouddn.com/zhejiang'"
}


def get_map(map_name):
    """

    :param map_name:
    :return:
    """
    _location_js = _mapindex.get(map_name, "")
    _location = ""
    try:
        _location = _location_js.split(":")[0]
    except:
        pass
    return dict(
        location_js=_location_js,
        location=_location
        )


def get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path
