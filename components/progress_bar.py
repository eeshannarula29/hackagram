"""File contains a progress bar used for loading visualization"""


class ProgressBar:
    """The class represents a progress bar

    Private Attribute Instances:
    - _sections: the number of sections in the loading bar
    - _progress: the percentage progress made so far
    """
    def __init__(self, sections: int) -> None:
        self._sections = sections
        self._progress = 0

    def get_bar(self) -> str:
        """Return the current progress bar string"""
        # calculate the number of filled bars
        bars = (self._progress / 100) * self._sections
        # loop through each bar to check if it is checked or not
        string_so_far = '|'
        for section in range(1, self._sections + 1):
            # if the progress is more that or equal to the current bar
            if section <= bars:
                string_so_far += '='
            # if the progress is less than the bar
            else:
                string_so_far += ' '

        return string_so_far + '|'

    def increment(self) -> None:
        self._progress += 1

    def decrement(self) -> None:
        self._progress -= 1

    @property
    def finished(self) -> bool:
        """Return whether the progress bar is finished loading"""
        return self._sections == (self._progress / 100) * self._sections

    @property
    def progress_percentage(self) -> int:
        return self._progress

    @property
    def progress(self) -> float:
        return (self._progress / 100) * self._sections
