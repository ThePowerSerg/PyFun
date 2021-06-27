# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    try:
        for participant in participants:
            my_participant_dict[participant] = random.randint(1, 9)
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except Exception:
        return None