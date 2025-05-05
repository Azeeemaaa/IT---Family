age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")       # This line is correct

elif age >= 18 and age < 65:        # This line is disabled
    print("You are an adult.")

else age >= 65:   # This line is incorrect
    print("You are a senior citizen.")
