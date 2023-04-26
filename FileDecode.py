from PIL import Image, ImageFilter
import numpy as np
import base64
import math


# 输出十六进制类型数组
def print_hex(bytes):
    l = [hex(int(i)) for i in bytes]
    print(" ".join(l))

f_base = open("tmp.png","rb")
content = f_base.read()
f_base.close()

find_index = content.find(b'\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82')
print(find_index)

png_offset = find_index+12


b_len = (content[png_offset] << 8) + content[png_offset+1]
print("len ",b_len)
index = 0
new_p = []
while index<b_len:
	offset = png_offset+2+index*3
	value = content[offset] | content[offset+1] | content[offset+2]
	new_p.append(value)
	index+=1;

newbytes =  bytes(new_p)
# print_hex(newbytes)
base_secret_key = base64.b64decode(newbytes)
print("secret_key ", base_secret_key)
print("------")
print("b64 ", base64.b64encode(base_secret_key))
