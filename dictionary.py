
my_dict = {
    "name": 'jk',
    "fav": 'kdrama',
    "fav1": 'chocolates',
    "color" : "black"
}

print("------Keys------")
for i in my_dict.keys():
    print(i)
print("-----Values-----")
for i in my_dict.values():
    print(i)
print("-----Items-----")
for i in my_dict.items():
    print(i)

#copy - copies the dict
this_dict = my_dict.copy()
print(this_dict)

#add items in a dict
this_dict["hello"] = "world"
print(this_dict)

#pop items from a dict
this_dict = this_dict.pop("hello")
print(this_dict)

#clear - empties the dict
this_dict.clear()

#del dict - deletes dict
del this_dict 

#nested - nested dict
subjects = {
    "first_semester" : {
        "IIT" : "CSC109",
        "CProgramming" : "CSC110",
        "DigitalLogic" : "CSC111",
        "MathematicsI" : "MTH112",
        "Physics" : "PHY113" 
    },
    "second_semester" : {
        "DicreteStructure" : "CSC160",
        "ObjectOrientedProgramming" : "CSC161",
        "Microprocessor" : "CSC162",
        "MathematicsII" : "MTH163",
        "StatisticsI" : "STA164"
    },
    "third_semester" : {
        "DataStructuresAndAlgorithms" : "CSC206",
        "NumericalMethod" : "CSC207",
        "ComputerArchitecture" : "CSC208",
        "ComputerGraphics" : "CSC209",
        "StatisticsII" : "STA210"
    }
}


#create three dict and sum up the three dict in a single dict
first_semester = {
        "IIT" : "CSC109",
        "CProgramming" : "CSC110",
        "DigitalLogic" : "CSC111",
        "MathematicsI" : "MTH112",
        "Physics" : "PHY113" 
    }
second_semester = {
        "DicreteStructure" : "CSC160",
        "ObjectOrientedProgramming" : "CSC161",
        "Microprocessor" : "CSC162",
        "MathematicsII" : "MTH163",
        "StatisticsI" : "STA164"
    }
third_semester = {
        "DataStructuresAndAlgorithms" : "CSC206",
        "NumericalMethod" : "CSC207",
        "ComputerArchitecture" : "CSC208",
        "ComputerGraphics" : "CSC209",
        "StatisticsII" : "STA210"
    }

csit_subjects = {
    "first_semester" : first_semester,
    "second_semester" : second_semester,
    "third_semester" : third_semester
}
print("First semester : ",first_semester)
#print(csit_subjects)


