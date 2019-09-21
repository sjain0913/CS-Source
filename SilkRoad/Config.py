class Config:
    skill_pts = 0
    sail_skill = 0
    cannon_skill = 0
    barter_skill = 0
    craft_skill = 0
    money = 0
    diff_settings = ["easy", "medium", "hard"]
    diff = ""
    player_name = ""

    @staticmethod
    def difficulty(jsonDiff):
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

    def inc_sailor(self):
        if Config.skill_pts_remaining > 0:
            Config.sail_skill = Config.sail_skill + 1
            Config.skill_pts_remaining = Config.skill_pts_remaining - 1

    def dec_sailor(self):
        if Config.sail_skill > 0:
            Config.sail_skill = Config.sail_skill - 1