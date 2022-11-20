def assign_to_tank(aquarium_creaturess, new_tank_number):
    def apply(x):
        x["tank number"] = new_tank_number
        return x

    return map(apply, aquarium_creaturess)


aquarium_creatures = [
    {"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
    {"name": "ashley", "species": "crab", "tank number": 25,
     "type": "shellfish"},
    {"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
    {"name": "jackie", "species": "lobster", "tank number": 21,
     "type": "shellfish"},
    {"name": "charlie", "species": "clownfish", "tank number": 12,
     "type": "fish"},
    {"name": "olly", "species": "green turtle", "tank number": 34,
     "type": "turtle"}
]

assigned_tanks = assign_to_tank(aquarium_creatures, 42)
print(list(assigned_tanks))