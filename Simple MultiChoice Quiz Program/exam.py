import options #load the options file
import time #load time module

username = input("Please enter your name : ")
username = username.title()
test = "Software Engineering"
pyt = "Python Programming"
html = "HTML"

print(f"Welcome to the {test} assessment")

#python test questions and answer check
def py_que():
    global score
    score = 0
    print("1. What function is used to display an out put to the terminal?")
    options.answers(options.opt)
    question1 = input(f"answer: ")
    answer = 'a'
    if question1 == answer:
        score += 1
        print(f"You got it correctly, your score is {score}")

    print("2. Who created Python?")
    options.answers(options.opt1)
    question2 = input(f"answer: ")
    answer1 = 'c'
    if question2 == answer1:
        score += 1
        print(f"You got it correctly, your score is {score}")

    print("3. Which function is used to open the file for reading in python?")
    options.answers(options.opt2)
    question3 = input(f"answer: ")
    answer2 = 'b'
    if question3 == answer2:
        score += 1
        print(f"You got it correctly, your score is {score}")

    print("4. What is the correct method to load a module in Python?")
    options.answers(options.opt3)
    question4 = input(f"answer: ")
    answer3 = 'b'
    if question4 == answer3:
        score += 1
        print(f"You got it correctly, your score is {score}")

    print("5. For tuples and list which is correct?")
    options.answers(options.opt4)
    question5 = input(f"answer: ")
    answer4 = 'b'
    if question5 == answer4:
        score += 1
        print(f"You got it correctly, your score is {score}")

    print("6. Which is mutable out of list and tuple?")
    options.answers(options.opt5)
    question6 = input(f"answer: ")
    answer5 = 'b'
    if question6 == answer5:
        score += 1
        print(f"You got it correctly, your score is {score}")
    print(f"Thank You for taking the {pyt} assessment {username}\nYour score is {score}/6 in {pyt}")
    


#html test questions and answer check
def html_que():
    print("1. HTML stands for?")
    options.answers(options.opt_ht)
    question1 = input(f"answer: ")
    answer = 'b'
    global html_score
    html_score = 0
    if question1 == answer:
        html_score += 1
        print(f"You got it correctly, your score is {html_score}")

    print("2. Correct HTML tag for the largest heading is?")
    options.answers(options.opt_ht1)
    question2 = input(f"answer: ")
    answer1 = 'a'
    if question2 == answer1:
        html_score += 1
        print(f"You got it correctly, your score is {html_score}")

    print("3. What are Empty elements and is it valid?")
    options.answers(options.opt_ht2)
    question3 = input(f"answer: ")
    answer2 = 'b'
    if question3 == answer2:
        html_score += 1
        print(f"You got it correctly, your score is {html_score}")

    print("4. Web pages starts with which ofthe following tag?")
    options.answers(options.opt_ht3)
    question4 = input(f"answer: ")
    answer3 = 'c'
    if question4 == answer3:
        html_score += 1
        print(f"You got it correctly, your score is {html_score}")

    print("5. Character encoding is?")
    options.answers(options.opt_ht4)
    question5 = input(f"answer: ")
    answer4 = 'c'
    if question5 == answer4:
        html_score += 1
        print(f"You got it correctly, your score is {html_score}")

    print("6. How can you open a link in a new browser window?")
    options.answers(options.opt_ht5)
    question6 = input(f"answer: ")
    answer5 = 'b'
    if question6 == answer5:
        html_score += 1
        print(f"You got it correctly, your score is {html_score}")
    print(f"Thank You for taking the {html} assessment {username}")




print("Start a test")

#logic to control number of times each test can be taken
chance = 1
do_py = 0

#Loop for tests when they've not been taken to complete assessment completion
while True:
    choice = input("Enter '1' to start Python\nEnter '2' to start HTML")
    choice = choice.lower()

    if choice == '1' and do_py < chance: 
        py_que()
        do_py += 1

        if do_py <= chance:
            html_que() #call the html test
        
        else:
            print("You've taken all test")
            quit()


    elif choice == '2' and do_py < chance:
        html_que()
        do_py += 1
 
        if do_py <= chance:
            py_que() #call the python test 

    elif do_py == chance:
        #calculate and print the test scores and final in percentage %
        total_score = (html_score + score) / 12 * (100)
        total_score = round(total_score, 1) 
        print("You've taken all test")
        print(f"Thank You for taking the {html} assessment {username}\nYour score is {html_score}/6 in {html}\nYour score is {score}/6 in {test}\nYour total score is {total_score}%")
        print("ending program........")
        time.sleep(3)
        print("Goodbye!")
        quit() #End the program when all tests are taken

    elif choice != '1' or choice != '2':
        print("Come back when you are ready")

    else:
        print("Done")