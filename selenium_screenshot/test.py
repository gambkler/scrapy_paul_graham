import os
import json
import time
import math

from PIL import Image
# from selenium import webdriver

# geckodriver_path = os.path.join(os.path.abspath(os.curdir), 'geckodriver')
# options = webdriver.FirefoxOptions()
# options.headless = True
# geckodriver = webdriver.Firefox(executable_path=geckodriver_path, options=options)
# # 如果想要截长图，浏览器窗口大小会被拉伸到超过显示器分辨率，需要使用headless模式
# # geckodriver = webdriver.Firefox(executable_path=geckodriver_path)
# geckodriver.set_page_load_timeout(30)

# main_url = 'https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API'

# print('opening main_url, may take several minutes')
# geckodriver.get(main_url)
# print('opened main_url')
# links_xpath = '//div[@id="sidebar-quicklinks"]//a'
# link_elements = geckodriver.find_elements_by_xpath(links_xpath)

# links = []
# for i in link_elements:
#     links.append({
#         'href': i.get_attribute('href'),
#         'title': i.get_attribute('title'),
#         'text': i.text,
#     })

# def get_current_doc_size(geckodriver):
#     return (
#         geckodriver.execute_script('return document.body.scrollWidth'),
#         geckodriver.execute_script('return document.body.scrollHeight')
#     )

png_folder = os.path.join(os.path.abspath(os.curdir), 'png')
# if not os.path.exists(png_folder):
#     os.mkdir(png_folder)

# print('begin screenshot')
# for c, i in enumerate(links):
#     print(c, len(links), i['href'])
#     geckodriver.get(i['href'])
#     geckodriver.set_window_size(*get_current_doc_size(geckodriver))
#     i['img_path'] = os.path.join(png_folder, i['text']+'.png')
#     geckodriver.save_screenshot(i['img_path'])
#     time.sleep(3)

# geckodriver.close()

deatil_filename = os.path.join(png_folder,'detail.json')
# with open(deatil_filename, 'w+') as f:
#     json.dump(links, f, indent=4)

detail = None
with open(deatil_filename) as f:
    detail = json.load(f)

# A4 210mm*297mm  300ppi  2480*3508
# 1inch = 25.4mm  8.268*11.693inch
# 180ppi 1488*2105
page_width, page_height = 1488, 2105
split_height = 1905
def crop_pic(pic):
    width, height = pic.size
    cropped_pictures = []
    for i in range(math.ceil(height/split_height)):
        splitted = pic.crop((0, i*split_height, width, (i+1)*split_height if (i+1)*split_height<height else height))
        new_pic = Image.new(pic.mode, (page_width, page_height), color='white')
        new_pic.paste(splitted, ((page_width-width)//2, (page_height-split_height)//2))
        splitted.close()
        cropped_pictures.append(new_pic)
    return cropped_pictures

base_png = Image.new('RGB', (page_width, page_height), color='white')
pngs = []
catalogue = []
page_num = 1
for i in detail[1:]:
    pic = Image.open(i['img_path']).convert("RGB") # 去除A通道，A通道为透明度
    cropped = crop_pic(pic)
    pngs += cropped
    pic.close()
    catalogue.append((i['text'], page_num))
    page_num += len(cropped)
base_png.save('test.pdf', 'pdf', save_all=True, append_images=pngs)
base_png.close()
for png in pngs:
    png.close()

with open('test.txt', 'w+') as f:
    json.dump(catalogue, f, indent=4)
