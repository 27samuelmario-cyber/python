class Television:
    """
    A class representing a Television remote controls.
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Set default values for status, mute, volume, and channel.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turn the TV on or off.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute or unmute the TV when powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel, wrapping to minimum if at maximum.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the channel, wrapping to maximum if at minimum.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase the volume up to maximum and unmute.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume down to minimum and unmute.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str :
        """
        Return the formatted string showing the TV's status.
        """
        if self.__muted:
            display_volume = Television.MIN_VOLUME
        else:
            display_volume = self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}"

