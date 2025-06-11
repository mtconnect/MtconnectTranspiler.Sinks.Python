# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;logical or physical entity that provides a capability.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{block(Component)}} is an abstract entity and will be realized by specific {{block(Component)}} types for an {{block(MTConnectDevices)}} entity. See {{package(Component Types)}} for more details on the {{block(Component)}} types.

{{block(Component)}} also provides structure for describing the {{term(lower level)}} entities associated with it.

At least one of {{block(Component)}}, {{block(DataItem)}}, or {{block(Reference)}} entities **MUST** be provided for a {{block(Component)}}.

![Component Example](figures/Component%20Example.png "Component Example"){: width="0.8"}

> Note: See {{lst(component-example)}} for the {{term(XML)}} representation of the same example.&#10;

"""


class ComponentGeneralization(ComponentClass):


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for the {{block(Component)}}.&#10;

        """

        self.Id = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;name of the {{block(Component)}}.
        
        When provided, {{property(Component::name)}} **MUST** be unique for all child {{block(Component)}} entities of a parent {{block(Component)}}.&#10;

        """

        self.Name = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;common name associated with {{block(Component)}}.&#10;

        """

        self.NativeName = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;interval in milliseconds between the completion of the reading of the data associated with the {{block(Component)}} until the beginning of the next sampling of that data.
        
        This information may be used by client software applications to understand how often information from a {{block(Component)}} is expected to be refreshed.
        
        The refresh rate for data from all child {{block(Component)}} entities will be the
        same as for the parent {{block(Component)}} element unless specifically overridden by another {{property(Component::sampleInterval)}} provided for the child {{block(Component)}}.&#10;

        """

        self.SampleInterval = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;**DEPRECATED** in *MTConnect Version 1.2*. Replaced by {{property(Component::sampleInterval)}}.&#10;

        """

        self.SampleRate = ""

        # TODO: Import object and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;universally unique identifier for the {{block(Component)}}.&#10;

        """

        self.Uuid = ""

        # TODO: Import DescriptionClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasDescription = ""

        # TODO: Import CompositionClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasComposition = ""

        # TODO: Import ComponentGeneralization and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasComponent = ""

        # TODO: Import ConfigurationClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasConfiguration = ""

        # TODO: Import ComponentGeneralization and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.IsComponentOf = ""

        # TODO: Import DataItemClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Observes = ""

        # TODO: Import ObservationGeneralization and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.MadeObservation = ""

        # TODO: Import ReferenceClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasReference = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;specifies the {{block(CoordinateSystem)}} for this {{block(Component)}} and its children.&#10;

        """

        self.CoordinateSystemIdRef = ""

        # TODO: Import ComponentStreamClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasComponentStream = ""



