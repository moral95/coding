# 10807 번
inputs1 = input()
inputs2= input()
inputs3 = input()


# split_n = inputs.split('\n')
# print(split_n)

# split_2 = split[1].split('')
split_2 = inputs2.split(' ')
# print(split_2)

# split_2_list = list(split_2[1:-1])
# print(split_2_list)

predict_split_2 = split_2.count(inputs3)
print(predict_split_2)