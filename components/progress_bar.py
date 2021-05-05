class ProgressBar:
    """The class represents a progress bar"""
    def __init__(self, sections: int) -> None:
        self._sections = sections
        self._progress = 0

    def get_bar(self) -> str:
        """Return the current progress bar string"""
        bars = (self._progress / 100) * self._sections

        string_so_far = '|'
        for section in range(1, self._sections + 1):
            if section <= bars:
                string_so_far += '='
            else:
                string_so_far += ' '

        return string_so_far + '|'

    def increment(self) -> None:
        self._progress += 1

    def decrement(self) -> None:
        self._progress -= 1

    @property
    def finished(self) -> bool:
        return self._sections == (self._progress / 100) * self._sections

    @property
    def progress_percentage(self) -> int:
        return self._progress

    @property
    def progress(self) -> float:
        return (self._progress / 100) * self._sections
