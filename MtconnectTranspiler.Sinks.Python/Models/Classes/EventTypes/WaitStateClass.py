# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{def(EventEnum::WAIT_STATE)}}

When {{property(Execution::result)}} is not `WAIT`, {{property(Observation::isUnavailable)}} of {{block(WaitState)}} **MUST** be `true`.&#10;

"""


class WaitStateClass(EventClass):


    def __init__(self):


        # TODO: Import WaitStateEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Result = ""

        # TODO: Import EventEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Type = "WAIT_STATE"



