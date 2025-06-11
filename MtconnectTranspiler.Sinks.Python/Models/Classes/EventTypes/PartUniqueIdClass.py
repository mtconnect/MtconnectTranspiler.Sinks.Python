# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{def(EventEnum::PART_UNIQUE_ID)}}

If no {{property(DataItem::subType)}} is specified, `UUID` is default.&#10;

"""


class PartUniqueIdClass(EventClass):


    def __init__(self):


        # TODO: Import EventEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Type = "PART_UNIQUE_ID"

        # TODO: Import DataItemSubTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.SubType = "UUID"



