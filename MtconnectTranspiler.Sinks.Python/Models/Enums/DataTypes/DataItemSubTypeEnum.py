class DataItemSubTypeEnum(MTCEnum):
	
		Absolute = "   relating to or derived in the simplest manner from the fundamental units or measurements.   "
		
		Action = "   indication of the operating state of a mechanism.   "
		
		Actual = "   measured or reported value of an {{term(observation)}}.   "
		
		All = "   all actions, items, or activities being counted independent of the outcome.   "
		
		Alternating = "   measurement of alternating voltage or current. If not specified further in statistic, defaults to RMS voltage.   **DEPRECATED** in *Version 1.6*.   "
		
		AScale = "   A-Scale weighting factor on the frequency scale.   "
		
		Auxiliary = "   when multiple locations on a piece of bar stock being feed by a bar feeder are referenced as the indication of whether the end of that piece of bar stock has been reached.   "
		
		Bad = "   actions, items, or activities being counted that do not conform to specification or expectation.   "
		
		Brinell = "   scale to measure the resistance to deformation of a surface.   "
		
		BScale = "   B-Scale weighting factor on the frequency scale.   "
		
		Commanded = "   directive value including adjustments such as an offset or overrides.   "
		
		Consumed = "   amount of material consumed from an object or container during a manufacturing process.   "
		
		Control = "   state of the enabling signal or control logic that enables or disables the function or operation of the entity.   "
		
		CScale = "   C-Scale weighting factor on the frequency scale.   "
		
		Delay = "   elapsed time of a temporary halt of action.   "
		
		Direct = "   DC current or voltage.  **DEPRECATED** in *Version 1.6*.   "
		
		DrYRun = "   setting or operator selection used to execute a test mode to confirm the execution of machine functions.   "
		
		DScale = "   D-Scale weighting factor on the frequency scale.   "
		
		Expiration = "   relating to the expiration or end of useful life for a material or other physical item.   "
		
		FirsTUse = "   relating to the first use of a material or other physical item.   "
		
		Good = "   actions, items, or activities being counted that conform to specification or expectation.   "
		
		Incremental = "   relating to or derived from the last {{term(observation)}}.   "
		
		Jog = "   relating to momentary activation of a function or a movement.  **DEPRECATION WARNING**: May be deprecated in the future.   "
		
		Lateral = "   indication of the position of a mechanism that may move in a lateral direction.   "
		
		Leeb = "   scale to measure the elasticity of a surface.   "
		
		Length = "   reference to a length type tool offset variable.   "
		
		Line = "   state of the power source.   "
		
		Linear = "   direction of motion of a linear motion.   "
		
		Loaded = "   indication that the subparts of a piece of equipment are under load.   "
		
		MachinEAxiSLock = "   setting or operator selection that changes the behavior of the controller on a piece of equipment.   "
		
		Main = "   relating to the primary logic or motion program currently being executed.   "
		
		Maintenance = "   relating to maintenance on the piece of equipment.   "
		
		ManuaLUnclamp = "   indication of the state of an operator controlled interlock that can inhibit the ability to initiate an unclamp action of an electronically controlled chuck.   "
		
		Manufacture = "   related to the production of a material or other physical item.   "
		
		Maximum = "   maximum value.   "
		
		Minimum = "   minimum value.   "
		
		Mohs = "   scale to measure the resistance to scratching of a surface.   "
		
		Motion = "   indication of the open or closed state of a mechanism.   "
		
		NOScale = "   no weighting factor on the frequency scale.   "
		
		Operating = "   piece of equipment that is powered or performing any activity.   "
		
		Operator = "   relating to the person currently responsible for operating the piece of equipment.   "
		
		OptionaLStop = "   setting or operator selection that changes the behavior of the controller on a piece of equipment.    "
		
		Override = "   overridden value.   "
		
		Powered = "   piece of equipment is powered and functioning or {{block(Component)}} that are required to remain on are powered.   "
		
		Primary = "   main or principle.   "
		
		Probe = "   position provided by a measurement probe.  **DEPRECATION WARNING**: May be deprecated in the future.   "
		
		Process = "   relating to production of a part or product on a piece of equipment.   "
		
		Programmed = "   directive value without offsets and adjustments.   "
		
		Radial = "   reference to a radial type tool offset variable.   "
		
		Rapid = "   performing an operation faster or in less time than nominal rate.   "
		
		Remaining = "   remaining measure or count of an action, object or activity.   "
		
		Rockwell = "   scale to measure the resistance to deformation of a surface.   "
		
		Rotary = "   direction of a rotary motion using the right hand rule convention.   "
		
		Schedule = "   identity of a control program that is used to specify the order of execution of other programs.   "
		
		SeTUp = "   relating to the preparation of a piece of equipment for production or restoring the piece of equipment to a neutral state after production.   "
		
		Shore = "   scale to measure the resistance to deformation of a surface.   "
		
		SinglEBlock = "   setting or operator selection that changes the behavior of the controller on a piece of equipment.    "
		
		Standard = "   standard measure of an object or an action.   "
		
		Start = "   boundary when an activity or an event commences.   "
		
		Switched = "   indication of the activation state of a mechanism represented by a {{block(Composition)}}.   "
		
		Target = "   goal of the operation or process.   "
		
		TargeTCompletion = "   relating to the end or completion of an activity or event.   "
		
		TooLChangEStop = "   setting or operator selection that changes the behavior of the controller on a piece of equipment.   "
		
		Useable = "   remaining usable measure of an object or action.   "
		
		Vertical = "   indication of the position of a mechanism that may move in a vertical direction.   "
		
		Vickers = "   scale to measure the resistance to deformation of a surface.   "
		
		Working = "   piece of equipment performing any activity, the equipment is active and performing a function under load or not.   "
		
		IpV4Address = "   IPV4 network address of the {{block(Component)}}.   "
		
		IpV6Address = "   IPV6 network address of the {{block(Component)}}.   "
		
		Gateway = "   Gateway for the {{block(Component)}} network.   "
		
		SubneTMask = "   SubNet mask for the {{block(Component)}} network.    "
		
		VlaNId = "   layer2 Virtual Local Network (VLAN) ID for the {{block(Component)}} network.   "
		
		MaCAddress = "   Media Access Control Address. The unique physical address of the network hardware.   "
		
		Wireless = "   identifies whether the connection type is wireless.   "
		
		License = "   license code to validate or activate the hardware or software.   "
		
		Version = "   version of the hardware or software.    "
		
		ReleasEDate = "   date the hardware or software was released for general use.   "
		
		InstalLDate = "   date the hardware or software was installed.   "
		
		Manufacturer = "   corporate identity for the maker of the hardware or software.   "
		
		Uuid = "   universally unique identifier as specified in ISO 11578 or RFC 4122.   "
		
		SeriaLNumber = "   serial number that uniquely identifies a specific part.   "
		
		RaWMaterial = "   material that is used to produce parts.   "
		
		Lot = "   group of parts tracked as a lot.   "
		
		Batch = "   group of parts produced in a batch.   "
		
		HeaTTreat = "   material heat number.   "
		
		ParTNumber = "   particular part design or model.   "
		
		ParTFamily = "   group of parts having similarities in geometry, manufacturing process, and/or functions.   "
		
		ParTName = "   word or set of words by which a part is known, addressed, or referred to.   "
		
		ProcesSStep = "   step in the process plan that this occurrence corresponds to.    "
		
		ProcesSPlan = "   process plan that a process occurrence belongs to.   "
		
		OrdeRNumber = "   authorization of a process occurrence.   "
		
		ProcesSName = "   word or set of words by which a process being executed (process occurrence) by the device is known, addressed, or referred to.    "
		
		IsOStePExecutable = "   reference to a ISO 10303 Executable.   "
		
		Complete = "   associated with the completion of an activity or event.   "
		
		Active = "   relating to logic or motion program currently executing.   "
		
		Failed = "   actions or activities that were attempted , but failed to complete or resulted in an unexpected or unacceptable outcome.   "
		
		Aborted = "   actions or activities that were attempted, but terminated before they could be completed.   "
		
		Ended = "   boundary when an activity or an event terminates.   "
		
		Waste = "   amount discarded.   "
		
		Part = "   amount included in the {{term(part)}}.   "
		
		Request = "   {{term(request)}} by an {{block(Interface)}} for a task.   "
		
		Response = "   {{term(response)}} by an {{block(Interface)}} to a {{term(request)}} for a task.   "
		
		Activity = "   phase or segment of a recipe or program.   "
		
		Segment = "   phase of a recipe process.   "
		
		Recipe = "   process as part of product production; can be a subprocess of a larger process.   "
		
		Operation = "   step of a discrete manufacturing process.   "
		
		Binary = "   observed as a binary data type.   "
		
		Boolean = "   observed as a boolean data type.   "
		
		Enumerated = "   observed as a set containing a restricted number of discrete values where each discrete value is named and unique. {{cite(ISO 21961:2003, 013)}}   "
		
		Detect = "   indicated by the presence or existence of something.   "
		
		Model = "   model info of the hardware or software.   "
		