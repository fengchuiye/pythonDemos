#someone@gmail.com
#bill.gates@microsoft.com
# -*- coding: utf-8 -*-
import re
def is_valid_email(addr):
    if re.match(r'[\w|.]+@.*.com',addr):
        return True
    else:
        return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


#<Tom Paris> tom@voyager.org => Tom Paris
#bob@example.com => bob
# -*- coding: utf-8 -*-
import re
def name_of_email(addr):
    m=re.match(r'<*([\w|.|\s]*)>*([\w|.|\s])*@.*..*',addr)
    return m.group(1)
    
# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
