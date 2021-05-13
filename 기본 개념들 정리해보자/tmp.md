# 예외처리

## 개념

- 코드를 실행중에 발생하는 에러를 처리하기 위한 처리입니다.

## 예외처리 하기

`특정 코드에 대한 예외처리`

```{.python}
try:
    코드
except 예외명:
    코드
```

- 위와 같이 특정 에러에만 특별한 처리를 하고 싶으면 except 를 이용하면 된다.
  - except는 여러개를 작성해도 된다.
- try문에서 에러가 발생하면, 그 코드줄(발생위치)실행하지 않는다.

  - 에러에 맞는 except로 이동하여 처리한다.

`간단 예시`

```{.python}
try:
    num = 2 /0
    print(num)
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
```

- 위와 같이 작성한다면 try문의 print(num)은 출력하지 않고, except에 <font color = red> '0으로 나눌 수 없습니다.' </font>가 출력된다.

`에러 메시지 받아오기`

```{.python}
try :
    코드
except 예외 as 변수:
    코드
```

- 위외 같이 작성한다면 에외에 관한 메시지들을 받아올 수 있다.

```{.python}
try:
    num = 2 /0
    print(num)
except ZeroDivisionError as e :
    print('0으로 나눌 수 없습니다.',e)
```

- 위와 같이 작성한다면 try문의 print(num)은 출력하지 않고, except에 <font color = red> '0으로 나눌 수 없습니다. <u>division by zero'</u></font>가 출력된다.

`위와같이 사용 할 수 있지만, 모든 에러를 볼 수 있는 <font color = red > Exeception</font>을 많이 사용한다.`

```{.python}
except Execption as e :
    print("Error 발생",e)
```

` 위와같이 사용한다면 모든 에러 메시지를 받아올 수 있다.

## else 및 finally

- else는 예이가 발생하지 않았을 때 실행할 코드이다.
  - except: 가 실행했다면, 실행되는 코드블록이다.
- finally는 예외 발생 여부와 상관없이 실행하는 코드이다.
  - except: 의 실행여부에 상관없이 무조껀 실행되는 코드블록이다.

```{.pyhthon}
try:
    실행할 코드
except:
    예외 발생시 실행할 코드
else:
    예외 발생하지 않는다면 실행할 코드
finally:
    예외 발생여부 상관없이 실행할 코드
```

`간단한 예시`

```{.pyhthon}
try:
    num = 2 /2
    print(num)
except:
    print("Error 발생",e)
else:
    print("Error 발생 안했어요")
finally:
    print("코드 끝났어요")
```

` 위와같은 코드를 실행하면 '1'을 출력하고 else문과 finally문을 실행하게된다.`

## 예외 발생시키기

- 위와 같은 방법으로는 파이썬에서 지정한 예외에 대한 처리만 할 수 있습니다.
- 개발자가 생각하는 상황을 예외처리를 하여 발생시키는 방법입니다.

### 방법

```{.python}
raise 예외('에러 메시지')
```

### 예시

```{.python}
try:
    x = int(input('2의 배수를 입력하시오.'))
    if x %2 ==1:
        raise Exception('2의 배수가 아니에요')
    print(x)
except Exception as e:
    print('예외가 발생!!',e)
```

`위와 같이 개발자가 예외 상황을 만들 수 있습니다.`

### 다시 except에서 실행 후 try문으로 돌아가기.

`"raise 예외('에러메시지')" 넣기!`

```{.python}
try:
    x = int(input('2의 배수를 입력하시오.'))
    if x %2 ==1:
        raise Exception('2의 배수가 아니에요')
    print(x)
except Exception as e:
    print('예외가 발생!!',e)
    raise RuntimeError('예외가 발생했어요!!')
```

- 코드 실행중 raise를 만나면 실행줄이 try로 돌아간다.

- `"assert 조건식, 에러메시지 " 를 이용하여 발생시킬 수 있다.`
