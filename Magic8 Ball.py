import random

name = "Joe"

question = "Yes" or "No"

answer = ""

random_number = random.randint(1,9)
print(random_number)

if random_number == 1:
  print("Yes - definately.")
elif random_number == 2:
  print("it is decidedly so.")
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print(" Reply hazy, try again")
elif random_number == 5:
  print("Ask again later")
elif random_number == 6:
  print("Better not tell you know.")
elif random_number == 7:
  print("My sources say no.")
elif random_number == 8:
  print("Outlook not so good.")
elif random_number == 9:
  print("Vey doubtful")
  print(name + " asks: " + question)
  print(" Magic 8-Ball's anser: " + answer)





