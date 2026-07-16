import csv
import json

clean_student = [] #유효한 학생 데이터 저장용 리스트

try : #오류나면 처리 가능
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file) #파일을 한 줄씩 읽어오기 위한 reader 객체 생성
        next(reader) #첫 번째 줄을 한 번 읽고 버림(헤더 건너뛰기)

        for row in reader: #reader 안에 있는 한 줄씩 꺼내서 row에 저장
            name = row[0]
            score_text = row[1]

            try:
                score = int(score_text) #점수를 정수로 변환

            except ValueError: #오류 발생시 사용
                print(name, "-> 숫자 변환 실패")
                continue

            if score < 0 or score > 100: #점수가 0~100 범위에 있는지 확인
                print(name, "-> 허용 범위 초과")
                continue

            clean_student.append([name, score]) #유효한 학생 데이터만 저장
                

except FileNotFoundError: #오류 발생시 사용
    print("students.csv 파일을 찾을 수 없습니다.")
    exit() #프로그램 종료

with open("clean_student.csv", "w", encoding="utf-8") as file: #w:새로운 파일 생성 가능, try생략가능
       writer = csv.writer(file) #파일에 데이터를 쓰기 위한 writer 객체 생성
       writer.writerow(["name", "score"]) #헤더 작성
       writer.writerows(clean_student) #유효한 학생 데이터를  저장
    
scores = [] #점수 테이터 저장용 리스트

for student in clean_student:
        scores.append(student[1]) #점수만 추출하여 scores 리스트에 저장

count = len(scores) #점수 개수
if count > 0:
        average = sum(scores) / count #평균 계산
        highest = max(scores) #최고 점수 계산
else: #정상 학생이 없을 경우
    average = 0
    highest = 0

summary = { #json으로 저장할 데이터 만들기     
    "count":count,
    "average": average,
    "highest": highest #통계정보 딕셔너리에 저장
}

with open("summary.json", "w", encoding="utf-8") as file:

    json.dump( summary, file, ensure_ascii=False )
        #파일에 저장하는 함수

 
