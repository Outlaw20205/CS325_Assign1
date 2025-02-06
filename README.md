# CS325_Assign1 - Ethan Lawrence - 2/5/25

## BattingAverage.py
```
 def findMedian(func):
    def wrapper(*args):
        median = args[0]
        median.sort()

        print("The median Batting Average is ", median[4])

        print("The average Batting Average is ", func(*args))

        return
    return wrapper


@findMedian
def findAvg(playerBA):
    avg = 0
    for x in playerBA:
        avg += x

    return avg / len(playerBA)

playersAvg = [.301, .273, .226, .260, .211, .273, .197, .248, .125]

findAvg(playersAvg) 
```

## TranslateNum.py
```
JPNum = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
count = 1

for x in JPNum:
    print(f"{count} is {x} in Japanese")
    count += 1
```

### ![This is Cooper](./Cooper.jpg)