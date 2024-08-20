from .action import Action
from flask import jsonify, Response


class ReadAloudParagraph(Action):
    paragraphs = [
        {
            "id": 1,
            "paragraph": "The sun was shining brightly in the sky. Birds were singing, and a gentle breeze was blowing through the trees. Children were playing in the park, laughing and running around. It was a perfect day to be outside, enjoying the fresh air and warm weather. Everyone seemed happy and relaxed.",
        },
        {
            "id": 2,
            "paragraph": "As the days grew shorter and the leaves began to change color, Sarah found herself reflecting on the past year. It had been a time of both growth and challenges, with many lessons learned along the way. Though the future was still uncertain, she felt a renewed sense of hope. The autumn air, crisp and cool, seemed to promise new beginnings and the chance to start fresh.",
        },
        {
            "id": 3,
            "paragraph": "The concept of time is often perceived as a linear progression from past to present to future. However, in the realm of theoretical physics, time may not be as straightforward. According to the theory of relativity, time is intrinsically linked to space, forming a four-dimensional fabric known as spacetime. This interconnectedness suggests that time can be affected by factors such as gravity and velocity, leading to phenomena like time dilation, where time appears to pass differently depending on an object's speed or position in a gravitational field.",
        },
    ]

    schema = {
        "id": {"type": "integer", "min": 0, "default": 1},
    }

    def __init__(self, logger):
        super(ReadAloudParagraph, self).__init__(logger)

    def action(self, **kwargs) -> Response:
        self.log("id={}".format(kwargs["id"]))
        return jsonify(
            self.parseResponse(
                next(
                    (item for item in self.paragraphs if item["id"] == (kwargs["id"])),
                    {},
                )
            )
        )

    def parseResponse(self, paragraph) -> str:
        paragraph["hasNext"] = True if paragraph["id"] < len(self.paragraphs) else False
        paragraph["hasPrevious"] = True if paragraph["id"] > 1 else False
        return paragraph

    def getParagraph(self, id: int) -> str:
        paragraph = next((item for item in self.paragraphs if item["id"] == id), {})
        return paragraph.get("paragraph", "")
