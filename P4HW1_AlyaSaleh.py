def main():
    forLoop()
def forLoop():
    scores = []
    num = int(input("Enter number of scores to total: "))
    for i in range (1, num + 1):
        score = float(input(f'Enter score #{i}: '))
        while score < 0 or score > 100:
            print("INVALID Score entered!!!")
            print('Score should be between 0 and 100')
            score = float(input(f'Enter score #{i}: '))
        scores.append(score)
    print("-"*40)
    print("Score list:", scores)
    lowest = min(scores)
    print(lowest)
    scores.remove(lowest)
    print("modified: ", scores)
    average  = sum(scores)/ len(scores)
    print("Average: ", average )
    print("-"*40)
    if average  >=90:
        print('Your Grade is A')
    elif average  >=80:
        print('Your Grade is B')
    elif average  >=70:
        print('Your Grade is C')
    elif average  >=60:
        print('Your Grade is D')
    else:
        print('Your Grade is F')
    print("-"*40)
    print("press any key to exit")
    input()
main()
