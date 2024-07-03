from itertools import permutations

def check_constraints(assignment):
    for subject, time_slot in assignment.items():
        for other_subject, other_time_slots in assignment.items():
            if subject != other_subject and time_slot == other_time_slots:
                return False
    return True

def is_valid_assignment(assignment, variable, value):
    # Check if the assignment is valid based on the constraints
    for subject, allowed_values in constraints:
        if variable == subject:
            if value not in allowed_values:
                return False
        elif assignment.get(subject) == value:
            return False
    return True

def backtrack_search(assignment, variables, domains):
    if len(assignment) == len(variables):
        return assignment

    unassigned = [v for v in variables if v not in assignment]
    first = unassigned[0]

    for value in domains:
        if is_valid_assignment(assignment, first, value):
            assignment[first] = value
            result = backtrack_search(assignment, variables, domains)
            if result is not None:
                return result
            assignment.pop(first)

    return None

constraints = [("PROG1", ["Tues_12:00-14:00", "Wed_13:00-15:00"]),
              ("OOP", [
                  "Mon_16:00-18:00", "Tues_16:00-18:00", "Wed_16:00-18:00",
                  "Thurs_16:00-18:00"
              ]),
              ("MT", [
                  "Mon_14:00-16:00", "Tues_14:00-16:00", "Wed_14:00-16:00",
                  "Thurs_14:00-16:00"
              ]),
              ("CSys", [
                  "Mon_16:00-18:00", "Tues_16:00-18:00", "Wed_16:00-18:00",
                  "Thurs_18:00-20:00"
              ]),
              ("WAD",
               ["Mon_14:00-16:00", "Tues_16:00-18:00", "Wed_14:00-16:00"]),
              ("ML", ["Wed_14:00-16:00", "Thurs_16:00-18:00"])]



def schedule_classes(courses_timeslots):
    # Extract the courses and timeslots from the input
    variables = [course for course, _ in courses_timeslots]
    domains = [timeslot for _, timeslots in courses_timeslots for timeslot in timeslots]

    solution = backtrack_search({}, variables, domains)

    return solution



solution = schedule_classes(constraints)
print(solution)
