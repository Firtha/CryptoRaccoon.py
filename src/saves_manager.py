import json
from datetime import datetime


def getSavedGames():
    print("Hello getSavedGames")
    with open('../Saves/saves.json') as json_file:
        data = json.load(json_file)
        return data


def getUserUnfinishedGames(userName):
    print("Hello getUserSavedGames")
    data = getSavedGames()
    userDatas = []
    for player in data['players']:
        if player['name'] == userName:
            for save in player['saves']:
                if not save['game_over']:
                    userData = [str(save['id']), save['date'], save['score']]
                    userDatas.append(userData)

    return userDatas


def getBestScores():
    print("Hello getBestScores")
    data = getSavedGames()
    savedGames = []
    for player in data['players']:
        for save in player['saves']:
            if save['game_over']:
                savedGame = [player['name'], save['score']]
                savedGames.append(savedGame)

    for x in range(len(savedGames)-1):
        for y in range(x+1, len(savedGames)):
            if float(savedGames[x][1]) < float(savedGames[y][1]):
                tmp = savedGames[x]
                savedGames[x] = savedGames[y]
                savedGames[y] = tmp

    for savedGame in savedGames:
        print(savedGame[0], " -> ", savedGame[1])

    return savedGames


def getNextId(userName):
    print("Hello getNextId")
    data = getSavedGames()
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
                    'score': '%.4f' % userScore,
                    'game_over': False
                })

    with open('../Saves/saves.json', 'w') as outfile:
        json.dump(data, outfile)
