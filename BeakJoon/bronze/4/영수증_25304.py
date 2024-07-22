# https://www.acmicpc.net/problem/25304


def main():
    money = int(input())
    totalPrice = 0
    for _ in range(int(input())):
        totalPrice += eval(input().replace(" ", "*"))
    print("Yes" if money == totalPrice else "No")


if __name__ == "__main__":
    main()
