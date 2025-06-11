# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;configuration for a {{block(Sensor)}}.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;![SensorConfiguration](figures/SensorConfiguration.png "SensorConfiguration"){: width="0.8"}

> Note: See {{sect(Configuration Schema Diagrams)}} for XML schema.&#10;

"""


class SensorConfigurationClass:


    def __init__(self):


        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;Date upon which the {{term(sensor unit)}} was last calibrated.&#10;

        """

        self.CalibrationDate = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;The initials of the person verifying the validity of the calibration data.&#10;

        """

        self.CalibrationInitials = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;Version number for the sensor unit as specified by the manufacturer.&#10;

        """

        self.FirmwareVersion = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;Date upon which the {{term(sensor unit)}} is next scheduled to be calibrated.&#10;

        """

        self.NextCalibrationDate = ""

        # TODO: Import ChannelClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasChannel = ""



