import math

def solution(fees, records):
    answer = []
    arr = []
    parking = {}
    total = {}

    for i in range(len(records)):
        arr.append(records[i].split())

    for i in range(len(records)):
        time = arr[i][0]
        car = arr[i][1]
        in_out = arr[i][2]

        hour, minute = map(int, time.split(":"))
        time = hour * 60 + minute

        if in_out == "IN":
            parking[car] = time

        else:
            parking_time = time - parking[car]

            if car not in total:
                total[car] = parking_time
            else:
                total[car] += parking_time

            del parking[car]

    end_time = 23 * 60 + 59

    for car in parking:
        parking_time = end_time - parking[car]

        if car not in total:
            total[car] = parking_time
        else:
            total[car] += parking_time

    cars = sorted(total.keys())

    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    for car in cars:
        time = total[car]

        if time <= basic_time:
            answer.append(basic_fee)

        else:
            fee = basic_fee + math.ceil(
                (time - basic_time) / unit_time
            ) * unit_fee

            answer.append(fee)

    return answer