# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;location of the pot or spindle the cutting tool currently resides in.

If {{property(Location::negativeOverlap)}} or {{property(Location::positiveOverlap)}} is provided, the tool reserves additional locations on either side, otherwise if they are not given, no additional locations are required for this tool.

If the pot occupies the first or last location, a rollover to the beginning or the end of the indexable values may occur. For example, if there are 64 pots and the tool is in pot 64 with a {{property(Location::positiveOverlap)}} of 1, the first pot **MAY** be occupied as well.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{block(Location)}} **MUST** be defined only for the {{block(CuttingToolLifeCycle)}} of {{block(CuttingTool)}} and **MUST NOT** be defined for the {{block(CuttingToolLifeCycle)}} of {{block(CuttingToolArchetype)}}.&#10;

"""


class LocationClass:


    def __init__(self):


        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;number of locations at lower index values from this location.&#10;

        """

        self.NegativeOverlap = ""

        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;number of locations at higher index value from this location.&#10;

        """

        self.PositiveOverlap = ""

        # TODO: Import LocationTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of location being identified. 
        
        When a `POT` or `STATION` type is used, {{property(Location::value)}}**MUST** be a numeric value.&#10;

        """

        self.Type = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;turret associated with a tool.&#10;

        """

        self.Turret = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;tool magazine associated with a tool.&#10;

        """

        self.ToolMagazine = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;tool bar associated with a tool.&#10;

        """

        self.ToolBar = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;tool rack associated with a tool.&#10;

        """

        self.ToolRack = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;automatic tool changer associated with a tool.&#10;

        """

        self.AutomaticToolChanger = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Value = ""



