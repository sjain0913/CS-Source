class Config:
    diff_settings = ["easy", "medium", "hard"]
    diff = ""
    player_name = ""

    def __init__(self, data):
        self.difficulty(data)

    def to_String(self):
        print(self.diff)

    def difficulty(self, jsonDiff):
        Config.diff = jsonDiff
        if Config.diff == "easy":
            Config.skill_pts_remaining = 16
            Config.money = 1000
        elif Config.diff == "medium":
            Config.money = 500
            Config.skill_pts_remaining = 12
        else:
            Config.money = 100
            Config.skill_pts_remaining = 8

    