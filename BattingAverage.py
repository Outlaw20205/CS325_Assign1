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