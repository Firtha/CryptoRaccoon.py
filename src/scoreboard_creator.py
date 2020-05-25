import json
import data_collector


def json_formatted(json_input):
    formatted_data = json.dumps(json_input, indent = 4)
    return formatted_data

def update_scoreboard():
    data_user = data_collector.get_file_data()
    data_scoreboard = data_collector.get_file('src/scoreboard.json')
    users_score = []
    for key in data_user['players']:
        for value in key['save']:
            user_score = (key['name'], value['score'] )
            users_score.append(user_score)
        # print(json_formatted(key['save']))
        # print(key['save'][0]['score'])
    
    for user_score in users_score:
        print(user_score)

    print("fin de la fonction")    
    print(users_score)




update_scoreboard()