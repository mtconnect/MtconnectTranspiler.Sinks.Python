# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;organizes the data associated with each {{block(Component)}} entity defined for a {{block(Device)}} in the associated {{term(MTConnectDevices Response Document)}}.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;At least one of {{block(Sample)}}, {{block(Event)}}, or {{block(Condition)}} **MUST** be organized by a {{block(ComponentStream)}} entity.&#10;

"""


class ComponentStreamClass:


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifies the {{block(Component)}} type associated with the {{block(ComponentStream)}}.
        
        Examples of {{property(ComponentStream::component)}} are {{block(Device)}}, {{block(Controller)}}, {{block(Linear)}} and {{block(Loader)}}.&#10;

        """

        self.Component = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifier of the {{block(Component)}} as defined by the {{property(Component::id)}} in the {{term(MTConnectDevices Response Document)}}.&#10;

        """

        self.ComponentId = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;name of the {{block(Component)}} associated with the {{block(ComponentStream)}}.&#10;

        """

        self.Name = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;common name of the {{block(Component)}} associated with the {{block(ComponentStream)}}.&#10;

        """

        self.NativeName = ""

        # TODO: Import object and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;uuid of the {{block(Component)}} associated with the {{block(ComponentStream)}}.&#10;

        """

        self.Uuid = ""

        # TODO: Import EventClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.OrganizesEvent = ""

        # TODO: Import SampleClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.OrganizesSample = ""

        # TODO: Import ConditionClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.OrganizesCondition = ""

        # TODO: Import ComponentGeneralization and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.IsOrganizerFor = ""



