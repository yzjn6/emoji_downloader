import os

import requests
from bs4 import BeautifulSoup

# 网页URL
domain = "https://www.emojiall.com/zh-hans/emoji"

# 发送HTTP GET请求获取网页内容

emojis = ["✉️🍅🥚🥚",
          "⚖️🤍👉1️⃣",
          "⚪🦳👞🧓🏻",
          "1️⃣🧹2️⃣🈳",
          "3️⃣🔀9️⃣🤤",
          "7️⃣4️⃣🔙🥜",
          "🈚🐔🉑🙏🏻",
          "🈚👨❓🐳",
          "🈚🔒🍅🍅",
          "🈚😘🈚🦴",
          "🈯Ⓜ️🙅🏻‍♀️5️⃣",
          "🈯🖐🏻🉑🥵",
          "🈳🦱🍹🎫",
          "🈵🔫🥵🍊",
          "🈵🚪✍🏻斩",
          "🈶🍅🈚🦖",
          "🈶👀🏹🦠",
          "🈹🈹🙅🏻‍♀️🦌",
          "🉐🙅🏻‍♀️👅🦁",
          "🌁👆🏻👨➖",
          "🌩️💪🌪️🚶‍♂️",
          "🍋4️⃣🙅🏻‍♀️🍪",
          "🍜🍜🙋🏻‍♂️🌾",
          "🎁👆🏻🕸️🚶‍♀️",
          "🏹🏹👓👓",
          "🐌🦶🏻🤫🔆",
          "🐍🥜🍪1️⃣",
          "🐏🐏🚿🚿",
          "🐔🐠🙏🏻🍊",
          "🐠🐲👻🤹🏻",
          "🐠🥩💯✉️",
          "🐳9️⃣🙅🏻‍♀️🍉",
          "🐹⬜🈚💪",
          "👶🏻🐳🍅🦴",
          "💪👓🐹🤕",
          "💯🏠💉🔆",
          "💰🚗🍹⚔️",
          "📿🔗🦎🈴",
          "🔃🍐🍊🐙",
          "🔃💧⏏️🛶",
          "🔄🔃🐔🍅",
          "🔥🀄🤏🏻🌰",
          "🕰️🔒🥣🕷️",
          "🖐🏻📋♟️🏄🏻",
          "🖐🏻🦶🏻🈚❌",
          "🗳️🐭🐔💨",
          "🙅🏻‍♀️⚪1️⃣0️⃣0️⃣0️⃣0️⃣🍐",
          "🙅🏻‍♀️1️⃣2️⃣🛫",
          "🙅🏻‍♀️1️⃣🐠💪",
          "🙅🏻‍♀️🉑🥁📐",
          "🙅🏻‍♀️🐔🍹🌈",
          "🙅🏻‍♀️🐔🙅🏻‍♀️🍐",
          "🙅🏻‍♀️🔆1️⃣💰",
          "🙅🏻‍♀️🥶2️⃣🌰",
          "🥇🌪️🌽🦌",
          "🥜0️⃣♟️👓",
          "🥜🤰🏼6️⃣🐞",
          "🥝🌁大🥴",
          "🦈1️⃣#️⃣💯",
          "🦟🏘️4️⃣👶🏻",
          "🦠1️⃣🈚2️⃣",
          "🧓🏻☀️🐲🕰️",
          "🧠🤭🍊😡",
          "🪑🧓🏻🎙️🧓🏻"]
# emojis = ["✉️🍅🥚🥚"]


def download(i,url):
    response = requests.get(url)
    print(url)
    # 检查请求状态码，200表示请求成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML文档
        soup = BeautifulSoup(response.content, 'html.parser')

        # 找到目标图片的节点
        img_node = soup.select_one(
            'body > div.body_warp.row.no-gutters > section > div > div > div > div > div:nth-child(1) > div > div > div > div > div > div:nth-child(1) > div:nth-child(15) > div > ul > li:nth-child(2) > figure > img')
        print("img_node",img_node)
        # 获取图片的URL链接
        image_url = "https://www.emojiall.com"+img_node['data-src']
        print(image_url)
        # 发送HTTP GET请求获取图片内容
        image_response = requests.get(image_url)

        # 检查请求状态码，200表示请求成功
        if image_response.status_code == 200:
            # 将图片保存到本地
            with open("words/" + words+"/"+i+".png", "wb") as file:
                file.write(image_response.content)
            print("图片下载成功！")
        else:
            print("图片下载失败！")
    else:
        print("网页请求失败！")


if __name__ == '__main__':

    for words in emojis:
        os.makedirs("words/" + words)
        for i in words:
            url_emoji = domain + "/"+i
            download(i,url_emoji)
