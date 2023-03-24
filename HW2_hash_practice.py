#!/usr/bin/env python
# coding: utf-8

# In[7]:


def count_letters(file_path):
    # 定義一個空字典來保存每個字母的出現次數
    letter_count = {}
    
    # 定義一個變數來計算總共有多少個不重複的英文字
    unique_letters = 0
    
    # 讀取字串檔案，須先將檔案放在同個資料夾
    with open(file_path, 'r') as f:
        # 逐行讀取
        for line in f:
            # 移除行末的換行符號
            letter = line.strip()
            # 如果這個字母還沒出現過，就把它加入字典
            if letter not in letter_count:
                letter_count[letter] = 1
                unique_letters += 1
            # 如果這個字母已經出現過，就把它出現次數加一
            else:
                letter_count[letter] += 1
    # 回傳結果
    return unique_letters, letter_count

# 測試程式碼
file_path = 'hw2_data.txt' # 字串檔案名稱為 hw2_data.txt
unique_letters, letter_count = count_letters(file_path)
print('總共有', unique_letters, '個不重複的英文字')
print('每一個英文字出現次數為:')
for letter, count in letter_count.items():
    print(letter, ':', count)


# In[ ]:





# In[ ]:




