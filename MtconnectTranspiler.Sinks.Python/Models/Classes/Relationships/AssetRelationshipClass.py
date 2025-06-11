# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(ConfigurationRelationship)}} that describes the association between a {{block(Component)}} and an {{block(Asset)}}.&#10;

"""


class AssetRelationshipClass(ConfigurationRelationshipClass):


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;uuid of the related {{block(Asset)}}.&#10;

        """

        self.AssetIdRef = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of {{block(Asset)}} being referenced.&#10;

        """

        self.AssetType = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(URI)}} reference to the associated {{block(Asset)}}.&#10;
        &#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{property(AssetRelationship::href)}} **MUST** also include the {{property(Device::uuid)}} for that specific piece of equipment.
        
        {{property(AssetRelationship::href)}} is of type `xlink:href` from the W3C XLink specification: {{cite(https://www.w3.org/TR/xlink11/)}}.&#10;

        """

        self.Href = ""



