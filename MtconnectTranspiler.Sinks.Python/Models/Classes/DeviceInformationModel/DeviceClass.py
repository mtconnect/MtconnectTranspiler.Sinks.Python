# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Component)}} composed of a piece of equipment that produces {{termplural(observation)}} about itself.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;A {{block(Device)}} {{termplural(organize)}} its parts as {{block(Component)}} entities.

A {{block(Device)}} **MUST** have a {{property(Device::name)}} and {{property(Device::uuid)}} to identify itself. 

A {{block(Device)}} **MUST** have the following {{block(DataItems)}}: {{block(Availability)}}, {{block(AssetChanged)}}, and {{block(AssetRemoved)}}.

See {{package(Components)}} for more details on the properties of {{block(Device)}}.

> See {{sect(Part Properties of Device)}} for a list of {{term(top level)}} {{block(Component)}} types for a {{block(Device)}}.
&#10;

"""


class DeviceClass(ComponentGeneralization):


    def __init__(self):


        # TODO: Import AuxiliaryClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasAuxiliary = ""

        # TODO: Import ControllerClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasController = ""

        # TODO: Import InterfaceClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasInterface = ""

        # TODO: Import ResourceClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasResource = ""

        # TODO: Import StructureClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasStructure = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;**DEPRECATED** in *MTConnect Version 1.2*.&#10;

        """

        self.Iso841Class = ""

        # TODO: Import object and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;universally unique identifier for the element.&#10;

        """

        self.Uuid = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;MTConnect version of the {{term(Device Information Model)}} used to configure the information to be published for a piece of equipment in an {{term(MTConnect Response Document)}}.&#10;

        """

        self.MtconnectVersion = ""

        # TODO: Import SystemClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasSystem = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;name of an element or a piece of equipment.&#10;

        """

        self.Name = ""

        # TODO: Import PartClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasPart = ""

        # TODO: Import ProcessClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasProcess = ""

        # TODO: Import AxisClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasAxis = ""

        # TODO: Import AdapterClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasAdapter = ""

        # TODO: Import AvailabilityClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesAvailability = ""

        # TODO: Import AssetChangedClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesAssetChanged = ""

        # TODO: Import AssetRemovedClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesAssetRemoved = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;condensed message digest from a secure one-way hash function. {{cite(FIPS PUB 180-4)}}&#10;

        """

        self.Hash = ""



