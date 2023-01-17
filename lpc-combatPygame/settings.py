from pygame import Color


class Settings:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    CURRENT_LEVEL = 1
    MAX_PLAYER_POINTS = 4
    MAX_BALL_HITS = 5
    BALL_DRAW_VELOCITY = 8
    FONT_SIZE = 32
    FONT_PATH = "fonts/PressStart2P.ttf"

    SPRITES_PATH = {
        # Put all paths of sprites here. Default path `/sprites/<SPRITE_NAME>.png`
        "SPRITE_NAME": "sprites/example.png",
        "PLAYER_1": "sprites/player_1.png",
        "PLAYER_2": "sprites/player_2.png",
    }

    SOUNDS_PATH = {
        # Put all paths of sounds here. Default path `/sounds/<SOUND_NAME>.wav`
        "SOUND_NAME": "sounds/example.wav"
    }

    COLORS = {
        "BLACK": Color(0, 0, 0),
        "WHITE": Color(255, 255, 255),
        "RED": Color(255, 0, 0),
        "BLUE": Color(31, 104, 163),
        "GREEN": Color(91, 227, 116),
        "SCREEN_ORANGE": Color(217, 177, 69),
        "SCREEN_RED": Color(145, 22, 3),
    }
