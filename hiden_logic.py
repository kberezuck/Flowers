def get_based_price(freshness: float, stem_lenght: float):
    if freshness <= 50 or stem_lenght <= 50:  # в % и см
        based_price = 5
        return based_price
    elif 50 < freshness < 100 and 50 < stem_lenght <= 100:
        based_price = 10
        return based_price
    elif freshness == 100 and 50 < stem_lenght <= 100:
        based_price = 15
        return based_price


def get_life_time(freshness: float):
    if freshness < 50:  # in %
        life_time = 24 # in hours
        return life_time
    elif 50 <= freshness < 100:
        life_time = 48
        return life_time
    else:
        life_time = 72
        return life_time