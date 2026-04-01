# -*- coding: utf-8 -*-
"""
智能地址识别系统
学号：2024001001  姓名：张三
"""

from aip import AipNlp

# 百度AI配置（请替换为你的真实信息）


# 创建客户端
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

print("=" * 50)
print("智能地址识别系统")
print(f"学号：2024001001  姓名：张三")
print("=" * 50)

# 测试地址列表
addresses = [
    "北京市海淀区上地十街10号百度大厦",
    "上海市浦东新区世纪大道100号环球金融中心",
    "广东省深圳市南山区科技园腾讯大厦",
    "浙江省杭州市西湖区学院路77号"
]

for i, text in enumerate(addresses, 1):
    print(f"\n【测试 {i}】")
    print(f"原文本：{text}")
    print("-" * 50)

    try:
        # 调用地址识别
        result = client.address(text)

        # 显示结果
        if 'error_code' in result:
            print(f"错误：{result['error_msg']}")
        else:
            print(f"省份：{result.get('province', '无')}")
            print(f"城市：{result.get('city', '无')}")
            print(f"区县：{result.get('district', '无')}")
            print(f"详细地址：{result.get('text', text)}")
            print(f"经度：{result.get('lng', '无')}")
            print(f"纬度：{result.get('lat', '无')}")

    except Exception as e:
        print(f"识别失败：{e}")

print("\n" + "=" * 50)
print("识别完成！")
