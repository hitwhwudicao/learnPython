# q7_输入三个英语单词按字典序升序输出,字符串之间可以直接用;操作符进行比较
word_list = [ 'bow','apple','compatible']
# word_list = sorted(word_list)
# 这里使用一个简单的冒泡排序进行比较
for i in range(len(word_list)) :
    for j in range(i+1, len(word_list)):
        if word_list[i] >= word_list[j] :
            temp = word_list[i]
            word_list[i] = word_list[j]
            word_list[j] = temp

print(word_list)