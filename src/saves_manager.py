import json
from datetime import datetime


# Returns an object containing all saved games for every users
def getSavedGames():
    with open('../Saves/saves.json') as json_file:
        data = json.load(json_file)
        return data


# Returns an object containing unfinished games for a specific user
def getUserUnfinishedGames(userName):
    print("Hello getUserUnfinishedGames")
    data = getSavedGames()
    userDatas = []
    for player in data['players']:
        if player['name'] == userName:
            for save in player['saves']:
                if not save['game_over']:
                    userData = [str(save['id']), save['date'], save['score']]
                    userDatas.append(userData)
    return userDatas


# Returns the number of unfinished games recorded for an user
def countUserUnfinishedGames(userName):
    print("Hello countUserUnfinishedGames")
    data = getSavedGames()
    savesCount = 0
    for player in data['players']:
        if player['name'] == userName:
            for save in player['saves']:
                if not save['game_over']:
                    savesCount += 1
    print("Unfinished games found : ", savesCount)
    return savesCount


# Returns the last saved game datas for a given user
def getLastSave(userName):
    data = getSavedGames()
    lastDate = 0
    lastId = 0
    for player in data['players']:
        if player['name'] == userName:
            for save in player['saves']:
                if not save['game_over']:
                    # This split the data of the data, removing ':' and '-' in order to convert all digits into a big int for later comparison
                    currDate = int(save['date'][:4] + save['date'][5:7] + save['date'][8:10] + save['date'][11:13] + save['date'][14:16] + save['date'][17:19])
                    if currDate > lastDate:
                        lastDate = currDate
                        lastId = int(save['id'])

    # Now that we have the right id, let's extract and return all the associated save object
    for player in data['players']:
        if player['name'] == userName:
            for save in player['saves']:
                if not save['game_over']:
                    if int(save['id']) == lastId:
                        return [save['id'], save['date'], save['score']]
    if lastDate == 0:
        return -1


# Returns an array of string arrays, containing every scores recorded for finished games only
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


# Returns the next ID for game creation, based on the last ID used for a specific user
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


def deleteSavedGame(userName, saveId):
    print("Hello deleteSavedGame for user ", userName, " and id ", saveId)
    data = getSavedGames()
    currPlayer = 0
    for player in data['players']:
        currSave = 0
        for save in player['saves']:
            if save['id'] == int(saveId) and player['name'] == userName:
                del data['players'][currPlayer]['saves'][currSave]
            currSave += 1
        currPlayer += 1

    with open('../Saves/saves.json', 'w') as outfile:
        json.dump(data, outfile)


# Rewrite the saves file with the current game (edit or append, user and save or save only if existing user)
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
                if save['id'] == int(saveId):
                    saveExist = True
                    save['score'] = '%.4f' % userScore
                    save['date'] = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

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
