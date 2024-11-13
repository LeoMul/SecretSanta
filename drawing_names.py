import random as rand
import numpy as np
#import quantumrandom

MAX_ITER = 1000


def draw_names_trial(list_of_names):

    number = len(list_of_names)

    assigned_people = []

    index_list = generate_index_list(number)

    for j in range(0,number):
        #draw indices, remove as we go.
        numleft = len(index_list)
        random_index = rand.randint(0,numleft-1)
        #random_index = quantumrandom.randint(0,numleft-1)
        name_index = index_list[random_index]

        assigned_people.append(list_of_names[name_index])
        index_list.remove(name_index)
        
    return assigned_people

def check_for_someone_assigned_to_self(people,assigned_people):

    #returns True if someone is self assigned. False otherwise. i.e False = good

    length = len(people)
    length2 = len(assigned_people)
    assert(length == length2),"length disparity between number of people and assigned people"

    for i in range(0,length):
        if people[i] == assigned_people[i]:
            return True

    return False

def draw_until_noone_has_themselves(list_of_names):
    print("Commencing name drawing.")
    checker = True 
    counter = 0
    while (checker == True) and (counter < MAX_ITER):
        #draw until we noone has themselves
        assigned_names = draw_names_trial(list_of_names)
        checker = check_for_someone_assigned_to_self(list_of_names,assigned_names)
        counter = counter + 1

    assert(counter != MAX_ITER), "max iter reached, stopping"
    print("Drawing names complete. Iterations: {:3}".format(counter))
    return assigned_names

def reveal_names(people,assigned_people):
    out_string = '{:20} has been assigned {:20}'

    for ii in range(0,len(people)):
        print(out_string.format(people[ii],assigned_people[ii]))
        


def generate_index_list(number):
    index_list = []

    for i in range(0,number):
        index_list.append(i)

    return index_list

