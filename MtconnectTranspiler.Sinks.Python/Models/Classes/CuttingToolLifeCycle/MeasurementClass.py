# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;constrained scalar value associated with a cutting tool.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;A {{block(Measurement)}} is specific to the tool management policy at a particular shop. The tool zero reference point or gauge line will be different depending on the particular implementation and will be assumed to be consistent within the shop. MTConnect Standard does not standardize the manufacturing process or the definition of the zero point.&#10;

"""


class MeasurementClass:


    def __init__(self):


        # TODO: Import CodeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;shop specific code for the measurement. 
        
        ISO 13399 codes **MAY** be used for these codes as well. 
        
        See {{package(Cutting Tool Measurement Subtypes)}} and {{package(Cutting Item Measurement Subtypes)}} for details on {{block(Measurement)}} types and their respective {{property(Measurement::code)}} values.&#10;

        """

        self.Code = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;maximum value for the measurement. &#10;

        """

        self.Maximum = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;minimum value for the measurement. &#10;

        """

        self.Minimum = ""

        # TODO: Import NativeUnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;units the measurement was originally recorded in. See {{package(Device Information Model)}} for the complete list of {{property(DataItem::nativeUnits)}}.&#10;

        """

        self.NativeUnits = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;as advertised value for the measurement.&#10;

        """

        self.Nominal = ""

        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;number of significant digits in the reported value. &#10;

        """

        self.SignificantDigits = ""

        # TODO: Import UnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;units for the measurements. See {{package(Device Information Model)}} for the complete list of {{property(DataItem::units)}}.&#10;

        """

        self.Units = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Value = ""



