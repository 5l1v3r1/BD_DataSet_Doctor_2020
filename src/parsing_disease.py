
def verify_main_class(item):
    known_diseases = ["MEL", "NV", "SCC-MAL", "VASC", "BAL", "BENO", "BCC", "AK-BW", "BKL", "DF", "Collision"]
    collision_test = []

    collision_test = item.split('-')
    if len(collision_test) > 2:
        for item in collision_test:
            if (item not in known_diseases) or item == "":
                return False
        return True
    if item in known_diseases:
        return True
    return False
