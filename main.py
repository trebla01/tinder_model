from graph import *
import random



#make 5 males and 5 females and add it to the network
initial_people = []
for i in range(5):
    initial_people.append(Person("male", 70))
    initial_people.append(Person("female", 30))
network = Full_Graph()
for individual in initial_people:
    network.add_person(individual)


for user in network.graph:
    m_count = 0
    f_count = 0
    for potential_match in network.graph[user]:
        if potential_match.gender == "male":
            m_count += 1
        else:
            f_count += 1
    print(m_count, f_count)

