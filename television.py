class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize the Television object with default values.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Turn the TV on and off by changing the value of the status variable.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute and unmute the TV when it's on by changing the value of the muted variable.
        """
        self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the TV channel when it's on. If at the maximum channel, set it to the minimum.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Decrease the TV channel when it's on. If at the minimum channel, set it to the maximum.
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """
        Increase the TV volume when it's on. If at the maximum volume, keep it at the maximum.
        """
        if self.__status:
            self.__muted = False
            self.__volume = min(self.__volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """
        Decrease the TV volume when it's on. If at the minimum volume, keep it at the minimum.
        """
        if self.__status:
            self.__muted = False
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
        """
        Represent the TV object as a string.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
