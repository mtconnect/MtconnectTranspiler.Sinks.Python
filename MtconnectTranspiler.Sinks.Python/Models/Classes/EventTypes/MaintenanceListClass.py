# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{def(EventEnum::MAINTENANCE_LIST)}}

If {{property(MaintenanceList::result::Interval)}} `key` is not provided, it is assumed `ABSOLUTE`.

If {{property(MaintenanceList::result::Direction)}} `key` is not provided, it is assumed `UP`.

If {{property(MaintenanceList::result::Units)}} `key` is not provided, it is assumed to be `COUNT`.&#10;

"""


class MaintenanceListClass(EventClass):


    def __init__(self):


        # TODO: Import EventEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Type = "MAINTENANCE_LIST"

        # TODO: Import MaintenanceListResultClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Result = ""



