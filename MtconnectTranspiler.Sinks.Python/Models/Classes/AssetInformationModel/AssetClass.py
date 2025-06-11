# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;abstract {{term(Asset)}}. &#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;It is used in the manufacturing process, but is not permanently associated with a single piece of equipment. It can be removed from the piece of equipment without compromising its function, and can be associated with other pieces of equipment during its lifecycle.


![Asset](figures/Asset.png "Asset"){: width="0.8"}

> Note: See {{sect(Assets Schema Diagrams)}} for XML schema.&#10;

"""


class AssetClass(AssetGeneralization):


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for an {{block(Asset)}}.&#10;

        """

        self.AssetId = ""

        # TODO: Import object and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;associated piece of equipment's {{term(UUID)}} that supplied the {{block(Asset)}}'s data.
        
        It references to {{property(Device::uuid)}} defined in {{package(Device Information Model)}}.&#10;

        """

        self.DeviceUuid = ""

        # TODO: Import Boolean and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;indicator that the {{block(Asset)}} has been removed from the piece of equipment.&#10;

        """

        self.Removed = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;time the {{block(Asset)}} data was last modified.&#10;

        """

        self.Timestamp = ""

        # TODO: Import DescriptionClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;Description can contain any descriptive content about the Asset.&#10;

        """

        self.HasDescription = ""

        # TODO: Import ConfigurationClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasConfiguration = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;condensed message digest from a secure one-way hash function. {{cite(FIPS PUB 180-4)}}&#10;

        """

        self.Hash = ""



