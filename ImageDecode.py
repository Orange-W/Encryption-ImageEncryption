from PIL import Image, ImageFilter
import numpy as np
import base64
import math


# 输出十六进制类型数组
def print_hex(bytes):
    l = [hex(int(i)) for i in bytes]
    print(" ".join(l))


if __name__ == "__main__":
	# 解码 ----------------------
	im2 = Image.open(r"out.png")
	data = im2.getdata()

	new_p = []

	for point in data:
		r = point[0]
		g = point[1]
		b = point[2]
		value = r | g | b
		new_p.append(value)

	newbytes =  bytes(new_p)
	# print_hex(newbytes)
	base_secret_key = base64.b64decode(newbytes)
	print("secret_key ", base_secret_key)
	print("------")
	print("b64 ", base64.b64encode(base_secret_key))