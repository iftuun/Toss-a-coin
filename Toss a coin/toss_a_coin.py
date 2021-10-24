import random

print("welcome to coin toss match....")
c=input("Choose: Head or Tail : ").lower()

generate_random=str(random.randint(1,2))


if generate_random=="1":
    generate_random="head"
    
else:
    generate_random="tail"
    

if c == generate_random:
    print(f"hurray it's {generate_random}, you win")
else:
    print(f"you loose it's {generate_random}")

