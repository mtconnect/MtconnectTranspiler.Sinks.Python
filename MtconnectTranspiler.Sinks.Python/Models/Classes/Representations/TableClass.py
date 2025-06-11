# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Representation)}} for an {{block(Observation)}} composed of two-dimensional sets of {{termplural(key-value pair)}} where the {{block(Entry)}} represents rows containing sets of {{termplural(key-value pair)}} given by {{block(Cell)}} entities. 
&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;{{block(Table)}} for an {{block(Observation)}} is defined by the associated {{property(DataItem::representation)}} as `TABLE`.

{{property(DataItem::representation)}} as `TABLE` **MUST** have {{property(DataItem::category)}} as `SAMPLE` or `EVENT`.

{{figure(WorkOffsetTable)}} shows the model for {{block(WorkOffset)}} ({{block(Event)}} type) with a {{block(Representation)}} type of {{block(Table)}}. 

![WorkOffsetTable](figures/WorkOffsetTable.png "WorkOffsetTable"){: width="0.8"}

> Note: See {{sect(Representation Schema Diagrams)}} for XML schema.

{{block(Table)}} has the same behavior as the {{block(DataSet)}} for change tracking, clearing, and history. When an {{block(Entry)}} changes, all {{block(Cell)}} entities update at the same time; they are not tracked separately like {{block(Entry)}}.

The meaning of each {{block(Entry)}} and {{block(Cell)}} **MAY** be provided as the {{block(DataItem)}} {{block(EntryDefinition)}} and {{block(CellDefinition)}}.

{{property(Entry::key)}}  **MUST** be the unique identity of the {{block(Entry)}} within an {{block(Observation)}}. {{property(Cell::key)}} **MUST** be the unique identity of the {{block(Cell)}} within an {{block(Entry)}}.

{{figure(Table Example)}} shows {{block(Event)}} {{block(Observation)}} type {{block(WorkOffset)}} with a {{block(Representation)}} type of `Table`.

![Table Example](figures/Table%20Example.png "Table Example"){: width="0.8"}

> Note: See {{lst(table-example)}} for the {{term(XML)}} representation of the same example.

&#10;

"""


class TableClass(RepresentationClass):


    def __init__(self):


        # TODO: Import TableEntryClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.Result = ""

        # TODO: Import Int32 and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;number of {{termplural(key-value pair)}} represented as {{block(Entry)}} entities.&#10;

        """

        self.Count = ""



