hats = {
    "snapback" : 10,
    "beanie" : 5,
    "baseballcap" : 3
}
hats["weirdtophat"] = 1
hats["snapback"] += 1
del hats["weirdtophat"]

print(hats)
"""C FUNCTION"""
def Summer(LIST):
    Sum = 0 
    for each_number in LIST:
        Sum += each_number
    return Sum

blew = Summer([4,5,2,-3])
print(blew)

sports = ["basketball","softball","football","baseball","track"]

with open("sports.txt", "w") as THEFILE:
    for i in range(5):
        THEFILE.write(sports[i] + "\n")
with open("sports.txt" , "r") as books:
    informed = books.readlines()
    print(informed)