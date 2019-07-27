#密碼重式程式
#讓使用者重複輸入密碼
#最多輸入錯誤三次
#如果正確，印出登入成功
#如果不正確，印出密碼錯誤

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
		else:
			print('密碼錯誤超過3次，已鎖定!')
			break