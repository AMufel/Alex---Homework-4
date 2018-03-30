tasks = ('Wake up', 'Brush my teeth', 'Drink water and take my vitamins', 'Get dressed', 'Take the subway',  'go to work',  'Eat breakfast', 'once Im at work I eat lunch around 12', 'Go to bed', 'have interesting dreams')

def daily(major_tasks):
        print("I will {} at 6:30 and {}. I'll {} before heading out the door. I'll usually leave my house at 7, and I quickly {}. I {} {} in midtown Manhattan. My working hours are 7:40/45 - 5/5:30 so I usually dont {} home, and {}. Usually, I {} at 10PM and {}.".format(*major_tasks))


daily(major_tasks=tasks)
