class Result:
    _result: list

    _match_count: int
    _mismatch_count: int
    _partial_count: int

    MATCH = "match"
    MISMATCH = "mismatch"
    PARTIAL = "partial"

    def __init__(self) -> None:
        self._result = []
        self._match_count = 0
        self._mismatch_count = 0
        self._partial_count = 0

    def _append_to_result(self, word: str, type: str) -> None:
        self._result.append({"word": word, "type": type})

    def add_match(self, word: str) -> None:
        self._match_count += 1
        self._append_to_result(word, self.MATCH)

    def add_mismatch(self, word: str) -> None:
        self._mismatch_count += 1
        self._append_to_result(word, self.MISMATCH)

    def add_partial(self, word: str) -> None:
        self._partial_count += 1
        self._append_to_result(word, self.PARTIAL)

    def match_count(self) -> int:
        return self._match_count

    def mismatch_count(self) -> int:
        return self._mismatch_count

    def partial_count(self) -> int:
        return self._partial_count

    def summary(self) -> list:
        return self._result
