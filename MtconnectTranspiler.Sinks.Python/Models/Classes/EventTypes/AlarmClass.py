# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{def(EventEnum::ALARM)}}&#10;

"""


class AlarmClass(EventClass):


    def __init__(self):


        # TODO: Import EventEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Type = "ALARM"

        # TODO: Import AlarmCodeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of alarm.&#10;

        """

        self.Code = ""

        # TODO: Import AlarmSeverityEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;severity of the alarm.&#10;

        """

        self.Severity = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;native code for the piece of equipment.&#10;

        """

        self.NativeCode = ""

        # TODO: Import AlarmStateEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;state of the alarm.&#10;

        """

        self.State = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;specifies the language of the alarm text.
        
        See {{cite(IETF RFC 4646)}} (http://www.ietf.org/rfc/rfc4646.txt).&#10;

        """

        self.Lang = ""



