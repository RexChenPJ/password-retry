number = 3 #剩餘機會
password = 'a123456'

while number > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break #逃出迴圈

	elif pwd != password:
		
		if number > 1:
			number = number - 1
			print ('密碼錯誤! 還有', number ,'次機會(最多輸入3次密碼)')
		elif number == 1:
			print('密碼錯誤超過3次，已鎖定!')
			break