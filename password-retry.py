number = 3
number1 = 2

while number > 0:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功!')
		break

	elif password != 'a123456':
		
		if number1 > 0:
			print ('密碼錯誤! 還有', number1 ,'次機會(最多輸入3次密碼)')
			number = number - 1
			number1 = number1 -1
		elif number1 >= 0:
			print('密碼錯誤超過3次，已鎖定!')
			break