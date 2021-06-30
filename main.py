from Reasoning import Reasoning

####################################################################################################################

reasoning_situations = [
    "Tom is heavier than Fred.",
    "John is brighter than Pete.",
    "Wendy is not as strong as Rachel.",
    "Bob is not as happy as Paul.",
    "Carol is not as good as Anne",
    "Bob is faster than Mike.",
    "Val is happier than Rachel.",
    "Claire is not as strong as Kate.",
    "Bill is not as dull as Joe.",
    "Eve is heavier than Wendy.",
    "Mike is weaker than Pete.",
    "Bob is not as tall as Tony.",
    "Sue is lighter than Lucy.",
    "Kate is stronger than Sarah.",
    "Bob is not as heavy as Fred.",
]

reasoning_questions = [
    "Who is heavier?",
    "Who is duller?",
    "Who is weaker?",
    "Who is sadder?",
    "Who is worse?",
    "Who is slower?",
    "Who is happier?",
    "Who is weaker?",
    "Who is brighter?",
    "Who is lighter?",
    "Who is stronger?",
    "Who is taller?",
    "Who is lighter?",
    "Who is stronger?",
    "Who is lighter?"
]

reasoning_options = [
    ["Tom", "Fred"],
    ["John", "Pete"],
    ["Rachel", "Wendy"],
    ["Bob", "Paul"],
    ["Carol", "Anne"],
    ["Bob", "Mike"],
    ["Val", "Rachel"],
    ["Claire", "Kat"],
    ["Bill", "Joe"],
    ["Eve", "Wendy"],
    ["Mike", "Pete"],
    ["Bob", "Tony"],
    ["Sue", "Lucy"],
    ["Kate", "Sarah"],
    ["Bob", "Fred"],
]

reasoning_answers = [
    1,
    2,
    2,
    1,
    1,
    2,
    1,
    1,
    1,
    2,
    2,
    2,
    1,
    1,
    1
]

reasoning_list = [

]

x = 0

while x < len(reasoning_situations):
    reasoning_list.append(Reasoning(reasoning_situations[x], reasoning_questions[x], reasoning_options[x][0],
                                    reasoning_options[x][1], reasoning_answers[x]))
    x += 1
#####################################################################################################################



#####################################################################################################################


print(reasoning_list)
print("Please enter:\n 1. For Reasoning\n 2. For Number Speed and Recovery\n 3. For Word_Meaning")
option_selector = int(input("\nPlease input your desired number here: "))


def main(a_option_selector):
    score = 0
    i = 0
    if a_option_selector == 1:
        while i < len(reasoning_list):
            print("\n" + reasoning_situations[i] + "\n" + reasoning_questions[i] + "\n 1. " + reasoning_options[i][0] +
                  "\n 2. " + reasoning_options[i][1])
            answer = int(input("Answer here: "))

            if answer == reasoning_answers[i]:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
            i += 1

    elif a_option_selector == 2:
        print("\n4 2 8\n 1. 4\n 2. 2\n 3. 8")
        answer = int(input("Answer here: "))
        if answer == 8 or answer == 3:
            print("Correct!")
        else:
            print("Wrong!")

    elif a_option_selector == 3:
        print("\nHalt Cold Stop\n\n 1. Halt\n 2. Cold\n 3. Stop")
        answer = int(input("Answer here: "))
        if answer == 2:
            print("Correct!")
        else:
            print("Wrong!")
    else:
        print("Please print correct option!")

    print("Your score is : " + str(score))


main(option_selector)
