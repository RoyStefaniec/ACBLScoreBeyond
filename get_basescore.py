def get_basescore(contract_level,tricks_taken, suit, is_vulnerable, doubled, redoubled):

    if doubled and redoubled:
        raise ValueError("Contract cannot be both doubled and redoubled.")
    
    base_points = {
        "part_score": 50,
        "doubled part_score": 100,
        "redoubled part_score": 150,
        "game": 300 if not is_vulnerable else 500,
        "doubled game": 350 if not is_vulnerable else 550,
        "redoubled game": 400 if not is_vulnerable else 600,
        "small_slam": 500 if not is_vulnerable else 750,
        "grand_slam": 1000 if not is_vulnerable else 1500
    }
    contract_level = int(contract_level)
    tricks_taken = int(tricks_taken)
    if contract_level == 7:
        return base_points["grand_slam"]
    if contract_level == 6:
        return base_points["small_slam"]

    is_game = (contract_level >= 3 and suit in ["No Trump"]) or \
              (contract_level >= 4 and suit in ["Hearts", "Spades"]) or \
              (contract_level == 5 and suit in ["Clubs", "Diamonds"]) or \
              (contract_level) == 2 or 3 and suit in ["Hearts", "Spades"] and doubled or \
              (contract_level) == 3 or 4 and suit in ["Clubs", "Diamonds"] and doubled or \
              (contract_level) >= 1 and suit in ["Hearts", "Spades", "No Trump"] and redoubled or \
              (contract_level) >= 2 and suit in ["Clubs", "Diamonds"] and redoubled
    
    if tricks_taken < 6 + contract_level:
        return 0
    if redoubled:
        return base_points["redoubled game"] if is_game else base_points["redoubled part_score"]
    if doubled:
        return base_points["doubled game"] if is_game else base_points["doubled part_score"]
    if is_game:
        return base_points["game"]
    
    return base_points["part_score"]