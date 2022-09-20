from importlib import resources
import json


__version__ = "0.4.1"

ALL_QUESTIONS = json.loads(resources.read_text("pyneng_quiz", "questions.json"))
