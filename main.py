from graph import *

# user defined data
num_males = 10
num_females = 10
male_right_swipe = 60
female_right_swipe = 40

initial_people = []
for i in range(num_males):
    initial_people.append(Person(i, "male", male_right_swipe))
for i in range(num_females):
    initial_people.append(Person(i+num_females, "female", female_right_swipe))

network = Full_Graph()
for individual in initial_people:
    network.add_person(individual)
network.simulate_network()
network.summarize_network()

