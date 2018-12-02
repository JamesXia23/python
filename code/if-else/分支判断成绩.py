score = int(input("请输入一个成绩："))

if score > 100 or score < 0:
    print("成绩错误")
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >=70:
    print("一般")
elif score >= 60:
    print("及格")
else:
    print("不及格")
