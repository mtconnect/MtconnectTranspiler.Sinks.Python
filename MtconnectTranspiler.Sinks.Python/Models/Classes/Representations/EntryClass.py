# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{term(key-value pair)}} published as part of a {{block(DataSet)}}.&#10;
&#10;&#10;&#10;Constraints for Entry Values&#10;&#10;&#10;&#10;
The value of each {{block(Entry)}} **MUST** have the same restrictions as the value of an {{term(observation)}} with {{property(DataItem::representation)}} as `VALUE`.

An {{block(Entry)}} **MAY** be further constrained by the {{block(DataItem)}} definition (see {{package(Device Information Model)}}), for example a `VariableDataSet` having a string value **MAY** have a floating-point {{block(Temperature)}} value. A restriction **MUST NOT** be broadened or removed, for example, the value "READY" **MUST NOT** occur with a `TemperatureDataSet` constrained to floating-point numbers.

{{block(EntryDefinition)}} **MAY** provide the type and units of an {{property(Entry::key)}}.
&#10;

"""


class EntryClass:


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for each {{term(key-value pair)}}.&#10;

        """

        self.Key = ""

        # TODO: Import Boolean and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;removal indicator of a {{term(key-value pair)}}.&#10;

        """

        self.Removed = ""

        # TODO: Import DataSetClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.IsEntryFor = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;value of the {{block(Entry)}}.&#10;

        """

        self.Result = ""



