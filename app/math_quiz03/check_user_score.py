def check_user_score(list1, list2, user_answers):
    score = 0
    for i in range(len(list1)):
        if user_answers[i] == list1[i] - list2[i]:
            score += 1
    return score


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    user_answers = [6, 8, 10, 4]
    print(check_user_score(list1, list2, user_answers))
