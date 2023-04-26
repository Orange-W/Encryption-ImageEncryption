from PIL import Image, ImageFilter
import numpy as np
import base64
import math

# 输出十六进制类型数组
def print_hex(bytes):
    l = [hex(int(i)) for i in bytes]
    print(" ".join(l))

if __name__ == "__main__":
	# secret_key="MA=="
	secret_key = "AAAAB3NzaC1yc2EAAAADAQABAAABgQDdimE+IjeM13ABZLc1hV01C38aSLXRpFLQQst5KUVTYsiMSxJsSsnltULAVP6oNeVikUSV5GE6WmqkHFVzdrGeTucvyE4yoApTjfuMqbIcdMfyIxbEyzyMX4g3gqAGaSbyXfHzoZc/CGkFttEJS4V+LfVouQFiEuGOg/O+5wFjynL/Cs9hFc412Jw8YfpR+tY300F3MMrwQhP8Y+Z64J9Xf5p7R/baB7xg/rvH0v+5V7QpwQu2VGRJgnKOED40/isK6SUknAzpH3rV0CnmGwjCvsaKlduOfscdPISK13h1QNWeGb5YMrSYjbezVa+r1HGY/FPeohRB2yO78CeickMDFvT77OskTLI8q6i5v+l88emcRrStomPNqKUiJOv+eMwdSyYmpNv8llynE2jBj49vrZCpFp+5Kcs/lp9MtJfqc6TjMuS0no2VAK0kksc7SYRB2pVXIrNTm3Isklf0RQSBKm8LIcDl+6pJxi7e/ePPPdgv3baceSValy9vbF3dxx0="
	# b64_bytes = base64.b64encode(secret_key.encode("utf-8"))
	decode_bytes = base64.b64decode(secret_key)

	b64_bytes = base64.b64encode(decode_bytes)

	bytes_len =len(b64_bytes)

	print("------ len", bytes_len)
	print("b64 ", secret_key)
	print("------")
	print(decode_bytes)
	# print_hex(b64_bytes)

	bToWrite = bytearray()
	len_h = (bytes_len&0xFF00) >> 8
	len_l = (bytes_len&0x00FF)
	bToWrite.append(len_h)
	bToWrite.append(len_l)
	
	print("head",len_h,len_l)
	
	for point in b64_bytes:
		r = point & 0x42
		g = point & 0x24
		b = point & 0x19
		bToWrite.append(r)
		bToWrite.append(g)
		bToWrite.append(b)

	print("bToWrite ",bToWrite)
	print_hex(bToWrite)


	f_base = open("out.png","rb")     
	content = f_base.read()
	f_base.close()
	
	# 加点杂质
	impurities_bytes = bytes(b'\xff\xff\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82')

	f_new = open("tmp.png","wb")
	newContent = content+bToWrite+impurities_bytes
	f_new.write(newContent)
	f_new.close()


	