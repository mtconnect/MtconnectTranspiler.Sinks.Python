# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;references to a file with the three-dimensional geometry of the {{block(Component)}} or {{block(Composition)}}.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;The geometry **MAY** have a transformation and a scale to position the {{block(Component)}} with respect to the other {{block(Component)}}s. A geometry file can contain a set of assembled items, in this case, the {{block(SolidModel)}} references the {{property(SolidModel::id)}} of the assembly model file and the specific item within that file.

The {{block(SolidModel)}} **MAY** provide a translation, rotation, and scale to correctly place it relative to the other geometries in the machine. If the {{block(Component)}} can move and has a {{block(Motion)}} {{block(Configuration)}}, the {{block(SolidModel)}} will move when the {{block(Component)}} or {{block(Composition)}} moves.

Either an {{property(SolidModel::href)}} or a {{property(SolidModel::modelIdRef)}} and an {{property(SolidModel::itemRef)}} **MUST** be specified.&#10;

"""


class SolidModelClass:


    def __init__(self):


        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;unique identifier for this element.&#10;

        """

        self.Id = ""

        # TODO: Import TransformationClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasTransformation = ""

        # TODO: Import ScaleClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.HasScale = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;associated model file if an item reference is used.&#10;

        """

        self.SolidModelIdRef = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;{{term(URL)}} giving the location of the {{block(SolidModel)}}. 
        
        If not present, the model referenced in the {{property(SolidModel::solidModelIdRef)}} is used.
        
        {{property(SolidModel::href)}} is of type `xlink:href` from the W3C XLink specification.&#10;

        """

        self.Href = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;reference to the item within the model within the related geometry. A {{property(SolidModel::solidModelIdRef)}} **MUST** be given. 
        
        > Note: `Item` defined in ASME Y14.100 - A nonspecific term used to denote any unit or product, including materials, parts, assemblies, equipment, accessories, and computer software.&#10;

        """

        self.ItemRef = ""

        # TODO: Import MediaTypeEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;format of the referenced document.&#10;

        """

        self.MediaType = ""

        # TODO: Import String and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;reference to the coordinate system for this {{block(SolidModel)}}.&#10;

        """

        self.CoordinateSystemIdRef = ""

        # TODO: Import NativeUnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;same as {{property(DataItem::nativeUnits)}}. See {{sect(DataItem)}}.&#10;

        """

        self.NativeUnits = ""

        # TODO: Import UnitEnumMetaClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        &#10;&#10;&#10;same as {{property(DataItem::units)}}. See {{sect(DataItem)}}.&#10;

        """

        self.Units = ""



