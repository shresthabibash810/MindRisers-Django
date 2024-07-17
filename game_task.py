

# Print the count of word
# Guess the first letter
# Guess the second letter
# Guess the third letter and so on

a = 'Bibash'
count = len(a)
print("The Count of the word: ", count)

all_correct = True

for i in range(count):
    while True:
        guess = input(f"Enter a guess for the {i+1}th letter: ")
        if guess == a[i]:
            print(f"The {i+1}th letter is: ", a[i])
            break
        else:
            print("Incorrect Guess")
            all_correct = False
            break

if all_correct:
    print("Congratulations! All letters match their correct positions.")
else:
    print("The position of the indexes does not match.")
         





