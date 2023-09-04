# write your code here
def padel_court_cost(court_type): 
    if court_type == "indoor" :
        return 30
    elif court_type == "outdoor":
        return 20 
def racket_cost(racket_brand):
    if racket_brand == "Bullpadel" :
        return 100
    elif racket_brand == "Nox" :
        return 140
    elif racket_brand == "Siux" :
        return 200
def padel_balls_cost(ball_boxes):
    if ball_boxes == 1 :
        return 2
    elif ball_boxes == 2 :
        return 3.5
    elif ball_boxes == 3 :
        return 5
def padel_game_cost():
    court_type = input("indoor / outdoor: ")
    racket_brand = input("bullpadel / Nox / Siux :")
    ball_boxes = eval(input("1 / 2 / 3 balls :"))
    total_cost = padel_court_cost(court_type) + racket_cost(racket_brand) + padel_balls_cost(ball_boxes)
    print(f"""court type:{court_type}
racket brand:{racket_brand}
ball boxes :{ball_boxes}
total:{total_cost}""")
    return total_cost
total_cost = padel_game_cost()
print(f"the total cost of the game is {total_cost} kd")