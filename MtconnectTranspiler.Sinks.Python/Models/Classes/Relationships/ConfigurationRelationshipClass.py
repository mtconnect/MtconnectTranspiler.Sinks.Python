# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;association between two pieces of equipment that function independently but together perform a manufacturing operation.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{block(ConfigurationRelationship)}} is an abstract entity and hence will be realized by specific {{block(ConfigurationRelationship)}} types in an {{block(MTConnectDevices)}} entity. See {{sect(ComponentRelationship)}} and {{sect(DeviceRelationship)}}.&#10;

"""


class ConfigurationRelationshipClass:


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;name associated with this {{block(ConfigurationRelationship)}}.&#10;

        """

        self.Name = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for this {{block(ConfigurationRelationship)}}.&#10;

        """

        self.Id = ""

        # TODO: Import RelationshipTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;defines the authority that this piece of equipment has relative to the associated piece of equipment.&#10;

        """

        self.Type = ""

        # TODO: Import CriticalityTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;defines whether the services or functions provided by the associated piece of equipment is required for the operation of this piece of equipment.&#10;

        """

        self.Criticality = ""



