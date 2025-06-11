# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{term(sensing element)}} of a {{block(Sensor)}}.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;When {{block(Sensor)}} has multiple {{termplural(sensing element)}}, each {{term(sensing element)}} is modeled as a {{block(Channel)}} for the {{block(Sensor)}}. &#10;

"""


class ChannelClass:


    def __init__(self):


        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;Date upon which the {{term(sensor unit)}} was last calibrated to the {{term(sensor element)}}.&#10;

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
        &#10;&#10;&#10;name of the specific {{term(sensing element)}}.&#10;

        """

        self.Name = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;Date upon which the {{term(sensor element)}} is next scheduled to be calibrated with the {{term(sensor unit)}}.&#10;

        """

        self.NextCalibrationDate = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier that will only refer to a specific {{term(sensing element)}}.&#10;

        """

        self.Number = ""

        # TODO: Import DescriptionClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasDescription = ""

        # TODO: Import SensorConfigurationClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.IsChannelOf = ""



