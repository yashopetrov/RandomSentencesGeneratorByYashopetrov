from random import choice
from colorama import Fore


def choose_rand_word(words):
    return choice(words)


names = ["Maria", "Greta", "Mimi", "Peter", "George", "Ivan", "Nicolas"]
cities = ["New York", "San Francisco", "Paris", "London", "Kiev", "Moscow", "Tokyo"]
verbs = ["throws", "eats", "holds", "makes", "sees"]
nouns = ["bananas", "papers", "disco balls", "money", "cucumbers"]
adverbs = ["quickly", "gladly", "fast", "slowly", "sadly"]
details = ["on the street", "around the corner", "on the crosswalk", "under a tree", "in the park"]

print(Fore.GREEN + "Hello! Below is the first random generated sentence:")

while True:
    random_name = choose_rand_word(names)
    random_city_a = choose_rand_word(cities)
    random_city_b = choose_rand_word(cities)
    random_verb = choose_rand_word(verbs)
    random_noun = choose_rand_word(nouns)
    random_adverb = choose_rand_word(adverbs)
    random_details = choose_rand_word(details)
    print(Fore.CYAN + f"{random_name} from {random_city_a} {random_adverb} "
                      f"{random_verb} {random_noun} in {random_city_b}")
    input(Fore.RED + "Click [Enter] to generate a new one.")
