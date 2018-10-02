import random


while True:
	inn = input('**********键入Enter开始， q结束：**************')
	if inn.lower() == 'q':
		break
	elif inn == '':
		print('点数：' + str(random.randint(1, 6)))
print('******** game over ***********')
