class CoordinateSystemTypeEnum(MTCEnum):
	
		World = "   stationary coordinate system referenced to earth, which is independent of the robot motion. {{cite(ISO 9787:2013)}}  For non-robotic devices, stationary coordinate system referenced to earth, which is independent of the motion of a piece of equipment.   "
		
		Base = "   coordinate system referenced to the base mounting surface. {{cite(ISO 9787:2013)}}  A base mounting surface is a connection surface between the arm and its supporting structure.{{cite(ISO 9787:2013)}}  For non-robotic devices, it is the connection surface between the device and its supporting structure.   "
		
		Object = "   coordinate system referenced to the object. {{cite(ISO 9787:2013)}}   "
		
		Task = "   coordinate system referenced to the site of the task. {{cite(ISO 9787:2013)}}   "
		
		MechanicaLInterface = "   coordinate system referenced to the mechanical interface. {{cite(ISO 9787:2013)}}   "
		
		Tool = "   coordinate system referenced to the tool or to the end effector attached to the mechanical interface. {{cite(ISO 9787:2013)}}   "
		
		MobilEPlatform = "   coordinate system referenced to one of the components of a mobile platform. {{cite(ISO 8373:2012)}}   "
		
		Machine = "   coordinate system referenced to the home position and orientation of the primary axes of a piece of equipment.   "
		
		Camera = "   coordinate system referenced to the sensor which monitors the site of the task. {{cite(ISO 9787:2013)}}   "
		