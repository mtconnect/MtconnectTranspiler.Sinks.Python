# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(AbstractFile)}} type that provides information about the {{block(File)}} instance and its {{term(URL)}}.&#10;

"""


class FileClass(AbstractFileClass):


    def __init__(self):


        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;size of the file in bytes.&#10;

        """

        self.Size = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;version identifier of the file.&#10;

        """

        self.VersionId = ""

        # TODO: Import FileStateEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;state of the file. &#10;

        """

        self.State = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;secure hash of the file.&#10;

        """

        self.Signature = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;public key used to verify the signature.&#10;

        """

        self.PublicKey = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;time the file was created.&#10;

        """

        self.CreationTime = ""

        # TODO: Import DateTime and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;time the file was modified.&#10;

        """

        self.ModificationTime = ""

        # TODO: Import FileLocationClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasLocation = ""

        # TODO: Import DestinationClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasDestination = ""



