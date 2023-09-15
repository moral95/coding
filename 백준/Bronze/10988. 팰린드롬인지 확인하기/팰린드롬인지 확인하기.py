# 10988 번
inputs = input()
inputs
# if len(inputs)>0 and len(inputs)<=100 :

k =0
for i in range(len(inputs)):
    if inputs[1*i] == inputs[-1*(i+1)]:
        k += 1
if k / len(inputs) == 1:
    print(1)
else :
    print(0)