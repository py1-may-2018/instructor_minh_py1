# Course Overview
# Why python:
#     easy to learn
#     forces you to have good syntax
#     good community


# basic python
#     variables - storage block
#         int, float, bool, str
#     list
#     dictionaries
#     forloops
#     functions



raymond = {
    "first_name":"Raymond",
    "last_name":"Stallon"
}
tyson = {
    "first_name":"Tyson",
    "last_name":"Woodruff"
}

def printDictionary(dictionary, times=1):
    for i in range(0, times):
        for key in dictionary:
            print dictionary[key]

printDictionary(tyson)
printDictionary(raymond)

i = 0
while(i < 5):
    print "hello"
    i = i+1