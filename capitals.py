# an array of state dictionaries
# states = [
# {
#     "name": "Alabama",
#     "capital": "Montgomery"
# }, {
#     "name": "Alaska",
#     "capital": "Juneau"
# }, {
#     "name": "Arizona",
#     "capital": "Phoenix"
# }, {
#     "name": "Arkansas",
#     "capital": "Little Rock"
# }, {
#     "name": "California",
#     "capital": "Sacramento"
# }, {
#     "name": "Colorado",
#     "capital": "Denver"
# }, {
#     "name": "Connecticut",
#     "capital": "Hartford"
# }, {
#     "name": "Delaware",
#     "capital": "Dover"
# }, {
#     "name": "Florida",
#     "capital": "Tallahassee"
# }, {
#     "name": "Georgia",
#     "capital": "Atlanta"
# }, {
#     "name": "Hawaii",
#     "capital": "Honolulu"
# }, {
#     "name": "Idaho",
#     "capital": "Boise"
# }, {
#     "name": "Illinois",
#     "capital": "Springfield"
# }, {
#     "name": "Indiana",
#     "capital": "Indianapolis"
# }, {
#     "name": "Iowa",
#     "capital": "Des Moines"
# }, {
#     "name": "Kansas",
#     "capital": "Topeka"
# }, {
#     "name": "Kentucky",
#     "capital": "Frankfort"
# }, {
#     "name": "Louisiana",
#     "capital": "Baton Rouge"
# }, {
#     "name": "Maine",
#     "capital": "Augusta"
# }, {
#     "name": "Maryland",
#     "capital": "Annapolis"
# }, {
#     "name": "Massachusetts",
#     "capital": "Boston"
# }, {
#     "name": "Michigan",
#     "capital": "Lansing"
# }, {
#     "name": "Minnesota",
#     "capital": "St. Paul"
# }, {
#     "name": "Mississippi",
#     "capital": "Jackson"
# }, {
#     "name": "Missouri",
#     "capital": "Jefferson City"
# }, {
#     "name": "Montana",
#     "capital": "Helena"
# }, {
#     "name": "Nebraska",
#     "capital": "Lincoln"
# }, {
#     "name": "Nevada",
#     "capital": "Carson City"
# }, {
#     "name": "New Hampshire",
#     "capital": "Concord"
# }, {
#     "name": "New Jersey",
#     "capital": "Trenton"
# }, {
#     "name": "New Mexico",
#     "capital": "Santa Fe"
# }, {
#     "name": "New York",
#     "capital": "Albany"
# }, {
#     "name": "North Carolina",
#     "capital": "Raleigh"
# }, {
#     "name": "North Dakota",
#     "capital": "Bismarck"
# }, {
#     "name": "Ohio",
#     "capital": "Columbus"
# }, {
#     "name": "Oklahoma",
#     "capital": "Oklahoma City"
# }, {
#     "name": "Oregon",
#     "capital": "Salem"
# }, {
#     "name": "Pennsylvania",
#     "capital": "Harrisburg"
# }, {
#     "name": "Rhode Island",
#     "capital": "Providence"
# }, {
#     "name": "South Carolina",
#     "capital": "Columbia"
# }, {
#     "name": "South Dakota",
#     "capital": "Pierre"
# }, {
#     "name": "Tennessee",
#     "capital": "Nashville"
# }, {
#     "name": "Texas",
#     "capital": "Austin"
# }, {
#     "name": "Utah",
#     "capital": "Salt Lake City"
# }, {
#     "name": "Vermont",
#     "capital": "Montpelier"
# }, {
#     "name": "Virginia",
#     "capital": "Richmond"
# }, {
#     "name": "Washington",
#     "capital": "Olympia"
# }, {
#     "name": "West Virginia",
#     "capital": "Charleston"
# }, {
#     "name": "Wisconsin",
#     "capital": "Madison"
# }, {
#     "name": "Wyoming",
#     "capital": "Cheyenne"
# }]


states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}]



# game gonna run game function
# then ask if play again

#play_game()
# game function
#def play_game():

print('hi')

# slice1 = states[slice(3, 5)]
# print(slice1)

# pop1 = states.pop()
# print(pop1)
# print(states)

# pop0 = states.pop(0)
# print(pop0)

import random

for state in states:
    state["correct"] = 0
    state["wrong"] = 0
# print(states)

total_right = 0
total_wrong = 0


def show_score(state):
    name = state["name"]
    wins = state["correct"]
    losses = state["wrong"]
    print(f"win-loss for {name}: {wins} to {losses}")


def play_game(count):
    global total_right
    global total_wrong
    global states
    random.shuffle(states)
    states = sorted(states, key=lambda x: x["wrong"], reverse=True)
    correct = 0
    wrong = 0
    for i in range(count):
        state = states.pop(0)
        name = state["name"]
        capital = state["capital"]

        guess = input("guess the capitol of "+name+"!: ")
        if guess.upper() == "HINT":
            hint = state["capital"][0:3]
            guess = input(f"hint: {hint}: ")
        if guess.upper() == capital.upper():
            print('good!')
            correct += 1
            total_right += 1
            state["correct"] += 1
            show_score(state)
            print(f"overall score: {correct} to {wrong}")
            # wins = state["correct"]
            # losses = state["wrong"]
            # print(f"win-loss for {name}: {wins} to {losses}")
        else:
            print('bad!')
            wrong += 1
            total_wrong += 1
            state["wrong"] += 1
            show_score(state)
            print(f"overall score: {correct} to {wrong}")
        states.append(state)
    #print(states)
        # x = states[0].get("wrong")
        # print(x)

repeat = True
safety = 0
while repeat:
    rounds = int(input("how many rounds?: "))
    play_game(rounds)
    ask = input("play again y/n?: ")
    if ask == 'n':
        repeat = False
    safety += 1
    if safety > 10:
        repeat = False

print("done!")
print(f"total right: {total_right}")
print(f"total wrong: {total_wrong}")





# nope is wrong
# sorted_states = sorted(states.items(), key=lambda x: x[1])
# print(sorted_states)


#aha here we go
# sorted_states = sorted(states, 
# key=lambda x: x["capital"])


# sorted_states = sorted(states, 
# key=lambda x: x["wrong"], reverse=True)

# print(sorted_states)
