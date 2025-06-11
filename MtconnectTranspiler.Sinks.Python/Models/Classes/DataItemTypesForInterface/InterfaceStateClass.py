# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{def(InterfaceEventEnum::INTERFACE_STATE)}}

When the {{block(InterfaceState)}} is `DISABLED`, the state of all data items that are specific for the {{term(interaction model)}} associated with that {{block(Interface)}} **MUST** be set to `NOT_READY`.&#10;

"""


class InterfaceStateClass(EventClass):


    def __init__(self):


        # TODO: Import InterfaceEventEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Type = "INTERFACE_STATE"

        # TODO: Import InterfaceStateEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Result = ""



