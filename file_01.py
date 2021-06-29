# list = [10, 20, 52, 12, 56, 78]
# search = 56

# def linear_search(list, search):
#     for i in range(len(list)):
#         result = list[i]
#         if result == search:
#             print("found in index:",i)
#         else:
#             print("Not found.")
# linear_search(list, search)


# print() # just use for new line print
# print()
# print()


# list2 = [10, 20, 52, 12, 56, 78]
# search2 = 52
# found = False

# def linear_search2(list2, search2):
#     for i in range(len(list2)):
#         result2 = list2[i]
#         if result2 == search2:
#             found = True
#             break
#     if found == True:
#         print("Found this number, in index:",i)
#     else:
#         print("Not found your number..")
# linear_search2(list2, search2)



# print() # just use for new line print
# print()
# print()


str = "Anwar Hossain"
search3 = "o"
x = False

def linear_search3(str, search3):
    for j in range(len(str)):
        result3 = str[j]
        if result3 == search3:
            global x
            x = True
            break
    if x == True:
        print("This is found,",j,"number index")
    else:
        print("Not found your input..")

linear_search3(str, search3)