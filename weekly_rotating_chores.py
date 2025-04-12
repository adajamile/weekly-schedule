import random

#everyone in the rotation
all_participants = ["John", "Emily", "Sophia", "Lucas"]

#only these people can cook
chefs = ["Emily", "Lucas"]

#days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#builds a weekly schedule with rotating tasks
def generate_rotating_schedule():
    schedule = {}
    used_today = []

    for day in days_of_week:
        day_tasks = {}
        used_today.clear()

        #pick someone from the chefs list to cook
        chef = random.choice(chefs)
        day_tasks["Cook"] = chef
        used_today.append(chef)

        #pick someone who hasn’t been picked yet to wash dishes
        dish_washer = random.choice([p for p in all_participants if p not in used_today])
        day_tasks["Wash dishes"] = dish_washer
        used_today.append(dish_washer)

        #pick someone else to organize the kitchen
        organizer = random.choice([p for p in all_participants if p not in used_today])
        day_tasks["Organize kitchen"] = organizer

        #save the tasks for the day
        schedule[day] = day_tasks

    return schedule

weekly_schedule = generate_rotating_schedule()

for day, tasks in weekly_schedule.items():
    print(f"\n{day}:")
    for task, person in tasks.items():
        print(f"  - {task}: {person}")
