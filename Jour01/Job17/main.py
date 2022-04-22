i = 0
while i < 100:
    i = i + 1
    mention = ""
    if(i%5) == 0 and (i%3) == 0 :
        mention = "FizzBuzz"
    elif(i%5) == 0:
         mention = "Buzz"
    elif(i%3) == 0 :
         mention = "Fizz"
         
    print(i," - " ,mention)