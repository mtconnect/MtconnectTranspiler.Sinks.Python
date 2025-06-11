# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{term(asset)}} that is used by the manufacturing process to perform tasks.

> Note 1 to entry: An {{term(Asset)}} relies upon an {{term(Device)}} to provide {{termplural(observation)}} and information about itself and the {{term(Device)}} revises the information to reflect changes to the {{term(Asset)}} during their interaction. Examples of {{termplural(Asset)}} are cutting tools, Part Information, Manufacturing Processes, Fixtures, and Files.

> Note 2 to entry: A singular {{property(Asset::assetId)}} uniquely identifies an {{term(Asset)}} throughout its lifecycle and is used to track and relate the {{term(Asset)}} to other {{termplural(Device)}} and entities.

> Note 3 to entry: {{termplural(Asset)}} are temporally associated with a device and can be removed from the device without damage or alteration to its primary functions.

&#10;

"""


class AssetGeneralization(AssetClass):


    def __init__(self):


        # TODO: Import DeviceClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.BelongsTo = ""



