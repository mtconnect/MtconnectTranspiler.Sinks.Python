# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;constrained process spindle speed for the tool in revolutions/minute.

The {{property(ProcessSpindleSpeed::value)}} **MAY** contain the nominal process target spindle speed if available. If {{block(ProcessSpindleSpeed)}} is provided, at least one value of {{property(ProcessSpindleSpeed::maximum)}}, {{property(ProcessSpindleSpeed::nominal)}}, or {{property(ProcessSpindleSpeed::minimum)}} **MUST** be specified.&#10;

"""


class ProcessSpindleSpeedClass:


    def __init__(self):


        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;upper bound for the tool’s target spindle speed.&#10;

        """

        self.Maximum = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;lower bound for the tools spindle speed.&#10;

        """

        self.Minimum = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;nominal speed the tool is designed to operate at.&#10;

        """

        self.Nominal = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Value = ""



