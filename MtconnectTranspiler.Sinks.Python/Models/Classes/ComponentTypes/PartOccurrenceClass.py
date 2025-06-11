# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Part)}} that exists at a specific place and time, such as a specific instance of a bracket at a specific timestamp.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{block(PartId)}} **MUST** be defined for {{block(PartOccurrence)}}.&#10;
&#10;&#10;&#10;Example&#10;&#10;&#10;&#10;
~~~~xml
<Parts id="partOccSet">
   <Components>
	   <PartOccurrence id="partOccur">
		 <DataItems>
		   <DataItem id="partSet" category="EVENT" representation="TABLE" type ="COMPONENT_DATA">
			  <Definition>
				 <EntryDefinitions>
					  <EntryDefinition keyType="PART_UNIQUE_ID"/>
				 </EntryDefinitions>
				 <CellDefinitions>
					<CellDefinition key="partNumber" type="PART_KIND_ID" subType="PART_NUMBER"/>
					<CellDefinition key="batchId" type="PART_GROUP_ID" subType="BATCH"/>
					<CellDefinition key="quantity" type="PART_COUNT" subType="TARGET"/>
					<CellDefinition key="actualCompleteTime" type="PROCESS_TIME" subType="COMPLETE"/>
					<CellDefinition key="partState" type="PROCESS_STATE"/>
				</CellDefinitions>
			  </Definition>
			</DataItem>
		 </DataItems>
	   </PartOccurrence>
	</Components>
</Parts>
~~~~
{: caption="XML Device Model Example for PartOccurrence and ComponentData"}


~~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="/styles/Streams.xsl"?>
<MTConnectStreams>
  <Streams>
    <DeviceStream name="VMC-3Axis" uuid="test_27MAY">
      <ComponentStream component="PartOccurrence" name="partSet" componentId="partOccur">
        <Events>
          <ComponentDataTable dataItemId="partSet" timestamp="2020-10-28T19:45:43.070010Z" sequence="95" count="2">
            <Entry key="part1">
              <Cell key="actualStartTime">2009-06-15T00:00:00.000000</Cell>
              <Cell key="partId">part1</Cell>
              <Cell key="partName">SomeName</Cell>
              <Cell key="uniqueID">abc-123</Cell>
            </Entry>
            <Entry key="part2">
              <Cell key="actualStartTime">2009-06-15T00:00:00.007925</Cell>
              <Cell key="partId">part2</Cell>
              <Cell key="partName">AnotherName</Cell>
              <Cell key="uniqueID">def-123</Cell>
            </Entry>
          </ComponentDataTable>
        </Events>
      </ComponentStream>
    </DeviceStream>
  </Streams>
</MTConnectStreams>
~~~~
{: caption="XML Streams Response Example for PartOccurrence and ComponentData"}&#10;

"""


class PartOccurrenceClass(PartClass):


    def __init__(self):


        # TODO: Import PartIdClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesPartId = ""

        # TODO: Import PartUniqueIdClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesPartUniqueId = ""

        # TODO: Import PartGroupIdClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesPartGroupId = ""

        # TODO: Import PartKindIdClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesPartKindId = ""

        # TODO: Import PartCountClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesPartCount = ""

        # TODO: Import PartStatusClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesPartStatus = ""

        # TODO: Import ProcessOccurrenceIdClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesProcessOccurrenceId = ""

        # TODO: Import ProcessTimeClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesProcessTime = ""

        # TODO: Import UserClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesUser = ""



