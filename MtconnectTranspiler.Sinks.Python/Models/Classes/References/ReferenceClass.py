# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;pointer to information that is associated with another entity defined elsewhere in the {{block(MTConnectDevices)}} entity for a piece of equipment.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{block(Reference)}} is an abstract entity and will be realized by a specific {{block(Reference)}} type for an {{block(MTConnectDevices)}} entity. See {{sect(ComponentRef)}} and {{sect(DataItemRef)}}.&#10;

"""


class ReferenceClass:


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;pointer to the `id` of an entity that contains the information to be associated with this entity.&#10;

        """

        self.IdRef = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10; name of an element or a piece of equipment.&#10;

        """

        self.Name = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;pointer to the {{property(DataItem::id)}} that contains the information to be associated with this entity.&#10;

        """

        self.DataItemId = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;pointer to the {{property(DataItem::id)}} that contains the information to be associated with this entity.&#10;

        """

        self.RefDataItemId = ""



