import json


def getSavedGames():
    print("Hello getSavedGames")
    with open('Saves/saves.json') as json_file:
        data = json.load(json_file)
        return data


def getNextId():
    print("Hello getNextId")
    with open('Saves/saves.json') as json_file:
        data = json.load(json_file)
        maxId = 0
        for p in data['saved-games']:
            if p['saveId'] > maxId:
                maxId = p['saveId']
        return maxId + 1


def putSavedGame(userName, userScore, saveId):
    print("Hello putSavedGame")
    data = getSavedGames()
    isExisting = False
    for p in data['saved-games']:
        # If we find an existing saved game
        if p['saveId'] == saveId:
            isExisting = True
            p['userScore'] = '%.4f' % userScore

    # If we need to create a new saved game
    if isExisting == False:
        data['saved-games'].append({
            'saveId': saveId,
            'userName': userName,
            'userScore': '%.4f' % userScore
        })

    with open('Saves/saves.json', 'w') as outfile:
        json.dump(data, outfile)
