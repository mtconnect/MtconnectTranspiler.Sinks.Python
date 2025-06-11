# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;{{block(Component)}} composed of a mechanical mechanism or closure that can cover a physical access portal into a piece of equipment allowing or restricting access to other parts of the equipment.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;The closure can be opened or closed to allow or restrict access to other parts of the equipment.

{{block(Door)}} **MUST** have {{block(DoorState)}} data item to indicate if the door is `OPEN`, `CLOSED`, or `UNLATCHED`. A {{block(Component)}} **MAY** contain multiple {{block(Door)}} entities.&#10;

"""


class DoorClass(ComponentGeneralization):


    def __init__(self):


        # TODO: Import DoorStateClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.ObservesDoorState = ""



