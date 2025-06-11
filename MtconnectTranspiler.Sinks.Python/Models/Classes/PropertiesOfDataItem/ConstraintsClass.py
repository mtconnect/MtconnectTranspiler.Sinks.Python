# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{termplural(organize)}} a set of expected values that can be reported for a {{block(DataItem)}}.&#10;

"""


class ConstraintsClass:


    def __init__(self):


        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;numeric upper constraint.
        
        If the data reported for a data item is a range of numeric values, the expected value reported **MAY** be described with an upper limit defined by this constraint.&#10;

        """

        self.Maximum = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;numeric lower constraint.
        
        If the data reported for a data item is a range of numeric values, the expected value reported **MAY** be described with a lower limit defined by this constraint.&#10;

        """

        self.Minimum = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;numeric target or expected value.&#10;

        """

        self.Nominal = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;single data value that is expected to be reported for a {{block(DataItem)}}.
        
        {{property(Constraints::Value)}} **MUST NOT** be used in conjunction with any other {{block(Constraint)}} elements.&#10;

        """

        self.Value = ""

        # TODO: Import FilterClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasFilter = ""



