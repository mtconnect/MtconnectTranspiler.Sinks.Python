class MotionActuationTypeEnum(MTCEnum):
	
		Direct = "   movement is initiated by the component.   "
		
		Virtual = "   motion is computed and is used for expressing an imaginary movement.   "
		
		None = "   no actuation of this axis.  > Note: Actuation of `NONE` can be either a derived `REVOLUTE` or `PRISMATIC` motion or static `FIXED` relationship.   "
		