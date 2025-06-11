class PathModeEnum(MTCEnum):
	
		Independent = "   path is operating independently and without the influence of another path.   "
		
		Master = "   path provides information or state values that influences the operation of other {{block(DataItem)}} of similar type.   "
		
		Synchronous = "   physical or logical parts which are not physically connected to each other but are operating together.   "
		
		Mirror = "   axes associated with the path are mirroring the motion of the `MASTER` path.   "
		