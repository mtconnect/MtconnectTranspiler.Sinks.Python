# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;distance from the gauge plane or from the end of the shank to the furthest point on the tool, if a gauge plane does not exist, to the cutting reference point determined by the main function of the tool.

The {{block(CuttingTool)}} functional length will be the length of the entire tool, not a single cutting item. Each {{block(CuttingItem)}} can have an independent {{block(FunctionalLength)}} represented in its measurements. &#10;

"""


class FunctionalLengthClass(MeasurementClass):


    def __init__(self):


        # TODO: Import CodeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Code = "LF"

        # TODO: Import UnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Units = "MILLIMETER"



