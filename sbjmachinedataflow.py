import json
import regex
a =b'k\x00\x00\x00{"fk_bin_data_lib":"FKDATAHS101","user_id":"7","verify_mode":"1","io_mode":"0","io_time":"20190902155752"}\x00'
print("Original Data:")
print("A")
print(type(a))
print(a)
print("----------------------------------------")
b = a.decode("ascii","ignore")
print("B")
print(type(b))
print("Decoded data:",b)
print("----------------------------------------")
pattern = "(\{(?:[^{}]|(?1))*\})"
rawBody = regex.findall(pattern, b)
print("C")
print(type(rawBody))
print(rawBody)
print("----------------------------------------")
d = json.loads(rawBody[0])
print("D")
print(type(d))
print(d)
print("user_id: ", d["user_id"])



