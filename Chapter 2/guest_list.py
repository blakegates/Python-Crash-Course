guestList = ['Einstein', 'Darwin', 'Spielberg']

print(f"Hello {guestList[0]} would you like to come to dinner?")
print(f"Hello {guestList[1]} would you like to come to dinner?")
print(f"Hello {guestList[2]} you're not invited to dinner.")

print(f"{guestList[2]} can't make it.")
del guestList[2]
guestList.insert(2, "Lincoln")
print(f"{guestList[2]} is now coming for dinner instead.")

guestList.append("Kardashian")
print(f"{guestList[3]} you are now invited to dinner.")