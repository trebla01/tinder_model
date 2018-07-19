import random

class Full_Graph:
    def __init__(self):
        # keep a graph of users and all potential matches
        self.graph = {}
        # keep a list of all 1 way matches that are made. Note that the format:(personA, personB), personA swiped right on personB, but not vice versa
        self.half_matches = []
        # keep a list of all 2 way matches
        self.matches = []

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

    def simulate_network(self):
        for user in self.graph:
            for potential_match in self.graph[user]:
                r = random.randint(0,100)
                if r < user.swipe_chance:
                    if (potential_match, user) in self.half_matches:
                        self.half_matches.remove((potential_match, user))
                        self.matches.append((user, potential_match))
                    else:
                        self.half_matches.append((user, potential_match))

    def summarize_network(self):
        self.summarize_matches()

    def summarize_matches(self):
        for match in self.half_matches:
            print("One sided match: ", match)
        for match in self.matches:
            print("Full match: ", match)

    #TODO: finish this
    def summarize_user_experience(self):
        for user in self.graph:
            fail = 0
            success = 0
            for match in self.half_matches:
                if match[0] == user:
                    fail += 1
            for match in self.matches:
                if match[0] == user or match[1] == user:
                    success += 1
            percent_success = success / (success + fail) * 100


# a person has several traits
# male/female
# %chance to swipe right, from 0 to 100
class Person:
    def __init__(self, idx, gender, swipe_chance):
        self.idx = idx
        self.gender = gender
        self.swipe_chance = swipe_chance
    def __repr__(self):
        ret_str = "person " + str(self.idx) + ": " + self.gender
        return ret_str
    def __str__(self):
        ret_str = "person " + str(self.idx) + ": " + self.gender
        return ret_str


