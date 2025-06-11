# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;setting or operator selection that changes the behavior of the controller on a piece of equipment. 

The program execution is stopped after a specific program block is executed when `OPTIONAL_STOP` is `ON`.    

In the case of a G-Code program, a program block containing a M01 code designates the command for an `OPTIONAL_STOP`. 

{{block(Execution)}} **MUST** change to `OPTIONAL_STOP` after a program block specifying an optional stop is executed and the {{block(ControllerModeOverride)}} `OPTIONAL_STOP` selection is `ON`.&#10;

"""


class ControllerModeOverride.OptionalStopClass(ControllerModeOverrideClass):


    def __init__(self):


        # TODO: Import DataItemSubTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.SubType = ""



