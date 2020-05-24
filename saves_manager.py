import json
from datetime import datetime


def getSavedGames():
    print("Hello getSavedGames")
    with open('Saves/saves.json') as json_file:
        data = json.load(json_file)
        return data


def getNextId(userName):
    print("Hello getNextId")
    with open('Saves/saves.json') as json_file:
        data = json.load(json_file)
        maxId = 0
        finded = False
        for player in data['players']:
            if player['name'] == userName:
                print("Save finded for ", userName)
                for save in player['saves']:
                    print("Save finded with id ", save['id'])
                    if save['id'] >= maxId:
                        maxId = save['id']
                        finded = True

        if finded:
            return maxId + 1
        else:
            return 0


def putSavedGame(userName, userScore, saveId):
    print("Hello putSavedGame")
    data = getSavedGames()
    saveExist = False
    playerExist = False
    for player in data['players']:
        if player['name'] == userName:
            playerExist = True
            for save in player['saves']:
                # If we find an existing saved game
                if save['id'] == saveId:
                    saveExist = True
                    save['score'] = '%.4f' % userScore

    # If we need to create a new saved game
    if not saveExist:
        if not playerExist:
            data['players'].append({
                'name': userName,
                'saves': []
            })
        for player in data['players']:
            if player['name'] == userName:
                player['saves'].append({
                    'id': saveId,
                    'date': datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),
                    'score': '%.4f' % userScore
                })

    with open('Saves/saves.json', 'w') as outfile:
        json.dump(data, outfile)
