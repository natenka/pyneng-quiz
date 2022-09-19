from importlib import resources
import json


__version__ = "0.3.7"

ALL_QUESTIONS = json.loads(resources.read_text("pyneng_quiz", "questions.json"))
