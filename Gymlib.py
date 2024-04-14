def add_week(User_data):
    try:
       no_of_weeks =  User_data["no_of_weeks"]
       User_data["no_of_weeks"] = no_of_weeks+1
       User_data[str(no_of_weeks+1)] = {}
    except:
        User_data["no_of_weeks"] = 1
        User_data[1] = {}

def add_group(User_data,week_num,muscle_group):
    try:
        User_data["groups"].append(muscle_group)
        User_data["groups"] = list(set(User_data["groups"]))
    except:
        User_data["groups"] = []
        User_data["groups"].append(muscle_group)
    try:
        
        User_data[str(week_num)][muscle_group] = {}
        
    except:
        print("enter valid week_num")
        
def add_exercise(User_data,week_num,muscle_group,exercise):
    try:
        User_data["exercises"].append(exercise)
        User_data["exercises"] = list(set(User_data["exercises"]))
    except:
        User_data["exercises"] = []
        User_data["exercises"].append(exercise)
    try:
        User_data[str(week_num)][muscle_group][exercise] = {"set":0,"rep":0,"weight":0,"notes":""}
    except:
        print("enter valid arguments")

def update_set(User_data,week_num,muscle_group,exercise,set):
    try:
        User_data[week_num][muscle_group][exercise]["set"] = set
    except:
        print("enter valid arguments")
def update_rep(User_data,week_num,muscle_group,exercise,rep):
    try:
        User_data[week_num][muscle_group][exercise]["rep"] = rep
    except:
        print("enter valid arguments")
def update_weight(User_data,week_num,muscle_group,exercise,weight):
    try:
        User_data[week_num][muscle_group][exercise]["weight"] = weight
    except:
        print("enter valid arguments")
def update_notes(User_data,week_num,muscle_group,exercise,notes):
    try:
        User_data[week_num][muscle_group][exercise]["notes"] = notes
    except:
        print("enter valid arguments")

def new_week_duplicate(User_data):
    try:
        curr_week_no = User_data["no_of_weeks"]
        add_week(User_data)
        curr_week_no = curr_week_no+1
        
        for muscle_group,exercises in User_data[str(curr_week_no-1)].items():
            add_group(User_data,str(curr_week_no),muscle_group)
            for exercise,details in User_data[str(curr_week_no-1)][muscle_group].items():
                add_exercise(User_data,curr_week_no,muscle_group,exercise)
                for detail,values in User_data[str(curr_week_no-1)][muscle_group][exercise].items():
                    User_data[str(curr_week_no)][muscle_group][exercise][detail] = values
            
           
    except:
        print("there are no weeks available")


def save_data(data,file_name = "gym_data"):
    import json
    with open(file_name,"w") as f:
        json.dump(data,f)

def get_number_of_weeks(User_data):
    return User_data["no_of_weeks"]

def get_muscle_group_list(User_data,week_num):
    return sorted(User_data[(week_num)])

def get_exercise_list(User_data,week_num,muscle_grp):
    return sorted(User_data[week_num][muscle_grp])

def remove_week(User_data,week_num):
    try:
        del User_data[str(week_num)]
        User_data["no_of_weeks"] = User_data["no_of_weeks"] - 1
    except:
        pass
def remove_muscle_group(User_data,week_num,muscle_group):
    del User_data[str(week_num)][muscle_group]
   
def remove_exercise(user_data,week_num,musclegrp,exercise):
    del user_data[week_num][musclegrp][exercise]

import json


def load_data( file_name = "gym_data"):
    try:
        with open(file_name,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    

def previous_data_existance(user_data,weeknum,muscle_group,exercise,detail):
    try:
        test =  user_data[weeknum][muscle_group][exercise][detail]
        return 1
    except:
        return 0