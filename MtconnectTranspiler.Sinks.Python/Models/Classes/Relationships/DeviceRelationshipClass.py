# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(ConfigurationRelationship)}} that describes the association between two pieces of equipment that function independently but together perform a manufacturing operation.&#10;

"""


class DeviceRelationshipClass(ConfigurationRelationshipClass):


    def __init__(self):


        # TODO: Import object and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;reference to the {{property(Device::uuid)}} of the associated piece of equipment.&#10;

        """

        self.DeviceUuidRef = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(URI)}} identifying the {{term(agent)}} that is publishing information for the associated piece of equipment. &#10;
        &#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{property(DeviceRelationship::href)}} **MUST** also include the {{property(Device::uuid)}} for that specific piece of equipment.
        
        {{property(href)}} is of type `xlink:href` from the W3C XLink specification: {{cite(https://www.w3.org/TR/xlink11/)}}.&#10;

        """

        self.Href = ""

        # TODO: Import RoleTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;defines the services or capabilities that the referenced piece of equipment provides relative to this piece of equipment.&#10;

        """

        self.Role = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;`xlink:type`**MUST** have a fixed value of `locator` as defined in W3C XLink 1.1 {{cite(https://www.w3.org/TR/xlink11/)}}.&#10;
        &#10;&#10;&#10;Description&#10;&#10;&#10;&#10;If the {{property(DeviceRelationship::href)}} is provided, it **MUST** conform to the {{term(URI)}} syntactic rules as defined in IETF RFC 3986 for Uniform Resource Identifiers. {{cite(https://www.ietf.org/rfc/rfc3986.txt)}}&#10;

        """

        self.XlinkType = ""



