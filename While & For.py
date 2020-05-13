
def squared_numbers(start, stop):
    while start <= stop:
        print(start*start)
        start += 1

def is_greater(my_list, n):
    answer = []
    for num in my_list:
        if num > n:
            answer.append(num)

    return answer

# def numbers_letters_count(my_str):
#     results = [0, 0]
#     for char in my_str:
#         if char.isnumeric():
#             results[0] +=1
#         else:
#             results[1] +=1
#     return results

# def seven_boom(end_number):
#     results = []
#     for nums in range(end_number+1):
#         if nums %7 ==  0:
#         # if (x-7) % 10 == 0
#             results.append("BOOM")
#         elif "7" in str(nums):
#             results.append("BOOM")
#         else:
#             results.append(nums) 
#         # results + str(nums)
#     return results  

def sequence_del(my_str):
    clean_str = []
    for i in range(len(my_str)):
        if (len(clean_str) == 0):  
            clean_str.append(my_str[i])  
        else:
            Str = clean_str[-1]
            if (Str == my_str[i]):
                clean_str.pop()
            else:
                clean_str.append(my_str[i])
    return str(clean_str)



def main():
    # squared_numbers(-3, 3)
    # print("hello")
    # squared_numbers(4, 8)

    # result = is_greater([1, 30, 25, 60, 27, 28], 28)
    # print(result)

    # print(numbers_letters_count("Python 3.6.3"))

    # print(seven_boom(17))

    
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    # sequence_del("SSSSsssshhhh")
    # sequence_del("Heeyyy   yyouuuu!!!")

if __name__ == "__main__":
    main()
