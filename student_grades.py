class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self.sorted_scores = None


    def get_by_index(self, index):
        return self.scores[index]


    def count(self):
        return len(self.scores)

    # bonusovy ukoly:

    def best(self):
        return max(self.scores)

    def worst(self):
        return min(self.scores)

    def average(self):
        return sum(self.scores) / len(self.scores)

    def pass_rate(self):
        passed = 0

        for score in self.scores:
            if score >= 50:
                passed += 1

        return passed / len(self.scores)

    def __str__(self):
        return f"StudentsGrades: {self.count()} studentů, průměr {self.average():.1f}"



    # bonusovy ukoly


    def get_grade(self, index):
        points = self.scores[index]

        if points >= 90:
            return "A"
        elif points >= 80:
            return "B"
        elif points >= 70:
            return "C"
        elif points >= 60:
            return "D"
        elif points >= 50:
            return "E"
        else:
            return "F"


    def find(self, value):
        positions = []

        for i in range(len(self.scores)):
            if self.scores[i] == value:
                positions.append(i)

        return positions


    def get_sorted(self):
        numbers = self.scores.copy()

        for i in range(len(numbers)):
            for j in range(len(numbers) - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        return numbers


    def find_sorted(self, value):
        if self.sorted_scores is None:
            print("sorting...")
            self.sorted_scores = self.get_sorted()

        left = 0
        right = len(self.sorted_scores) - 1

        while left <= right:
            middle = (left + right) // 2

            if self.sorted_scores[middle] == value:
                return middle
            elif self.sorted_scores[middle] < value:
                left = middle + 1
            else:
                right = middle - 1

        return None




from student_grades import StudentsGrades

def main():
    results = StudentsGrades([85, 42, 91])
    print(results.count())

if __name__ == "__main__":
    main()