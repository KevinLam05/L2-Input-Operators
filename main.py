'''
userName = input("Enter your name: ")
#print("Hey " + userName)

userGrade = input("What grade are you in? ")
print("Hey " + userName + ", " + userGrade + " is a lame grade")

userYear = input("What year were you born? ")
userAge = 2022 - int(userYear)
print(str(userAge) + " is so young!")'''

# Create your own Madlibs
# Have at least 5 inputs 

yName = input("Give me a name: ")
yPronoun = input("Give me your pronoun: ")
yAge = input("Give me an age: ")
yTime = input("Give me a time in the past: ")
yAction = input("Give me an action in past tense: ")
yPlace = input("Give me a place: ")
yTheOtherPerson = input("Give me a different name: ")
yObject = input("Give mean object: ")

print(yName + " is " + yAge + " and " + yTime + " " + yPronoun +  " " + yAction + " " + yTheOtherPerson + " with a " + yObject + " in the " + yPlace)