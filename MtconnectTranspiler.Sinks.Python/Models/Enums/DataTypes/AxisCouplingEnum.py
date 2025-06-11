class AxisCouplingEnum(MTCEnum):
	
		Tandem = "   axes are physically connected to each other and operate as a single unit.   "
		
		Synchronous = "   axes are not physically connected to each other but are operating together in lockstep.   "
		
		Master = "   axis is the master of the {{block(CoupledAxes)}}.   "
		
		Slave = "   axis is a slave to the {{block(CoupledAxes)}}.   "
		