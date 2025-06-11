# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;design characteristics for a piece of equipment.&#10;

"""


class SpecificationClass:


    def __init__(self):


        # TODO: Import DataItemTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;same as {{property(DataItem::type)}}. See {{package(DataItem Types)}}.&#10;

        """

        self.Type = ""

        # TODO: Import DataItemSubTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;same as {{property(DataItem::subType)}}. See {{sect(DataItem)}}.&#10;

        """

        self.SubType = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;reference to the {{property(DataItem::id)}} associated with this entity.&#10;

        """

        self.DataItemIdRef = ""

        # TODO: Import UnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;same as {{property(DataItem::units)}}. See {{sect(DataItem)}}.&#10;

        """

        self.Units = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;reference to the {{property(Composition::id)}} associated with this entity.&#10;

        """

        self.CompositionIdRef = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{property(Specification::name)}} provides additional meaning and differentiates between {{block(Specification)}} entities.&#10;

        """

        self.Name = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;references the {{block(CoordinateSystem)}} for geometric {{block(Specification)}} elements.&#10;

        """

        self.CoordinateSystemIdRef = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for this {{block(Specification)}}.&#10;

        """

        self.Id = ""

        # TODO: Import OriginatorEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;reference to the creator of the {{block(Specification)}}.&#10;

        """

        self.Originator = "MANUFACTURER"

        # TODO: Import MaximumClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasMaximum = ""

        # TODO: Import UpperLimitClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasUpperLimit = ""

        # TODO: Import LowerWarningClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasLowerWarning = ""

        # TODO: Import LowerLimitClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasLowerLimit = ""

        # TODO: Import UpperWarningClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasUpperWarning = ""

        # TODO: Import NominalClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasNominal = ""

        # TODO: Import MinimumClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasMinimum = ""



