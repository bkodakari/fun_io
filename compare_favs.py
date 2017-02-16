brianne_fav_foods = open("brianne_fav_foods.txt")
brianne_favs = brianne_fav_foods.readlines()


maria_fav_foods = open("maria_fav_foods.txt")
maria_favs = maria_fav_foods.readlines()


def stripped_lists_brianne():
    new_list_brianne = []
    for item in brianne_favs:
        brianne_favs_stripped = item.strip()
        new_list_brianne.append(brianne_favs_stripped)
    return new_list_brianne


def stripped_list_maria():
    new_list_maria = []
    for item in maria_favs:
        maria_favs_stripped = item.strip()
        new_list_maria.append(maria_favs_stripped)
    return new_list_maria


def compare_favs():
    for item in stripped_lists_brianne():
        if item in stripped_list_maria():
            print "this item matches"
        else:
            print "we are different"

print stripped_lists_brianne()
print stripped_list_maria()

compare_favs()

brianne_fav_foods.close()
maria_fav_foods.close()
