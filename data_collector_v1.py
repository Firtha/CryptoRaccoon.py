import json 

# Name : get_file_data
# For : 
#       -> This function return the content of the json file into a python dict
# When : 
#       -> Use this fonction each time you need to put in a var data from a json file
# Limit : 
#       -> We use a fixed path, this function only get the data from the file src/gamedata.json
def get_file_data():
    path = 'src/gamedata.json'
    with open(path) as json_file:
        json_data = json.load(json_file)
        json_file.close()
        return json_data

# Name: print_json_formatted
# For : 
#       -> this function take a json input then return it with the correct indentation
# When : 
#       -> Use this function to write or print json data
def print_json_formatted(json_input):
    data = json.dumps(json_input, indent = 4)
    return data

# Name : read_json
# For : 
#    -> simple function that take a json file as input and print the content correctly formatted
def read_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return print_json_formatted(data)

# Name : write_json
# for : 
#       -> write data (input) into the given file (path)
def write_json(path, input):
    with open(path, 'w') as json_file:
        json.dump(input, json_file, indent = 4)

# Name : update_username
# For : 
#       -> verify the current username then update it with the given new username
# When : Call this function when you need to update the username
def update_username(username, new_username):
    data = get_file_data()

    pos = get_username_pos(username)
    if pos == None :
        return print("update_username : Error, current username not found")
    
    if get_username_pos(new_username) != None : 
        return print("update_username : Error, New username already exist")
    
    if data['players'][pos]['name'] == username:
        data['players'][pos]['name'] = new_username
        
        path = 'src/gamedata.json'
        json_file = open(path, 'w') 
        json.dump(data, json_file, indent = 4)
        json_file.close()


# Name : update_user_score
# For : 
#       -> Update the score for a given username
# When : Call this function when you need to update the user score
def update_user_score(username, new_score):
    data = get_file_data()
    pos = get_username_pos(username)
    if pos == None :
        return print("update_user_score : Error, Unknown Username")
    
    if data['players'][pos]['name'] == username:
        data['players'][pos]['score'] = new_score
        path = 'src/gamedata.json'
        json_file = open(path, 'w') 
        json.dump(data, json_file, indent = 4)
        json_file.close()
        return print("update_user_score : Succes, user score updated successfuly")
    else : 
        return print("update_user_score : Error")


# Name : get_registered_player
# For : 
#       -> display the name of all registered player
# When : 
#       -> use it
def get_registered_players():
    data = get_file_data()
    try :
        k = 0
        while k != None :
            print(data['players'][k]['name'])
            k += 1
    except : 
        print("---- end of list ----") 
        return k


# function get_username_pos : 
# return the position in the list for a given username 
# improvements : 
#   better error handling  
def get_username_pos(username):
    data = get_file_data()
    try :
        k = 0
        while k != None :
            if data['players'][k]['name'] == username:
                return k
            k += 1
    except : 
        print("Error : end of list") 


# TO REVIEW: probably deprecated
# function is_valid_username
# this function verify if a username is valid
# finalement c'est un doublon avec la fonction juste en dessous get_username_pos
# en effet indirectement la fonction d'en dessous valide la présence du username
# il est donc possible de supprimer cette fonction
# def is_valid_username(input_name):
#     players_registered = get_registered_players()
#     data = get_file_data()
#     isvalid = False
#     username_pos = None
#     k = 0
#     try :
#         while k <= players_registered :
#             if input_name == data['players'][k]['name'] :
#                 isvalid = True
#                 username_pos = k
#             k += 1
#     except : 
#         pass
#     return isvalid, username_pos 



####################################
#############   main   #############
####################################
def main():

    print(read_json('src/gamedata.json'))
    
    print(is_valid_username("patator"))
    
    update_username("Kahoot", "patator")

    update_user_score("patator", 11000)   


if __name__ == "__main__":
    main()