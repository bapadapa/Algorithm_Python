# https://www.acmicpc.net/problem/25206

sumCredit = 0
sumScore = 0
credit = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
for _ in range(20):
    subject, score, grade = input().split()
    if grade == "P":
        continue
    sumCredit += float(score) * credit[grade]
    sumScore += float(score)

if sumScore == 0:
    print("0.000000")
else:
    print(sumCredit / sumScore)
