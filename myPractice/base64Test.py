# -*- coding: utf-8 -*-
import base64
def safe_base64_decode(s):
    while len(s) % 4 != 0:
        s=s+b'='
    return base64.b64decode(s)
    
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')