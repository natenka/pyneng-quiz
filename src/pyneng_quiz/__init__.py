from importlib import resources
import json


__version__ = "0.1.0"

ALL_QUESTIONS = json.loads(resources.read_text("pyneng", "questions.json"))
