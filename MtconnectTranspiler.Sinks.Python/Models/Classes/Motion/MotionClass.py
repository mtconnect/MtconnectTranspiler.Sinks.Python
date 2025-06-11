# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;movement of the component relative to a coordinate system. &#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{block(Motion)}} specifies the kinematic chain of the {{block(component)}} entities.

At most only one of {{block(Origin)}} or {{block(Transformation)}} **MUST** be defined for a {{block(Motion)}}.&#10;

"""


class MotionClass:


    def __init__(self):


        # TODO: Import MotionActuationTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;describes if this component is actuated directly or indirectly as a result of other motion.&#10;

        """

        self.Actuation = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;coordinate system within which the kinematic motion occurs.&#10;

        """

        self.CoordinateSystemIdRef = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for this element.&#10;

        """

        self.Id = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;pointer to the {{property(Motion::id)}}.
        
        The kinematic chain connects all components using the parent relations. All motion is connected to the motion of the parent. The first node in the chain will not have a parent.&#10;

        """

        self.ParentIdRef = ""

        # TODO: Import MotionTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of motion.&#10;

        """

        self.Type = ""

        # TODO: Import AxisClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasAxis = ""

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

        # TODO: Import DescriptionClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasDescription = ""



