# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{def(SampleEnum::PATH_POSITION)}}

&#10;
&#10;&#10;&#10;Example&#10;&#10;&#10;&#10;~~~~xml
<DataItem type='PATH_POSITION' id='pathposit1' units="MILLIMETER_3D"/>
~~~~
{: caption="XML Device Model Example for `PathPosition` using `MILLIMETER_3D` unit"}

~~~~xml
<PathPosition>10.0 0.0 20.0</PathPosition>
~~~~
{: caption="XML Streams Response Example for `PathPosition` using `MILLIMETER_3D` unit"}


~~~~xml
<DataItem type='PATH_POSITION' id='pathposit1' representation="DATA_SET">
  <Definition>
    <EntryDefinition key='X' units='MILLIMETER'>
    <EntryDefinition key='Y' units='MILLIMETER'>
    <EntryDefinition key='Z' units='MILLIMETER'>
  </Definition>
</DataItem>
~~~~
{: caption="XML Device Model Example for `PathPosition` to demonstrate multi-dimensional representation using `DataSet` representation"}

~~~~xml
<PathPositionDataSet id='pathposit1'>
  <Entry key='X'>10.0</Entry>
  <Entry key='Z'>20.0</Entry>
</PathPositionDataSet>
~~~~
{: caption="XML Streams Response Example for `PathPosition` to demonstrate multi-dimensional representation using `DataSet` representation"}&#10;

"""


class PathPositionClass(SampleClass):


    def __init__(self):


        # TODO: Import UnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Units = "MILLIMETER_3D"

        # TODO: Import SampleEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Type = "PATH_POSITION"

        # TODO: Import float[] and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Result = ""



