from PIL import Image, ImageFilter
import numpy as np
import base64
import math


# 输出十六进制类型数组
def print_hex(bytes):
    l = [hex(int(i)) for i in bytes]
    print(" ".join(l))

if __name__ == "__main__":
	secret_key="MA=="

	# secret_key = "AAAAB3NzaC1yc2EAAAADAQABAAABgQDdimE+IjeM13ABZLc1hV01C38aSLXRpFLQQst5KUVTYsiMSxJsSsnltULAVP6oNeVikUSV5GE6WmqkHFVzdrGeTucvyE4yoApTjfuMqbIcdMfyIxbEyzyMX4g3gqAGaSbyXfHzoZc/CGkFttEJS4V+LfVouQFiEuGOg/O+5wFjynL/Cs9hFc412Jw8YfpR+tY300F3MMrwQhP8Y+Z64J9Xf5p7R/baB7xg/rvH0v+5V7QpwQu2VGRJgnKOED40/isK6SUknAzpH3rV0CnmGwjCvsaKlduOfscdPISK13h1QNWeGb5YMrSYjbezVa+r1HGY/FPeohRB2yO78CeickMDFvT77OskTLI8q6i5v+l88emcRrStomPNqKUiJOv+eMwdSyYmpNv8llynE2jBj49vrZCpFp+5Kcs/lp9MtJfqc6TjMuS0no2VAK0kksc7SYRB2pVXIrNTm3Isklf0RQSBKm8LIcDl+6pJxi7e/ePPPdgv3baceSValy9vbF3dxx0="
	# b64_bytes = base64.b64encode(secret_key.encode("utf-8"))
	decode_bytes = base64.b64decode(secret_key)
	

	b64_bytes = base64.b64encode(decode_bytes)

	bytes_len =len(b64_bytes)


	borderWidth = 1
	while(borderWidth*borderWidth < bytes_len):
		borderWidth += 1

	print("边长 ", borderWidth, "总长 ", bytes_len)
	print("------")
	print("b64 ", secret_key)
	print("------")
	print(decode_bytes)
	# print_hex(b64_bytes)

	img_save_bytes = []
	for point in b64_bytes:
		r = point & 0x42
		g = point & 0x24
		b = point & 0x19

		img_save_bytes.append((r,g,b))

	print("image_array ", (img_save_bytes))
	im = Image.new(mode="RGB", size=(borderWidth, borderWidth))
	im.putdata(img_save_bytes)
	im.save("out.png", quality=100)  # 将数组保存为图片
	
	print("\n\n-----------------------------------\n\n")