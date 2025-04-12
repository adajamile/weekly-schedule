## weekly kitchen task totator

This is a small python script that builds a weekly task schedule with random assignments; it picks people to cook, wash dishes, and organize the kitchen for each day of the week.

## features:
- Assigns tasks (Cooking, Washing dishes, Organizing kitchen) to different participants every day.
- Rotates tasks to ensure fairness and prevents participants from doing the same task too often.
- The weekly schedule is outputted in the terminal for easy viewing.

## participants:
- **John**
- **Emily**
- **Sophia**
- **Lucas**

## tasks:
- **Cook**: Prepares the meals for the day.
- **Wash dishes**: Cleans the dishes after meals.
- **Organize kitchen**: Tidies up and organizes the kitchen.

## how It Works:
1. The script assigns one of the designated chefs to cook each day.
2. Then, it assigns a participant to wash dishes from those not already assigned tasks.
3. Finally, it assigns a participant to organize the kitchen.
4. The schedule is printed to the terminal at the end.

## usage:
To use this script, simply run it in a Python environment. The schedule will be printed directly in the terminal.

```bash
python weekly_schedule.py
