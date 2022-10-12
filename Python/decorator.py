"""
decorator.md를 기반으로 정리한 내용이 실제로 어떤식으로 쓰이는지 정리

비밀번호 감지하고 동일하면 리스트를 돌며 평균값을 산출
비밀번호가 다를경우 다르다는 메세지만 리턴
"""

score = [(100, 100), (95, 80), (50, 78), (52, 98), (60, 61)]

def need_password(func):
    def wrapper(*args, **kwargs):
        password = "1234"
        input_pw = input("비밀번호를 입력하세요 : ")
        if password == input_pw:
            result = func(*args, **kwargs)
        else:
            result = "잘못된 비밀번호입니다"
        return result
    return wrapper

@need_password
def get_avg(num):
    for index, point in enumerate(num):
        print(f"{index+1}번, 평균 : {sum(point)/len(point)}")

get_avg(score)

"""
결과
비밀번호를 입력하세요 : 1234
1번, 평균 : 100.0
2번, 평균 : 87.5
3번, 평균 : 64.0
4번, 평균 : 75.0
5번, 평균 : 60.5
"""