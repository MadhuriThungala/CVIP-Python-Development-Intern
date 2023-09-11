import time
String="Welcome to python development project phase 2 normal task in coderscave"
wordcount=len(String.split())
print(String)
while True:
    t0=time.time()
    inputtext=str(input("Enter some sentences to test your typing speed:"))
    t1=time.time()
    acc=len(set(inputtext.split())&set(String.split()))
    acc=acc/wordcount
    timetaken=t1-t0
    wordperminute=wordcount/timetaken
    print("WORDPERMINUTE",wordperminute,"ACCURACY",acc,"TIMETAKEN",timetaken)
