#第四章 文本和字节序列
s = 'café'
print(len(s))
b = s.encode('utf8')
print(b)
print(len(b))
print(b.decode('utf8'))

cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)# bytearray没有字面量句法
print(cafe_arr)
print(cafe_arr[-1:])