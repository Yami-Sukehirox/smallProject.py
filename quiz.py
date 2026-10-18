questions = ("How many letters in aplahbet?: ",
            "How many elements in periodic table?: ", 
            "What brand does the first flying car introduce?: ", 
            "Which animal is lazy?: ", 
            "What is the largest planet?: ")

options = (("A. 25", "B. 26", "C. 20", "D. 30"), 
           ("A. 118", "B. 110", "C. 120", "D. 111"),
           ("A. Toyota", "B. Tesla", "C. Nissan", "D. Aventudor"), 
           ("A. Dog", "B. Whalw", "C. Capybarra", "D. Cat"), 
           ("A. Mars", "B. Neptune", "C. Saturn", "D. Jupiter"))

answerss = ("B", "A", "B", "C", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-" * 42)
    print(question)
    for option in options[question_num]:
        print (option)

    guess = input("Enter the answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answerss[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")  
        print(f"{answerss[question_num]} is the correct answer")  
    question_num += 1        

print ("=" * 42)
print("    RESULTS")
print("=" * 42)

print("answerss", end= " ")
for answer in answerss:
    print(answer, end=" ")
print()    

print("guesses", end= " ")
for guess in guesses:
    print(guess, end=" ")
print()    

score = int(score / len(questions)) * 100

print(f"Your score is {score}%")