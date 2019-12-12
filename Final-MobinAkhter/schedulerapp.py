from schedule import Schedule
from task import Task
class  SchedulerApp:
    def __init__(self):
        pass
    def run(self):
        numTask=0
        print("Please enter the tasks to schedule")
        descriptionOfTask= input("Task Duration: ")
        try:
            durationOfTask = int(input("Please enter the duration of your task: "))
        except ValueError:
            print("Please enter integers or floats only")
        print("What type of task do you want to be created?")
        try:
            taskType = int(input("1. Regular\n 2. Research\n 3. Design\n 4. Implementation "))
        except ValueError:
            print("Please enter integers only")
        if taskType == 1:
            pass
        elif taskType == 2:
            pass
        elif taskType == 3:
            pass
        elif taskType == 4:
            pass
        choice = input("Would you like to add another task [Y/N]?") 
        if choice == "y" or choice == "Y" or choice.lower()=="yes":
            while True:
                descriptionOfTask= input("Please enter the description of your task: ")
                durationOfTask = int(input("Please enter the duration of your task: "))
                if durationOfTask < 0:
                    print("An error occurred in the program.")
                elif durationOfTask > 100:
                    print("An error occurred in the program.")
                elif durationOfTask == 0:
                    print("An error occurred in the program!")
                else:
                    print("Your duration of task "+descriptionOfTask)
                print("What type of task do you want to be created?")
                taskType = int(input("1. Regular\n 2. Research\n 3. Design\n 4. Implementation "))
                if taskType == 1:
                    pass
                elif taskType == 2:
                    pass
                elif taskType == 3:
                    pass
                elif taskType == 4:
                    pass
            numTask = numTask + 1
        elif choice.lower== "no" or choice == "N" or choice == "n":
            print("======================SCHEDULE=======================")
            print("Number of tasks: "+numTask)
            print("Total duration of the schedule: "+durationOfTask)
            # Running out of time but it had to be calculated after every timeduration given by the user and stored in a variable that keeps count of each entry.
            print("Total Estimation: "+ Task.determineEstimation())

            




