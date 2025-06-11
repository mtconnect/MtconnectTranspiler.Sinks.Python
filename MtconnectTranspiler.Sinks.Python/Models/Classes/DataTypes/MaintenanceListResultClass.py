# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""

"""


class MaintenanceListResultClass(TableClass):


    def __init__(self):


        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;current interval value of the activity.&#10;

        """

        self.Value = ""

        # TODO: Import MaintenanceListIntervalEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;interval of the value observed.&#10;

        """

        self.Interval = "ABSOLUTE"

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;next date/time stamp that maintenance should be performed.&#10;

        """

        self.NextServiceDate = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;last date/time stamp of the {{term(observation)}} was reset.&#10;

        """

        self.Reset = ""

        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;level of severity on a scale of 1-10.&#10;

        """

        self.Severity = ""

        # TODO: Import MaintenanceListDirectionEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;direction of the value observed.&#10;

        """

        self.Direction = "UP"

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifier of the maintenance activity.&#10;

        """

        self.Name = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;last date/time stamp that maintenance was performed.&#10;

        """

        self.LastServiceDate = ""

        # TODO: Import UnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;same as {{property(DataItem::units)}}. See {{package(Device Information Model)}}.&#10;

        """

        self.Units = "COUNT"

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;target value of the next maintenance.&#10;

        """

        self.Target = ""



