def get_score(contract_level, tricks_taken, suit, is_vulnerable, doubled, redoubled):

    contract_level= int(contract_level)
    tricks_taken = int(tricks_taken)
    score = 0

    if tricks_taken >= (contract_level + 6):  # Contract made
        if suit in ["Clubs", "Diamonds"]:
            if doubled:
                score += contract_level * 40
            elif redoubled:
                score += contract_level * 80
            else:
                score += contract_level * 20
        elif suit in ["Hearts", "Spades"]:
            if doubled:
                score += contract_level * 60
            elif redoubled:
                score += contract_level * 120
            else:
                score += contract_level * 30
        elif suit == "No Trump":
            if doubled:
                score += 80 + (contract_level-1) * 60
            elif redoubled:
                score += 160 + (contract_level-1) * 120
            else:
                score += 40 + (contract_level-1) * 30
        else:
            raise ValueError("Invalid suit provided.")
        
        overtricks = max(0, tricks_taken - (contract_level + 6))
        if suit in ["Clubs", "Diamonds"]:
                if doubled:
                    score += overtricks * (200 if is_vulnerable else 100)
                elif redoubled:
                     score += overtricks * (400 if is_vulnerable else 200)
                else:
                    score += overtricks * 20
        elif suit in ["Hearts", "Spades", "No Trump"]:
                if doubled:
                     score += overtricks * (200 if is_vulnerable else 100)
                elif redoubled:
                     score += overtricks * (400 if is_vulnerable else 200)
                else:
                    score += overtricks * 30
    else:  # Contract failed
        undertricks = (contract_level + 6) - tricks_taken
        
        if is_vulnerable:
            if doubled:
                score = -200 - (undertricks - 1) * 300
            elif redoubled:
                score = -400 - (undertricks - 1) * 600
            else:
                score = -100 * undertricks
        else:
            if doubled:
                score = -100 - (undertricks - 1) * 200
            elif redoubled:
                score = -200 - (undertricks - 1) * 400
            else:
                score = -50 * undertricks
    if score == 0:
        raise ValueError("Invalid input combination")

    return score