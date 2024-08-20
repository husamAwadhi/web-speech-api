from flask import request, current_app
from webspeech.routes import bp
from webspeech.action.readAloudParagraph import ReadAloudParagraph
from webspeech.action.scoreTranscript import ScoreTranscript


@bp.route("/reading-task", methods=["POST"])
def get_reading_task():
    init = ReadAloudParagraph(current_app.logger)

    validated = init.validate(request.json)
    id = validated.get("id")

    return init.action(id=id)


@bp.route("/score", methods=["POST"])
def get_score():
    init = ScoreTranscript(current_app.logger)

    validated = init.validate(request.json)
    id = validated.get("id")
    transcript = validated.get("transcript")
    duration = validated.get("duration")

    return init.action(id=id, transcript=transcript, duration=duration)
