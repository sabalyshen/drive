# 這是依年齡看你可不可以開車的程式
drive = input('請問你開過車嗎?')
age = input('請問你的年齡? ')
age = int(age)
if drive == '有':
    if age >= 18:
        print('很好你通過囉')
    else:
    	print('未成年開車會被罰錢喔!!')
elif drive == '沒有':
    if age >= 18:
    	print('你可以考駕照囉!!')
    else:
    	print('未成年不要開車喔')
else:
	print('請輸入有或沒有')