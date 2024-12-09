from models import BotDifficultyLevel
from strategies.BotPlayingStrategy import BotPlayingStrategy
from strategies.EasyBotPlayingStrategy import EasyBotPlayingStrategy


class BotPlayingStrategyFactory:

    @staticmethod
    def getBotPlayingStrategy(difficulty_level : BotDifficultyLevel) -> BotPlayingStrategy:
        return EasyBotPlayingStrategy()