data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
#		count += 1
#		if count % 1000 == 0:
#			print(len(data))

#print('檔案讀取完了, 總共有', len(data), '筆資料')

# sum_len = 0
# for d in data:
# 	sum_len += len(d)
# 	print(sum_len)

# print(sum_len / len(data)) 

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)

# print('一共有', len(new), '筆資料小於100')
# print(new[0])

# 文字計數
wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		if word not in wc:
			wc[word] = 1	
# print(wc)

# 計算每個字出現的次數
# Nested for loop for 裡面有 for loop


# 列印比較漂亮，單行列印
for word in wc:
	if wc[word] > 100:
		print(word, wc[word])


while True: 
	word = input('請問你想要查甚麼字: ')
	
	if word == 'q':
		print('感謝使用本查詢功能')
		break
	if word in wc:
		print(word, '出現次數為: ', wc[word])
	else: 
		print('這個字沒有出現過')
		

# print(new[1])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')

# good = [d for d in data if 'good' in d]
# bad = ['bad' in d for d in data]
# print(bad)