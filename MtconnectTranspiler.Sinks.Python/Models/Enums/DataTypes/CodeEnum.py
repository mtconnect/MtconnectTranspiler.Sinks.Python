class CodeEnum(MTCEnum):
	
		Bdx = "   largest diameter of the body of a tool item.   "
		
		Lbx = "   distance measured along the X axis from that point of the item closest to the workpiece, including the cutting item for a tool item but excluding a protruding locking mechanism for an adaptive item, to either the front of the flange on a flanged body or the beginning of the connection interface feature on the machine side for cylindrical or prismatic shanks.   "
		
		Apmx = "   maximum engagement of the cutting edge or edges with the workpiece measured perpendicular to the feed motion.   "
		
		Dc = "   maximum diameter of a circle on which the defined point Pk of each of the master inserts is located on a tool item. The normal of the machined peripheral surface points towards the axis of the cutting tool.   "
		
		Df = "   dimension between two parallel tangents on the outside edge of a flange.   "
		
		Oal = "   largest length dimension of the cutting tool including the master insert where applicable.   "
		
		Dmm = "   dimension of the diameter of a cylindrical portion of a tool item or an adaptive item that can participate in a connection.   "
		
		H = "   dimension of the height of the shank.   "
		
		Ls = "   dimension of the length of the shank.   "
		
		Lux = "   maximum length of a cutting tool that can be used in a particular cutting operation including the non-cutting portions of the tool.   "
		
		Lpr = "   dimension from the yz-plane to the furthest point of the tool item or adaptive item measured in the -X direction.   "
		
		Wt = "   total weight of the cutting tool in grams.   The force exerted by the mass of the cutting tool.   "
		
		Lf = "   distance from the gauge plane or from the end of the shank to the furthest point on the tool, if a gauge plane does not exist, to the cutting reference point determined by the main function of the tool.   The {{block(CuttingTool)}} functional length will be the length of the entire tool, not a single cutting item. Each {{block(CuttingItem)}} can have an independent {{block(FunctionalLength)}} represented in its measurements.    "
		
		Crp = "   theoretical sharp point of the cutting tool from which the major functional dimensions are taken.   "
		
		L = "   theoretical length of the cutting edge of a cutting item over sharp corners.   "
		
		Drva = "   angle between the driving mechanism locator on a tool item and the main cutting edge.   "
		
		Wf = "   distance between the cutting reference point and the rear backing surface of a turning tool or the axis of a boring bar.   "
		
		Ic = "   diameter of a circle to which all edges of a equilateral and round regular insert are tangential.   "
		
		Sig = "   angle between the major cutting edge and the same cutting edge rotated by 180 degrees about the tool axis.   "
		
		Kapr = "   angle between the tool cutting edge plane and the tool feed plane measured in a plane parallel the xy-plane.   "
		
		Psir = "   angle between the tool cutting edge plane and a plane perpendicular to the tool feed plane measured in a plane parallel the xy-plane.   "
		
		NPERA = "   angle of the tool with respect to the workpiece for a given process.   The value is application specific.   "
		
		Bs = "   measure of the length of a wiper edge of a cutting item.   "
		
		SdLx = "   length of a portion of a stepped tool that is related to a corresponding cutting diameter measured from the cutting reference point of that cutting diameter to the point on the next cutting edge at which the diameter starts to change.   "
		
		StAx = "   angle between a major edge on a step of a stepped tool and the same cutting edge rotated 180 degrees about its tool axis.   "
		
		DCx = "   diameter of a circle on which the defined point Pk located on this cutting tool.  The normal of the machined peripheral surface points towards the axis of the cutting tool.   "
		
		Hf = "   distance from the basal plane of the tool item to the cutting point.   "
		
		Re = "   nominal radius of a rounded corner measured in the X Y-plane.   "
		
		LFx = "   distance from the gauge plane or from the end of the shank of the cutting tool, if a gauge plane does not exist, to the cutting reference point determined by the main function of the tool.   This measurement will be with reference to the cutting tool and **MUST NOT** exist without a cutting tool.   "
		
		Bch = "   flat length of a chamfer.   "
		
		Chw = "   width of the chamfer.   "
		
		W1 = "   insert width when an inscribed circle diameter is not practical.   "
		