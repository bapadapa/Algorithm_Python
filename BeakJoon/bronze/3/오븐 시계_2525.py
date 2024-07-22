# 첫째 줄에는 현재 시각이 나온다.
# 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.


def main():
    time, min = map(int, input().split())
    cookingTime = int(input())

    duration = time * 60 + min + cookingTime
    print(duration // 60 % 24, duration % 60)


if __name__ == "__main__":
    main()
