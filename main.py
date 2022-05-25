age = input("How old are you? ")

if int(age) > 16:
  is_old = True
else:
  is_old = False

licenced = input("Do you have a licence? ")
if licenced.casefold() == "yes":
  is_licenced = True
else:
  is_licenced = False


if is_old and is_licenced:
  print("You are ready to drive!")
elif is_old:
  print("You are old enough to drive! But you don't have a valid licence...")
elif is_licenced:
  print("You have a valid licence! But you aren't old enough...")
else:
  print("Sorry, you are not allowed to drive...")