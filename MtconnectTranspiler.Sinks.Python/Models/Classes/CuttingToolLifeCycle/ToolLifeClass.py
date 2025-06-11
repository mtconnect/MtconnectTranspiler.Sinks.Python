# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;cutting tool life as related to the assembly.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{block(ToolLife)}} **MUST** be defined only for the {{block(CuttingToolLifeCycle)}} of {{block(CuttingTool)}} and **MUST NOT** be defined for the {{block(CuttingToolLifeCycle)}} of {{block(CuttingToolArchetype)}}.&#10;

"""


class ToolLifeClass:


    def __init__(self):


        # TODO: Import CountDirectionTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;indicates if the tool life counts from zero to maximum or maximum to zero.&#10;

        """

        self.CountDirection = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;initial life of the tool when it is new.&#10;

        """

        self.Initial = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;end of life limit for the tool.&#10;

        """

        self.Limit = ""

        # TODO: Import ToolLifeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of tool life being accumulated.&#10;

        """

        self.Type = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;point at which a tool life warning will be raised.&#10;

        """

        self.Warning = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;value of {{block(ToolLife)}}.&#10;

        """

        self.Value = ""



