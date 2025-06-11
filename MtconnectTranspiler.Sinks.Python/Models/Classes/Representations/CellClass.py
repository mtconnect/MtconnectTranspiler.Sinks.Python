# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{term(key-value pair)}} published as part of a {{block(TableEntry)}}.&#10;
&#10;&#10;&#10;Constraints for Cell Values&#10;&#10;&#10;&#10;#### Constraints for Cell Values

The value of each {{block(Cell)}} **MUST** have the same restrictions as the value of an {{term(observation)}} with {{property(DataItem::representation)}} as `VALUE`.

An {{block(Cell)}} **MAY** be further constrained by the {{block(DataItem)}} definition (see {{package(Device Information Model)}}), for example a `VariableDataSet` having a string value **MAY** have a floating-point {{block(Temperature)}} value. A restriction **MUST NOT** be broadened or removed, for example, the value `READY` **MUST NOT** occur with a `TemperatureDataSet` constrained limited to floating-point numbers.

{{block(CellDefinition)}} **MAY** provide type and units of a {{property(Cell::key)}}.&#10;

"""


class CellClass:


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for each {{term(key-value pair)}}.&#10;

        """

        self.Key = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;value of the {{block(Cell)}}.&#10;

        """

        self.Result = ""



