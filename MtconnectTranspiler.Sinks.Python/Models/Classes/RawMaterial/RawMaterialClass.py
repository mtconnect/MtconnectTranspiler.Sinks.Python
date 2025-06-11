# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Asset)}} that represents {{term(raw material)}}.&#10;

"""


class RawMaterialClass(AssetClass):


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;name of the {{term(raw material)}}.
        
        Examples: `Container1` and `AcrylicContainer`.&#10;

        """

        self.Name = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;type of container holding the {{term(raw material)}}. 
        
        Examples: `Pallet`, `Canister`, `Cartridge`, `Tank`, `Bin`, `Roll`, and `Spool`.&#10;

        """

        self.ContainerType = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;ISO process type supported by this {{term(raw material)}}. 
        
        Examples include: `VAT_POLYMERIZATION`, `BINDER_JETTING`, `MATERIAL_EXTRUSION`, `MATERIAL_JETTING`, `SHEET_LAMINATION`, `POWDER_BED_FUSION` and `DIRECTED_ENERGY_DEPOSITION`.&#10;

        """

        self.ProcessKind = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;serial number of the {{term(raw material)}}.&#10;

        """

        self.SerialNumber = ""

        # TODO: Import Boolean and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{block(Material)}} has existing usable volume.&#10;

        """

        self.HasMaterial = ""

        # TODO: Import MaterialClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasMaterial = ""

        # TODO: Import FormEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;form of the {{term(raw material)}}.&#10;

        """

        self.Form = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;date the {{term(raw material)}} was created.&#10;

        """

        self.ManufacturingDate = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;date {{term(raw material)}} was first used.&#10;

        """

        self.FirstUseDate = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;date {{term(raw material)}} was last used.&#10;

        """

        self.LastUseDate = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;amount of material initially placed in {{term(raw material)}} when manufactured.&#10;

        """

        self.InitialVolume = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;dimension of material initially placed in {{term(raw material)}} when manufactured.&#10;

        """

        self.InitialDimension = ""

        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;quantity of material initially placed in {{term(raw material)}} when manufactured.&#10;

        """

        self.InitialQuantity = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;amount of material currently in {{term(raw material)}}.&#10;

        """

        self.CurrentVolume = ""

        # TODO: Import Single and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;dimension of material currently in {{term(raw material)}}.&#10;

        """

        self.CurrentDimension = ""

        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;quantity of material currently in {{term(raw material)}}.&#10;

        """

        self.CurrentQuantity = ""



