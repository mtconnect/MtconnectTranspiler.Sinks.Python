# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Asset)}} that describes the static cutting tool geometries and nominal values as one would expect from a tool catalog.&#10;

"""


class CuttingToolArchetypeClass(AssetClass):


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;manufacturers of the cutting tool.
        
        This will reference the tool item and adaptive items specifically. The cutting items
        manufacturers’ will be a property of {{block(CuttingItem)}}.
        
        > Note: In {{term(XML)}}, the representation will be a comma(,) delimited list of manufacturer names. See {{sect(CuttingTool Schema Diagrams)}}.&#10;

        """

        self.Manufacturers = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for this assembly.&#10;

        """

        self.SerialNumber = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifier for a class of cutting tools.&#10;

        """

        self.ToolId = ""

        # TODO: Import CuttingToolDefinitionClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasCuttingToolDefinition = ""

        # TODO: Import CuttingToolLifeCycleClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasCuttingToolLifeCycle = ""



