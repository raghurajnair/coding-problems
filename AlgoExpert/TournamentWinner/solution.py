def tournamentWinner(competitions, results):
    WinningTeam = ''
    currentWinningTeam = ''
    competitionResults = {}
    for idx in range(len(competitions)):
        if results[idx] == 0:
            currentWinningTeam = competitions[idx][1]
            if currentWinningTeam in competitionResults:
                competitionResults[currentWinningTeam] += 3
            else:
                competitionResults[currentWinningTeam] = 3
        else:
            currentWinningTeam = competitions[idx][0]
            if currentWinningTeam in competitionResults:
                competitionResults[currentWinningTeam] += 3
            else:
                competitionResults[currentWinningTeam] = 3
        
        if WinningTeam in competitionResults:
            if competitionResults[WinningTeam] < competitionResults[currentWinningTeam]:
                WinningTeam = currentWinningTeam
        else:
            WinningTeam = currentWinningTeam
			
    return WinningTeam