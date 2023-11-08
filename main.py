def calculate_bmi(height, weight):
    # BMI 계산을 위한 식
    bmi = weight / ((height / 100) ** 2)
    return bmi

def bmi_category(bmi, gender):
    if gender == "남자":
        if bmi < 18.5:
            return "저체중"
        elif 18.5 <= bmi < 23:
            return "정상"
        elif 23 <= bmi < 25:
            return "과체중"
        elif 25 <= bmi < 30:
            return "경도 비만"
        else:
            return "고도 비만"
    elif gender == "여자":
        if bmi < 18.5:
            return "저체중"
        elif 18.5 <= bmi < 22:
            return "정상"
        elif 22 <= bmi < 25:
            return "과체중"
        elif 25 <= bmi < 30:
            return "경도 비만"
        else:
            return "고도 비만"
    else:
        return "성별 정보를 확인할 수 없습니다."

def health_recommendation(category):
    if category == "저체중":
        return (
            "체중을 증가시키기 위해 균형 잡힌 식단 섭취: 영양소가 풍부한 식사를 즐기고, 규칙적인 식사 시간을 유지하세요.탄수화물을 많이 섭취하는 것보다는 단백질 섭취를 늘리는 것을 추천드립니다.\n"
            "규칙적인 운동: 근력 운동과 유산소 운동을 조화롭게 실시하여 건강한 체중 증가를 도우세요."
        )
    elif category == "과체중":
        return (
            "식단 관리: 칼로리 섭취를 조절하고, 건강한 식단으로 전환하여 체중 감량을 도우세요.\n"
            "규칙적인 유산소 운동: 유산소 운동을 실시하여 체지방을 태우고, 대사량을 증가시켜 체중 감량을 도우세요."
        )
    elif category == "경도 비만":
        return (
            "식단 조절: 식사량을 줄이고, 고칼로리 음식을 피하여 체중 감량을 도우세요.\n"
            "유산소 운동과 근력 운동: 체중 감량을 돕는 유산소 운동과 근력을 강화시키는 운동을 조화롭게 실시하세요."
        )
    elif category == "고도 비만":
        return (
            "전문가와 상담: 건강 전문가와 상담하여 체중 감량을 위한 개인 맞춤형 계획을 수립하세요.\n"
            "규칙적인 운동 및 식단 관리: 전문가의 지도에 따라 규칙적인 운동과 식단 관리를 실시하여 체중을 감량하세요."
        )
    else:
        return (
            "건강한 식단과 규칙적인 운동 유지를 통해 현재 상태를 유지하세요."
        )

# 사용자로부터 성별, 키, 몸무게를 입력받는다.
gender = input("성별을 입력하세요 (남자/여자): ")
height = float(input("키(cm)를 입력하세요: "))
weight = float(input("몸무게(kg)를 입력하세요: "))

# BMI 계산
bmi = calculate_bmi(height, weight)

# BMI 범주 확인
category = bmi_category(bmi, gender)

# 건강 및 운동 권장사항
recommendation = health_recommendation(category)

# 결과 출력
print("BMI: {:.2f}".format(bmi))
print("비만 정도: {}".format(category))
print("건강 및 운동 권장사항: {}".format(recommendation))
