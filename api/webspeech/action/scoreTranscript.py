from .action import Action
from flask import jsonify, Response
from webspeech.score.score import calculate
from .readAloudParagraph import ReadAloudParagraph


class ScoreTranscript(Action):
    schema = {
        "id": {"type": "integer", "min": 0, "required": True},
        "duration": {"type": "float", "min": 1, "max": 700, "required": True},
        "transcript": {"type": "string", "maxlength": 2000, "required": True},
    }

    def __init__(self, logger):
        super(ScoreTranscript, self).__init__(logger)

    def action(self, **kwargs) -> Response:
        self.log(
            "id={} | duration={} | transcript={}".format(
                kwargs["id"], kwargs["duration"], kwargs["transcript"]
            )
        )

        rap = ReadAloudParagraph(self.logger)
        return jsonify(
            calculate(
                base=rap.getParagraph(kwargs["id"]),
                transcript=kwargs["transcript"],
                duration=kwargs["duration"],
            )
        )
