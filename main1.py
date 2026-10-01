class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cricket - player: {self.__player}, score:{self.__score}")

    def play(self):
        print(f"{self.__player} hits a century. the crowd is going like OHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score Updated to: {self.__score}")
        else:
            print("score cannot be negative :( ")

class Football:
    def __init__(self, player, score):
        self.__score = score
        self.__player = player

    def info(self):
        print(f"Football - player: {self.__player}, score:{self.__score}")

    def play(self):
        print(f"{self.__player} hits 2 hat triccks. the crowd is going like OHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"score updated to:{self.__score}")

        else:
            print("score cannot be negative.")

Cricket = Cricket("Virat Kholi", 105)
Football = Football("Lamine Yamal", 6)

print("===== Sports Scoreboard =====\n")
for sport in (Cricket, Football):
    sport.info()
    sport.play()
    print()

print("----- Direct Change attempt -----")
Cricket.__score = 1000000000000000000000000000000000000000000000000000000000000000000000000000000
print(f"get_score() still shows: {Cricket.get_score()}")

print("\n----- Updating scores -----")
Cricket.set_score(101)
Football.set_score(6)