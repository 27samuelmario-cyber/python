import pytest
from television import Television


class Test:
    def setup_method(self):
        """
        Creates a fresh Television object before every test method.
        """
        self.tv1 = Television()

    def teardown_method(self):
        """
        Cleans up the Television object after every test method.
        """
        del self.tv1

    def test_init(self):
        """
        Tests the status, channel, and volume default values.
        """
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        """
        Tests TV details when power is turned on and then turned off.
        """
        self.tv1.power()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv1.power()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        """
        Tests muting/unmuting when TV is on and off.
        """
        # TV is off and muted / unmuted
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        # TV is on, volume increased once, and TV is muted
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        # TV is on and unmuted
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

    def test_channel_up(self):
        """
        Tests channel_up when off, when on, and wrapping past max.
        """
        # TV is off and channel is increased (should not change)
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        # TV is on and channel is increased
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 1, Volume = 0"

        # Increase channel past maximum value and wraps to minimum
        self.tv1.channel_up()  # channel = 2
        self.tv1.channel_up()  # channel = 3 (MAX)
        self.tv1.channel_up()  # wraps to 0 (MIN)
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        """
        Tests channel_down when off, when on, and wrapping past min.
        """
        # TV is off and channel is decreased
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        # TV is on and channel is decreased past minimum value
        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = True, Channel = 3, Volume = 0"

        # Regular channel decrease
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = True, Channel = 2, Volume = 0"

    def test_volume_up(self):
        """
        Tests volume_up when off, on, muted, and exceeding max.
        """
        # TV is off and volume is increased
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        # TV is on and volume is increased
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

        # TV is on, muted, and volume is increased
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"

        # Increased past maximum value (stays at MAX)
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        """
        Tests volume_down when off, on, muted, and at minimum.
        """
        # TV is off and volume is decreased (should not change)
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        # TV is on; increase to maximum before decreasing to see decreasing effect
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"

        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

        # TV is on, muted, and volume is decreased
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        # Decreased past minimum value (stays at MIN)
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

