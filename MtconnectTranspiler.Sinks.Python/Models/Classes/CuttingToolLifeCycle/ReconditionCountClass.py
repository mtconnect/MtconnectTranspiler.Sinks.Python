# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;number of times the cutter has been reconditioned.&#10;

"""


class ReconditionCountClass:


    def __init__(self):


        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;maximum number of times the tool may be reconditioned.&#10;

        """

        self.MaximumCount = ""

        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{property(ReconditionCount::value)}} **MUST** be provided for {{block(CuttingTool::CuttingToolLifeCycle)}} and **MUST NOT** be provided for the {{block(CuttingToolArchetype::CuttingToolLifeCycle)}}.&#10;

        """

        self.Value = ""



