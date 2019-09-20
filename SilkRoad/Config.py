class Config:
    skill_pts_remaining, pil_skill, fight_skill, merch_skill, eng_skill,  money = 0
    diff_settings = ["easy", "medium", "hard"]
    diff = ""
    player_name = ""

    def difficulty(self, button):
        Config.diff = Config.diff_settings[button]
        if Config.diff == "easy":
            Config.skill_pts_remaining = 16
            Config.money = 1000
        elif Config.diff == "medium":
            Config.money = 500
            Config.skill_pts_remaining = 12
        else:
            Config.money = 100
            Config.skill_pts_remaining = 8


    def inc_pilot():
        if Config.skill_pts_remaining > 0:
            Config.pil_skill = Config.pil_skill + 1
            Config.skill_pts_remaining = Config.skill_pts_remaining - 1


    def dec_pilot():
        if Config.pil_skill > 0:
            Config.pil_skill = Config.pil_skill - 1