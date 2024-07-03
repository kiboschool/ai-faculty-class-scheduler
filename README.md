# Kibo Faculty Class Scheduler

The objective of this assignment is to develop an AI agent to assist Kibo in scheduling live classes for instructors. The process is as follows:

- Each instructor will provide their available time slots.
- Each instructor is assigned to teach a specific course.
- Classes cannot be scheduled on weekends or Fridays.
- Each class will be scheduled for a duration of 2 hours.
- There can be a maximum of 2 classes per day with at least a 1-hour break between them.

Here is a sample of the input data for October 2023:

```
course,taught_by,time_slots
PROG1,Mohammed,Tues:12:00-15:00,Wed:12:00-15:00
OOP,David,Mon:16:00-20:00,Tues:16:00-20:00,Wed:16:00-20:00,Thurs:16:00-20:00
MT,Santiago,Mon:14:00-18:00,Tues:14:00-18:00,Wed:14:00-18:00,Thurs:14:00-18:00
CSys,David,Mon:16:00-20:00,Tues:16:00-20:00,Wed:16:00-20:00,Thurs:16:00-20:00
TSP,Mohammed,Tues:12:00-15:00,Wed:12:00-15:00
WAD,Olaperi,Mon:14:00-18:00,Tues:14:00-18:00,Wed:14:00-18:00
ML,Wasiu,Wed:14:00-18:00,Thurs:16:00-20:00
```

Your task is to write a program that will generate a schedule for the October 2023 semester. The output must be in the following format:

```
{'course1': 'time_slot', 'course2': 'time_slot', ...}
```

Example:

```
{'PROG1': 'Tues_12:00-14:00', 'OOP': 'Mon_16:00-18:00', 'MT': 'Mon_14:00-16:00', 'CSys': 'Tues_16:00-18:00', 'WAD': 'Wed_14:00-16:00', 'ML': 'Thurs_16:00-18:00'}
```

The main function that will be called is `schedule_classes`. You must have the same function signature as shown below, otherwise, your code will not pass the tests.
    
```python
def schedule_classes(courses):
    pass
```

Example of the data that will be passed to the function:

```python
courses_timeslots = [("PROG1", ["Tues_12:00-14:00", "Wed_13:00-15:00"]),
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

```

Sample output:

```python
{'PROG1': 'Tues_12:00-14:00', 'OOP': 'Mon_16:00-18:00', 'MT': 'Mon_14:00-16:00', 'CSys': 'Tues_16:00-18:00', 'WAD': 'Wed_14:00-16:00', 'ML': 'Thurs_16:00-18:00'}
```


## Hints
- You can begin by extracting the variables and domains from the courses_timeslots provided above.
- Then, implement the backtrack_search algorithm, passing an initial empty assignment, the domain data, and the variables.

## AI Supoprt
ChatGPT is doign great job in data manipulation. You can use ChatGPT in this assignment to help you extract parts of the input data as per your need.
You are not allowed to use ChatGPT, or any other AI tool, to solve assignments for you and paste it as your own work. This will lead to a zero grade for the assignment and you will be reported to the university for plagiarism.
