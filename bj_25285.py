def bmi_calc(w,h):
    return w / (h^2)

def rank(h,bmi):
    if h < 140.1:
        return 6
    elif h < 146:
        return 5
    elif h < 159:
        return 4
    elif h < 161:
        if bmi<35.0 & bmi>16.0:
            return 3
        else :
            return 4
    elif h >= 161 & h < 204:
        if (bmi > 16.0 & bmi < 18.5) |(bmi >30.0 & bmi<35.0) :
            return 3
        elif (bmi >= 18.5 & bmi < 20.0) | (bmi >= 25.0 & bmi < 30.0):
            return 2
        elif bmi >= 20.0 & bmi < 25.0:
            return 1
        else :
            return 4
    else :
        return 4
    

n = int(input());
p_list=[]
bmi_list = []
result_list = []
for i in  range(n):
    a = int(input())
    b = int(input())
    p_list.append([a,b])
    bmi_list.append(bmi_calc(p_list[i][0],p_list[i][1]))
    result_list.append(rank(a, bmi_list[i]))

for h in range(n):
    print(result_list[i])
