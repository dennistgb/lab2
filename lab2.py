print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list=get_user_input()
    print(num_list)
    calc_average_temperature(num_list)
    print(calc_min_max_temperature(num_list))
    


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    numbers = input().split(",")
    print(numbers)
    return numbers

def calc_average_temperature(num_list):
    sum = 0.0
    print(len(num_list))
    for i in num_list:
        sum += float(i)
    print("sum = " + str(sum))
    avg_temp = sum/(len(num_list))
    print(avg_temp)
    return avg_temp

def calc_min_max_temperature(num_list):
    min_max = ["max = " + str(max(num_list)), "min = " + str(min(num_list))]
    return min_max

main()