#graph with male and female nodes

class Full_Graph:
    def __init__(self):
        self.graph = {}

    def add_person(self, new_person):
        self.graph[new_person] = []
        if new_person.gender == "male":
            for person in self.graph:
                if person != new_person and person.gender == "female":
                    self.graph[person].append(new_person)
                    self.graph[new_person].append(person)
        if new_person.gender == "female":
            for person in self.graph:
                if person != new_person and person.gender == "male":
                    self.graph[person].append(new_person)
                    self.graph[new_person].append(person)
        

# a person has several traits
# male/female
# %chance to swipe right, from 0 to 100
class Person:
    def __init__(self, gender, swipe_chance):
        self.gender = gender
        self.swipe_chance = swipe_chance


