#숫자 분리
import re

string = input()
numbers = re.findall('\d', string)

#문자 분리
import re

string = input()
alphas = re.findall('[a-zA-Z]', string)