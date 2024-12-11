def calculate_love_score(name1, name2):

    true_occurs = 0
    love_occurs = 0
    check_true = "true"
    check_love = "love"

    both_names = (name1+name2).lower()

    for letter_check in both_names:
        if letter_check in check_true:
            true_occurs += 1

    for letter_check in both_names:
        if letter_check in check_love:
            love_occurs += 1

    love_score = str(true_occurs) + str(love_occurs)
    print(love_score)
    
calculate_love_score("Kanye West", "Kim Kardashian")
