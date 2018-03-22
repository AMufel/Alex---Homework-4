tasks = ('Wake up', 'Brush teeth', 'Drink water and vitamins', 'Get dressed', 'Take the subway',  'And go to work',  'Eat breakfast', 'More work and then eat lunch', 'Go to bed', 'Dream')

def daily(major_tasks):
        print("Usually, I'll {} at 6:30 and {}, and I'll {} before heading out the door. I'll usually leave my house at 7, and I quickly {}. I {} to work in midtown Manhattan. My working hours are 7:40/45 - 5/5:30 so I usually dont eat @ home {}, {} and {}. Usually, I {} at 10PM and {}.".format(*major_tasks))


daily(major_tasks=tasks)
