class Task:
    def __init__(self):
        self._taskDescription =  _taskDescription
        self._highRisk = False
        self._duration = 3
    def getTaskDescription(self):
        return self.taskDescription
    def setTaskDescription(self, newTaskDescription):
        self._taskDescription = newTaskDescription
    def getHighRisk(self):
        return self.highRisk
    def setHighRisk(self, isHighRisk):
        self._highRisk = isHighRisk

    def getDuration(self):
        return self._duration
    def setDuration(self, newDuration):
        self._duration = newDuration
    def determineEstimation(self):
        pass
    class TaskError(Exception):
        "This class will be used when the user has an incorrect input."



        
    
