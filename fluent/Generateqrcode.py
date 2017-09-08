#生成二维码
import qrcode
#img = qrcode.make('This is a quick response code!')

def generate(data):#貌似只能接受字符串，网址链接需要用双引号
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,#容错率
		box_size=10,
		border=4,
	)
	print(type(data))
	qr.add_data(data)
	qr.make(fit=True)
	img = qr.make_image(fill_color="white",back_color="black")
	img.save('qrcode.jpg','jpeg')
	img.show()

if __name__ == '__main__':
	import sys
	generate(*sys.argv[1:])
	