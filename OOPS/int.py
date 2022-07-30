class School:
    Student = "name"


    def __init__(self):
        print("I am a student") 

    def pose(self, section) :
        print(f"I am not a student\n{section}")

Subhra = School()
Subhra.pose("B")