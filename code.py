#密碼重試試驗
#先在城市中設定好密碼password ='a123456'
#請使用者重複輸入密碼
#最多輸入三次
#如果正確就印出登入成功
#如果不正確,就印出“密碼錯誤!還有＿次機會！

password  = 'a123456'
i = 3#剩餘機會
while i > 0:
	code = input('請輸入密碼:')
	if code == password:
		print('登入成功！')
		break
	else:
		i = i - 1
		print('密碼錯誤！還有',i,'次機會')
		

