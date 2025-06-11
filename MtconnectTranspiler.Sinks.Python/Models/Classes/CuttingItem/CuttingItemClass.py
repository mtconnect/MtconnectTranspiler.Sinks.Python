# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;part of of the tool that physically removes the material from the workpiece by shear deformation.&#10;

"""


class CuttingItemClass:


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;free-form description of the cutting item.&#10;

        """

        self.Description = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;material composition for this cutting item.&#10;

        """

        self.Grade = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;number or numbers representing the individual cutting item or items on the tool.
        
        Indices **SHOULD** start numbering with the inserts or {{block(CuttingItem)}} furthest from the gauge line and increasing in value as the items get closer to the gauge line. Items at the same distance **MAY** be arbitrarily numbered.
        
        > Note: In {{term(XML)}}, the representation **MUST** be a single number ("1") or a comma separated set of individual elements ("1,2,3,4"), or as a inclusive range of values as in ("1-10") or any combination of ranges and numbers as in "1-4,6-10,22". There **MUST NOT** be spaces or non-integer values in the text representation.&#10;

        """

        self.Indices = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;manufacturer identifier of this cutting item.&#10;

        """

        self.ItemId = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;free form description of the location on the cutting tool.
        
        For clarity, the words `FLUTE`, `INSERT`, and `CARTRIDGE` **SHOULD** be used to assist in noting the location of a {{block(CuttingItem)}}. {{property(CuttingItem::Locus)}} **MAY** be any free form string, but **SHOULD** adhere to the following rules:
        
        * The location numbering **SHOULD** start at the furthest {{block(CuttingItem)}} and work it’s way back to the {{block(CuttingItem)}} closest to the gauge line.
        
        * Flutes **SHOULD** be identified as such using the word `FLUTE`:. For example: `FLUTE`: 1, `INSERT`: 2 - would indicate the first flute and the second furthest insert from the end of the tool on that flute.
        
        * Other designations such as `CARTRIDGE` **MAY** be included, but should be identified using upper case and followed by a colon (:).&#10;

        """

        self.Locus = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;manufacturers of the cutting item.
        
        This will reference the tool item and adaptive items specifically. The cutting items
        manufacturers’ will be a property of {{block(CuttingItem)}}.
        
        > Note: In {{term(XML)}}, the representation **MUST** be a comma(,) delimited list of manufacturer names. See {{sect(CuttingItem Schema Diagrams)}}.&#10;

        """

        self.Manufacturers = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;tool group this item is assigned in the part program.&#10;

        """

        self.ProgramToolGroup = ""

        # TODO: Import StatusClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasCutterStatus = ""

        # TODO: Import ItemLifeClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;The tool life measured in tool wear.&#10;

        """

        self.HasItemLife = ""

        # TODO: Import MeasurementClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;A collection of measurements relating to this cutting item.&#10;

        """

        self.HasMeasurement = ""



