from roster import student_roster
import itertools


# Import modules above this line
class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(student_roster)

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        i = self.count
        self.count += 1
        if i < len(self.sorted_names):
            return self.sorted_names[i]
        else:
            raise StopIteration

    def _sort_alphabetically(self, students):
        names = []
        for student_info in students:
            name = student_info['name']
            names.append(name)
        return sorted(names)

    def seating_options(self):
        seat_options = []
        seating_combos = itertools.combinations(self.sorted_names, 2)
        for combo in seating_combos:
            seat_options.append(combo)
        return seat_options

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in student_roster:
            if student['favorite_subject'] == subject:
                selected_students.append((student['name'], subject))
        return selected_students



