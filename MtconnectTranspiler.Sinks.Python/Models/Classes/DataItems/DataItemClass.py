# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;information reported about a piece of equipment.&#10;

"""


class DataItemClass:


    def __init__(self):


        # TODO: Import CategoryEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;specifies the kind of information provided by a data item.&#10;

        """

        self.Category = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;identifier attribute of the {{block(Composition)}} that the reported data is most closely associated.&#10;

        """

        self.CompositionId = ""

        # TODO: Import CoordinateSystemEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;for measured values relative to a coordinate system like {{block(Position)}}, the coordinate system used may be reported.
        
        **DEPRECATED** in *Version 2.0*. Replaced by {{property(Component::coordinateSystemIdRef)}}. &#10;

        """

        self.CoordinateSystem = ""

        # TODO: Import Boolean and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;indication signifying whether each value reported for the {{term(Observation)}} is significant and whether duplicate values are to be suppressed.
        
        If a value is not defined for {{property(DataItem::discrete)}}, the default value **MUST** be `false`.&#10;

        """

        self.Discrete = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for this data item.&#10;

        """

        self.Id = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;name of the data item.&#10;

        """

        self.Name = ""

        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;used to convert the reported value to represent the original measured value.&#10;

        """

        self.NativeScale = ""

        # TODO: Import NativeUnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;native units of measurement for the reported value of the data item.&#10;

        """

        self.NativeUnits = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;rate at which successive samples of a data item are recorded by a piece of equipment.&#10;

        """

        self.SampleRate = ""

        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;number of significant digits in the reported value.&#10;

        """

        self.SignificantDigits = ""

        # TODO: Import StatisticEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of statistical calculation performed on a series of data samples to provide the reported data value.&#10;

        """

        self.Statistic = ""

        # TODO: Import DataItemSubTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;sub-categorization of the {{property(DataItem::type)}}.&#10;

        """

        self.SubType = ""

        # TODO: Import DataItemTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of data being measured. See {{package(DataItem Types)}}.&#10;

        """

        self.Type = ""

        # TODO: Import UnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unit of measurement for the reported value of the data item.&#10;

        """

        self.Units = ""

        # TODO: Import ComponentGeneralization and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.IsObservedBy = ""

        # TODO: Import RepresentationEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;description of a means to interpret data consisting of multiple data points or samples reported as a single value.  
        
        If {{property(DataItem::representation)}} is not specified, it **MUST** be determined to be `VALUE`.
        &#10;

        """

        self.Representation = ""

        # TODO: Import SourceClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasSource = ""

        # TODO: Import ConstraintsClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasConstraint = ""

        # TODO: Import FilterClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasFilter = ""

        # TODO: Import InitialValueClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasInitialValue = ""

        # TODO: Import ResetTriggerClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasResetTrigger = ""

        # TODO: Import ObservationGeneralization and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasObservation = ""

        # TODO: Import DefinitionClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasDefinition = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;associated {{block(CoordinateSystem)}} context for the {{block(DataItem)}}.&#10;

        """

        self.CoordinateSystemIdRef = ""

        # TODO: Import AbstractDataItemRelationshipClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasRelationship = ""



