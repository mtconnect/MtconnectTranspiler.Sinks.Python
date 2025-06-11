# Auto-generated Python class from MtconnectTranspiler.Sinks.Python.Example/Templates/Python.Class.Scriban template #

# NOTE: This is the SysML markdown summary

"""
&#10;&#10;&#10;abstract {{block(Component)}} composed of a motion system that provides linear or rotational motion for a piece of equipment.&#10;
&#10;&#10;&#10;Description&#10;&#10;&#10;&#10;In robotics, the term *Axis* is synonymous with *Joint*. A *Joint* is the connection between two parts of the structure that move in relation to each other.

{{block(Linear)}} and {{block(Rotary)}} components **MUST** have {{property(Component::name)}} that **MUST** follow the conventions described below. Use the {{property(Component::nativeName)}} for the manufacturer's name of the axis if it differs from the assigned {{property(Component::name)}}.

MTConnect has two high-level classes for automation equipment as follows: (1) Equipment that controls cartesian coordinate axes and (2) Equipment that controls articulated axes. There are ambiguous cases where some machines exhibit both characteristics; when this occurs, the primary control system's configuration determines the classification.

Examples of cartesian coordinate equipment are CNC Machine Tools, Coordinate measurement machines, as specified in ISO 841, and 3D Printers. Examples of articulated automation equipment are Robotic systems as specified in ISO 8373.

The following sections define the designation of names for the axes and additional guidance when selecting the correct scheme to use for a given piece of equipment.

#### Cartesian Coordinate Naming Conventions

A Three-Dimensional Cartesian Coordinate control system organizes its axes orthogonally relative to a machine coordinate system where the manufacturer of the equipment specifies the origin. 

{{block(Axes)}} {{property(Component::name)}} **SHOULD** comply with ISO 841, if possible.

##### Linear Motion

A piece of equipment **MUST** represent prismatic motion using a {{block(Linear)}} axis and assign its {{property(Component::name)}} using the designations `X`, `Y`, and `Z`. A {{block(Linear)}} axis {{property(Component::name)}} **MUST** append a monotonically increasing suffix when there are more than one parallel axes; for example, `X2`, `X3`, and `X4`. 

##### Rotary Motion

MTConnect **MUST** assign the {{property(Component::name)}} to {{block(Rotary)}} axes exhibiting rotary motion using `A`, `B`, and `C`. A {{block(Rotary)}} axis {{property(Component::name)}} **MUST** append a monotonically increasing suffix when more than one {{block(Rotary)}} axis rotates around the same {{block(Linear)}} axis; for example, `A2`, `A3`, and `A4`. 

#### Articulated Machine Control Systems

An articulated control system's axes represent the connecting linkages between two adjacent rigid members of an assembly. The {{block(Linear)}} axis represents prismatic motion, and the {{block(Rotary)}} axis represents the rotational motion of the two related members. The control organizes the axes in a kinematic chain from the mounting surface (base) to the end-effector or tooling.

#### Articulated Machine Axis Names

The axes of articulated machines represent forward kinematic relationships between mechanical linkages. Each axis is a connection between linkages, also referred to as joints, and **MUST** be named using a `J` followed by a monotonically increasing number; for example, `J1`, `J2`, `J3`.  The numbering starts at the base axis connected or closest to the mounting surface, `J1`, incrementing to the mechanical interface, `Jn`, where `n` is the number of the last axis. The chain forms a parent-child relationship with the parent being the axis closest to the base.

A machine having an axis with more than one child **MUST** number each branch using its numeric designation followed by a branch number and a monotonically increasing number. For example, if `J2` has two children, the first child branch **MUST** be named `J2.1.1` and the second child branch `J2.2.1`. A child of the first branch **MUST** be named `J2.1.2`, incrementing to `J2.1.n`, where `J2.1.n` is the number of the last axis in that branch.&#10;

"""


class AxisClass(ComponentGeneralization):


    def __init__(self):


        # TODO: Import DeviceClass and initialize here

        # NOTE: This is the SysML markdown summary
        """
        
        """

        self.IsAxisOf = ""



