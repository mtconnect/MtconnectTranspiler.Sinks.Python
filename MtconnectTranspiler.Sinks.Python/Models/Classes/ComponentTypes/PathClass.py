# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Component)}} that organizes an independent operation or function within a {{block(Controller)}}.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;For many types of equipment, {{block(Path)}} organizes a set of {{block(Axes)}}, one or more Program elements, and the data associated with the motion of a control point as it moves through space. However, it **MAY** also represent any independent function within a {{block(Controller)}} that has unique data associated with that function.
 
{{block(Path)}} **SHOULD** provide an {{block(Execution)}} data item to define the operational state of the {{block(Controller)}} of the piece of equipment.

If the {{block(Controller)}} is capable of performing more than one independent operation or function simultaneously, a separate {{block(Path)}} **MUST** be used to organize the data associated with each independent operation or function.&#10;

"""


class PathClass(ComponentGeneralization):


    def __init__(self):


        # TODO: Import ExecutionClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesExecution = ""

        # TODO: Import ProgramClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesProgram = ""

        # TODO: Import PathFeedrateOverride.ProgrammedClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesPathFeedrateOverrideProgrammed = ""

        # TODO: Import PathFeedrateOverride.RapidClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesPathFeedrateOverrideRapid = ""

        # TODO: Import RotaryVelocityOverrideClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesRotaryVelocityOverride = ""

        # TODO: Import PathFeedrateClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesPathFeedrate = ""

        # TODO: Import PartCountClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesPartCount = ""



