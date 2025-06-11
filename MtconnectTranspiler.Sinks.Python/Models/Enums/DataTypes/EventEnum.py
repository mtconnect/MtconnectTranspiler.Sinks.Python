class EventEnum(MTCEnum):
	
		ActivEAxes = "   set of axes currently associated with a {{block(Path)}} or {{block(Controller)}}.   "
		
		ActuatoRState = "   operational state of an apparatus for moving or controlling a mechanism or system.   "
		
		Alarm = "   **DEPRECATED:** Replaced with `CONDITION` category data items in Version 1.1.0.   "
		
		AsseTChanged = "   {{block(assetId)}} of the {{term(Asset)}} that has been added or changed.   "
		
		AsseTRemoved = "   {{block(assetId)}} of the {{term(Asset)}} that has been removed.   "
		
		Availability = "   {{term(agent)}}'s ability to communicate with the data source.   "
		
		AxiSCoupling = "   describes the way the axes will be associated to each other.     This is used in conjunction with `COUPLED_AXES` to indicate the way they are interacting.   "
		
		AxiSFeedratEOverride = "   value of a signal or calculation issued to adjust the feedrate of an individual linear type axis.   "
		
		AxiSInterlock = "   state of the axis lockout function when power has been removed and the axis is allowed to move freely.   "
		
		AxiSState = "   state of a {{block(Linear)}} or {{block(Rotary)}} component representing an axis.   "
		
		Block = "   line of code or command being executed by a {{block(Controller)}} entity.   "
		
		BlocKCount = "   total count of the number of blocks of program code that have been executed since execution started.   "
		
		ChucKInterlock = "   state of an interlock function or control logic state intended to prevent the associated {{block(Chuck)}} component from being operated.   "
		
		ChucKState = "   operating state of a mechanism that holds a part or stock material during a manufacturing process.   It may also represent a mechanism that holds any other mechanism in place within a piece of equipment.   "
		
		Code = "   programmatic code being executed.  **DEPRECATED** in *Version 1.1*.   "
		
		CompositioNState = "   operating state of a mechanism represented by a {{block(Composition)}} entity.   "
		
		ControlleRMode = "   current mode of the {{block(Controller)}} component.   "
		
		ControlleRModEOverride = "   setting or operator selection that changes the behavior of a piece of equipment.   "
		
		CoupleDAxes = "   set of associated axes.   "
		
		DatECode = "   time and date code associated with a material or other physical item.   "
		
		DevicEUuid = "   identifier of another piece of equipment that is temporarily associated with a component of this piece of equipment to perform a particular function.   "
		
		Direction = "   direction of motion.   "
		
		DooRState = "   operational state of a {{block(Door)}} component or composition element.   "
		
		EmergencYStop = "   state of the emergency stop signal for a piece of equipment, controller path, or any other component or subsystem of a piece of equipment.   "
		
		EnDOFBar = "   indication of whether the end of a piece of bar stock being feed by a bar feeder has been reached.   "
		
		EquipmenTMode = "   indication that a piece of equipment, or a sub-part of a piece of equipment, is performing specific types of activities.   "
		
		Execution = "   operating state of a {{block(Component)}}.   "
		
		FunctionaLMode = "   current intended production status of the {{block(Component)}}.   "
		
		Hardness = "   hardness of a material.   "
		
		Line = "   current line of code being executed.  **DEPRECATED** in *Version 1.4.0*.   "
		
		LinELabel = "   identifier for a {{block(Block)}} of code in a {{block(Program)}}.   "
		
		LinENumber = "   position of a block of program code within a control program.   "
		
		Material = "   identifier of a material used or consumed in the manufacturing process.   "
		
		MateriaLLayer = "   identifies the layers of material applied to a part or product as part of an additive manufacturing process.   "
		
		Message = "   information to be transferred from a piece of equipment to a client software application.   "
		
		OperatoRId = "   identifier of the person currently responsible for operating the piece of equipment.   "
		
		PalleTId = "   identifier for a pallet.   "
		
		ParTCount = "   aggregate count of parts.   "
		
		ParTDetect = "   indication designating whether a part or work piece has been detected or is present.   "
		
		ParTId = "   identifier of a part in a manufacturing operation.   "
		
		ParTNumber = "   identifier of a part or product moving through the manufacturing process.  **DEPRECATED** in *Version 1.7*. `PART_NUMBER` is now a `subType` of `PART_KIND_ID`.   "
		
		PatHFeedratEOverride = "   value of a signal or calculation issued to adjust the feedrate for the axes associated with a {{block(Path)}} component that may represent a single axis or the coordinated movement of multiple axes.   "
		
		PatHMode = "   describes the operational relationship between a {{block(Path)}} entity and another {{block(Path)}} entity for pieces of equipment comprised of multiple logical groupings of controlled axes or other logical operations.   "
		
		PoweRState = "   indication of the status of the source of energy for an entity to allow it to perform its intended function or the state of an enabling signal providing permission for the entity to perform its functions.   "
		
		PoweRStatus = "   status of the {{block(Component)}}.  **DEPRECATED** in *Version 1.1.0*.   "
		
		ProcesSTime = "   time and date associated with an activity or event.   "
		
		Program = "   name of the logic or motion program being executed by the {{block(Controller)}} component.   "
		
		PrograMComment = "   comment or non-executable statement in the control program.   "
		
		PrograMEdit = "   indication of the status of the {{block(Controller)}} components program editing mode.  A program may be edited while another is executed.   "
		
		PrograMEdiTName = "   name of the program being edited.   This is used in conjunction with {{block(ProgramEdit)}} when in `ACTIVE` state.    "
		
		PrograMHeader = "   non-executable header section of the control program.   "
		
		PrograMLocation = "   {{term(URI)}} for the source file associated with {{block(Program)}}.   "
		
		PrograMLocatioNType = "   defines whether the logic or motion program defined by {{block(Program)}} is being executed from the local memory of the controller or from an outside source.   "
		
		PrograMNesTLevel = "   indication of the nesting level within a control program that is associated with the code or instructions that is currently being executed.   "
		
		RotarYMode = "   current operating mode for a {{block(Rotary)}} type axis.   "
		
		RotarYVelocitYOverride = "   percentage change to the velocity of the programmed velocity for a {{block(Rotary)}} axis.   "
		
		SeriaLNumber = "   serial number associated with a {{block(Component)}}, {{block(Asset)}}, or {{block(Device)}}.   "
		
		SpindlEInterlock = "   indication of the status of the spindle for a piece of equipment when power has been removed and it is free to rotate.   "
		
		TooLAsseTId = "   identifier of an individual tool asset.   "
		
		TooLGroup = "   identifier for the tool group associated with a specific tool. Commonly used to designate spare tools.   "
		
		TooLId = "   identifier of the tool currently in use for a given `Path`.  **DEPRECATED** in *Version 1.2.0*.   See `TOOL_ASSET_ID`.   "
		
		TooLNumber = "   identifier assigned by the {{block(Controller)}} component to a cutting tool when in use by a piece of equipment.   "
		
		TooLOffset = "   reference to the tool offset variables applied to the active cutting tool.   "
		
		User = "   identifier of the person currently responsible for operating the piece of equipment.   "
		
		Variable = "   data whose meaning may change over time due to changes in the operation of a piece of equipment or the process being executed on that piece of equipment.   "
		
		WaiTState = "   indication of the reason that {{block(Execution)}} is reporting a value of `WAIT`.   "
		
		Wire = "   identifier for the type of wire used as the cutting mechanism in Electrical Discharge Machining or similar processes.   "
		
		WorkholdinGId = "   identifier for the current workholding or part clamp in use by a piece of equipment.  **DEPRECATION WARNING**: Recommend using `FIXTURE_ID` instead.   "
		
		WorKOffset = "   reference to offset variables for a work piece or part.   "
		
		OperatinGSystem = "   Operating System (OS) of a {{block(Component)}}.   "
		
		Firmware = "   embedded software of a {{block(Component)}} .   "
		
		Application = "   application on a {{block(Component)}}.   "
		
		Library = "   software library on a {{block(Component)}}   "
		
		Hardware = "   hardware of a {{block(Component)}}.   "
		
		Network = "   network details of a {{block(Component)}}.   "
		
		Rotation = "   three space angular displacement of an object or coordinate system relative to a {{term(cartesian coordinate system)}}.   "
		
		Translation = "   three space linear displacement of an object or coordinate system relative to a {{term(cartesian coordinate system)}}.   "
		
		DevicEAdded = "   {{term(UUID)}} of new device added to an {{term(MTConnect Agent)}}.   "
		
		DevicERemoved = "   {{term(UUID)}} of a device removed from an {{term(MTConnect Agent)}}.   "
		
		DevicEChanged = "   {{term(UUID)}} of the device whose {{term(metadata)}} has changed.   "
		
		ConnectioNStatus = "   status of the connection between an {{term(adapter)}} and an {{term(agent)}}.   "
		
		AdapteRSoftwarEVersion = "   originator’s software version of the {{term(adapter)}}.   "
		
		AdapteRUri = "   {{term(URI)}} of the {{term(adapter)}}.   "
		
		MTConnectVersion = "   reference version of the MTConnect Standard supported by the {{term(adapter)}}.   "
		
		SensoRAttachment = "   {{term(attachment)}} between a sensor and an entity.   "
		
		ParTStatus = "   state or condition of a part.   "
		
		ProcesSOccurrencEId = "   identifier of a process being executed by the device.   "
		
		ProcesSAggregatEId = "   identifier given to link the individual occurrence to a group of related occurrences, such as a process step in a process plan.   "
		
		ProcesSKinDId = "   identifier given to link the individual occurrence to a class of processes or process definition.    "
		
		ParTGrouPId = "   identifier given to a collection of individual parts.    "
		
		ParTKinDId = "   identifier given to link the individual occurrence to a class of parts, typically distinguished by a particular part design.   "
		
		ParTUniquEId = "   identifier given to a distinguishable, individual part.    "
		
		ControLLimit = "   set of limits used to indicate whether a process variable is stable and in control.  **DEPRECATION WARNING**. Recommend using `CONTROL_LIMITS`.   "
		
		SpecificatioNLimit = "   set of limits defining a range of values designating acceptable performance for a variable.  **DEPRECATION WARNING**. Recommend using `SPECIFICATION_LIMITS`.   "
		
		AlarMLimit = "   set of limits used to trigger warning or alarm indicators.  **DEPRECATION WARNING**. Recommend using `ALARM_LIMITS`.   "
		
		LoaDCount = "   accumulation of the number of times an operation has attempted to, or is planned to attempt to, load materials, parts, or other items.   "
		
		UnloaDCount = "   accumulation of the number of times an operation has attempted to, or is planned to attempt to, unload materials, parts, or other items.   "
		
		TransfeRCount = "   accumulation of the number of times an operation has attempted to, or is planned to attempt to, transfer materials, parts, or other items from one location to another.   "
		
		ActivatioNCount = "   accumulation of the number of times a function has attempted to, or is planned to attempt to, activate or be performed.   "
		
		DeactivatioNCount = "   accumulation of the number of times a function has attempted to, or is planned to attempt to, deactivate or cease.   "
		
		CyclECount = "   accumulation of the number of times a cyclic function has attempted to, or is planned to attempt to execute.   "
		
		ValvEState = "   state of a valve is one of open, closed, or transitioning between the states.   "
		
		LocKState = "   state or operating mode of a {{block(Lock)}}.   "
		
		ProcesSState = "   particular condition of the process occurrence at a specific time.   "
		
		ParTProcessinGState = "   particular condition of the part occurrence at a specific time.   "
		
		OperatinGMode = "   state of {{block(Component)}} or {{block(Composition)}} that describes the automatic or manual operation of the entity.   "
		
		AsseTCount = "   {{term(data set)}} of the number of {{termplural(Asset)}} of a given type for a {{term(Device)}}.   "
		
		MaintenancEList = "   actions or activities to be performed in support of a piece of equipment.   "
		
		FixturEId = "   identifier for the current workholding or part clamp in use by a piece of equipment.   "
		
		ParTCounTType = "   interpretation of `PART_COUNT`.   "
		
		ClocKTime = "   time provided by a timing device at a specific point in time.   "
		
		HosTName = "   name of the host computer supplying data.   "
		
		NetworKPort = "   number of the TCP/IP or UDP/IP port for the connection endpoint.   "
		
		LeaKDetect = "   indication designating whether a leak has been detected.   "
		
		BatterYState = "   present status of the battery.   "
		
		FeaturEPersistenTId = "   {{term(UUID)}} of a {{term(feature)}}. {{cite(ISO 10303 AP 242/239)}}.   "
		
		SensoRState = "   detection result of a sensor.   "
		
		ComponenTData = "   {{block(Event)}} that represents a {{block(Component)}} where the {{block(EntryDefinition)}} identifies the {{block(Component)}} and the {{block(CellDefinition)}}s define the {{block(Component)}}'s observed {{block(DataItem)}}s.   "
		
		WorKOffsets = "   properties of each addressable work offset.   "
		
		TooLOffsets = "   properties of each addressable tool offset.   "
		
		FeaturEMeasurement = "   assessing elements of a {{term(feature)}}.   "
		
		CharacteristiCPersistenTId = "   {{term(UUID)}} of the {{term(characteristic)}}.   "
		
		MeasuremenTType = "   class of measurement being performed. {{cite(QIF 3:2018 Section 6.3)}}   "
		
		MeasuremenTValue = "   measurement based on the measurement type.   "
		
		MeasuremenTUnits = "   engineering units of the measurement.   "
		
		CharacteristiCStatus = "   pass/fail result of the measurement.   "
		
		UncertaintYType = "   method used to compute {{term(standard uncertainty)}}.   "
		
		Uncertainty = "   {{term(uncertainty)}} specified by {{block(UncertaintyType)}}.   "
		
		SpecificatioNLimits = "   set of limits defining a range of values designating acceptable performance for a variable.   "
		
		ControLLimits = "   set of limits used to indicate whether a process variable is stable and in control.   "
		
		AlarMLimits = "   set of limits used to trigger warning or alarm indicators.   "
		
		TooLCuttinGItem = "   references the {{block(CuttingToolLifeCycle)}} {{block(CuttingItem)}} index related to the {{property(CuttingItem::indices)}} of the currently active cutting tool edge.   "
		
		LocatioNAddress = "   structured information that allows the unambiguous determination of an object for purposes of identification and location. {{cite(ISO 19160-4:2017)}}   "
		
		ActivEPoweRSource = "   active energy source for the {{block(Component)}}.   "
		
		LocatioNNarrative = "   textual description of the location of an object or activity.   "
		
		Thickness = "   dimension between two surfaces of an object, usually the dimension of smallest measure, for example an additive layer, or a depth of cut.   "
		
		LocatioNSpatiaLGeographic = "   absolute geographic location defined by two coordinates, longitude and latitude and an elevation.   "
		