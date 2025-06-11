class CoordinateSystemEnum(MTCEnum):
	
		Machine = "   unchangeable coordinate system that has machine zero as its origin.   "
		
		Work = "   coordinate system that represents the working area for a particular workpiece whose origin is shifted within the `MACHINE` coordinate system.  If the `WORK` coordinates are not currently defined in the piece of equipment, the `MACHINE` coordinates will be used.   "
		