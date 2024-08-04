import random
class TestApp:
    def __init__(self):
        self.correct_sum = None
        self.list1 = []  # Change to a list
        self.list2 = []
        self.start_new_round()
        # self.score = 0

    def start_new_round(self):
        while True:
            self.list1 = [random.randint(11, 20) for _ in range(10)]  # Generate 10 random numbers
            self.list2 = [random.randint(1, 9) for _ in range(10)]  # Generate 10 random numbers
            if all(x - y < 10 for x, y in zip(self.list1, self.list2)):
                break

if __name__ == '__main__':
    applogic = TestApp()

    applogic.start_new_round()

    print(applogic.list1)
    print(applogic.list2)
    score = applogic.check_score([1, 2, 3, 4])
    print(score)
