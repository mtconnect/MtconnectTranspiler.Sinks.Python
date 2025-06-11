# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;constrained process feed rate for the tool in mm/s.

The {{property(ProcessFeedRate::value)}} **MAY** contain the nominal process target feed rate if available. If {{block(ProcessFeedRate)}} is provided, at least one value of {{property(ProcessFeedRate::maximum)}}, {{property(ProcessFeedRate::nominal)}}, or {{property(ProcessFeedRate::minimum)}} **MUST** be specified.&#10;

"""


class ProcessFeedRateClass:


    def __init__(self):


        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;upper bound for the tool’s process target feedrate.&#10;

        """

        self.Maximum = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;lower bound for the tool's feedrate.&#10;

        """

        self.Minimum = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;nominal feedrate the tool is designed to operate at.&#10;

        """

        self.Nominal = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Value = ""



