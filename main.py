from graph import *

#make 5 males and 5 females and add it to the network
initial_people = []
for i in range(10):
    initial_people.append(Person(i, "male", 60))
    initial_people.append(Person(i+5, "female", 40))

network = Full_Graph()
for individual in initial_people:
    network.add_person(individual)
network.simulate_network()
network.summarize_network()

