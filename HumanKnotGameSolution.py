import random

class Participant:
    def __init__(self, name):
        self.name = name
        self.left_hand = None
        self.right_hand = None
        self.position = 0  # Added to simulate their position in the circle

def knot_is_not_untangled(participants):
    return any(participant.left_hand or participant.right_hand for participant in participants)

def can_move_to_untangle(participant):
    return participant.left_hand or participant.right_hand

def make_move(participant):
    move = None
    if participant.left_hand:
        move = f"{participant.name} releases left hand from {participant.left_hand.name}."
        participant.left_hand.right_hand = None
        participant.left_hand = None
    elif participant.right_hand:
        move = f"{participant.name} releases right hand from {participant.right_hand.name}."
        participant.right_hand.left_hand = None
        participant.right_hand = None
    return move

def can_step_over_or_under(participant):
    return participant.left_hand or participant.right_hand

def step_over_or_under(participant):
    move = None
    if participant.left_hand:
        move = f"{participant.name} steps over {participant.left_hand.name}'s arm."
        participant.left_hand = None
    elif participant.right_hand:
        move = f"{participant.name} steps under {participant.right_hand.name}'s arm."
        participant.right_hand = None
    return move

def can_rotate_or_pivot(participant):
    return participant.left_hand or participant.right_hand

def rotate_or_pivot(participant):
    move = None
    if participant.left_hand:
        move = f"{participant.name} rotates to untangle from {participant.left_hand.name}."
        participant.left_hand = None
    elif participant.right_hand:
        move = f"{participant.name} pivots to untangle from {participant.right_hand.name}."
        participant.right_hand = None
    return move

def communicate_moves(participants):
    print("Participants communicate to coordinate their moves.")

def untangle_human_knot(participants):
    steps = []
    while knot_is_not_untangled(participants):
        for participant in participants:
            if can_move_to_untangle(participant):
                move = make_move(participant)
                if move:
                    steps.append(move)
            elif can_step_over_or_under(participant):
                move = step_over_or_under(participant)
                if move:
                    steps.append(move)
            elif can_rotate_or_pivot(participant):
                move = rotate_or_pivot(participant)
                if move:
                    steps.append(move)
        communicate_moves(participants)
    return steps

def create_human_knot(num_people):
    participants = [Participant(f"Person {i+1}") for i in range(num_people)]
    all_hands = participants * 2
    random.shuffle(all_hands)
    for i in range(0, len(all_hands), 2):
        all_hands[i].left_hand = all_hands[i + 1]
        all_hands[i + 1].right_hand = all_hands[i]
    return participants

num_people = int(input("Enter the number of participants: "))
participants = create_human_knot(num_people)

steps_taken = untangle_human_knot(participants)

for step in steps_taken:
    print(step)
