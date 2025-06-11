# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;reference system that associates a unique set of n parameters with each point in an n-dimensional space. {{cite(ISO 10303-218:2004)}}&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;At most only one of {{block(Origin)}} or {{block(Transformation)}} **MUST** be defined for a {{block(CoordinateSystem)}}.&#10;

"""


class CoordinateSystemClass:


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for the coordinate system.&#10;

        """

        self.Id = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;name of the coordinate system.&#10;

        """

        self.Name = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;manufacturer's name or users name for the coordinate system.&#10;

        """

        self.NativeName = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;pointer to the {{property(CoordinateSystem::id)}}.&#10;

        """

        self.ParentIdRef = ""

        # TODO: Import OriginClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasOrigin = ""

        # TODO: Import TransformationClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasTransformation = ""

        # TODO: Import CoordinateSystemTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of coordinate system.&#10;

        """

        self.Type = ""

        # TODO: Import object and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(UUID)}} for the coordinate system.&#10;

        """

        self.Uuid = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;natural language description of the {{block(CoordinateSystem)}}.&#10;

        """

        self.Description = ""



