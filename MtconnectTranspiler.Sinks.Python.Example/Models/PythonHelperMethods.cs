using System.Collections.Generic;
using System;
using MtconnectTranspiler.Xmi.UML;
using MtconnectTranspiler.Contracts;
using MtconnectTranspiler.CodeGenerators.ScribanTemplates;

namespace MtconnectTranspiler.Sinks.Python.Models
{
    /// <summary>
    /// Helper methods to process content for scriban templates
    /// </summary>
    public class PythonHelperMethods : ScribanHelperMethods
    {
        private static Dictionary<string, Type> umlDataTypeToPython = new Dictionary<string, Type>()
        {
            { "boolean", typeof(bool) },
            { "ID", typeof(string) },
            { "string", typeof(string) },
            { "float", typeof(float) },
            { "datetime", typeof(DateTime) },
            { "integer", typeof(int) },
            { "xlinktype", typeof(string) },
            { "xslang", typeof(string) },
            { "SECOND", typeof(float) },
            { "IDREF", typeof(string) },
            { "xlinkhref", typeof(string) },
            { "MILLIMETER", typeof(float) },
            { "DEGREE", typeof(float) },
            { "x509", typeof(string) },
            { "CUBIC_MILLIMETER", typeof(float) },
            { "int32", typeof(int) },
            { "int64", typeof(long) },
            { "version", typeof(string) },
            { "uint32", typeof(uint) },
            { "uint64", typeof(ulong) },
            { "double", typeof(double) },
            
        };
        public static Type? ToPrimitiveType(string umlType)
        {
            if (umlDataTypeToPython.TryGetValue(umlType, out var type))
                return type;
            return null;
        }

        /// <summary>
        /// Gets the Python equivalant of the <see cref="UmlDataType"/>.
        /// </summary>
        /// <param name="source">Reference to the packaged UML DataType</param>
        /// <returns>Primitive type. Returns null if unrecognizes or unhandled DataType</returns>
        public static Type? ToPrimitiveType(UmlDataType source)
            => ToPrimitiveType(source.Name);

        /// <summary>
        /// Gets the Python equivalant of the <see cref="UmlProperty"/>.
        /// </summary>
        /// <param name="model">Reference to the source XMI document</param>
        /// <param name="source">Reference to the packaged UML Property</param>
        /// <returns>Primitive type. Returns null if unrecognizes or unhandled Property</returns>
        public static Type? ToPrimitiveType(Xmi.XmiDocument model, UmlProperty source)
        {
            var umlDataType = model.LookupDataType(source.PropertyType);
            if (umlDataType == null)
                return null;
            return ToPrimitiveType(umlDataType);
        }


        public static string? TypeDeepSearch(Xmi.XmiDocument model, string propertyType, out Xmi.XmiElement? remoteType)
        {
            remoteType = null;
            if (string.IsNullOrEmpty(propertyType))
                return null;
            // TODO: Also cache the namespaces that each of these properties are contained within
            object _remote;
            if (model.IdCache.TryGetValue(propertyType, out _remote))
            {
                switch (_remote)
                {
                    case UmlEnumeration umlEnum:
                        remoteType = umlEnum;
                        return $"{umlEnum.Name}MetaClass";
                    case UmlClass umlClass:
                        remoteType = umlClass;
                        return PythonClass.GetClassName(model, umlClass);// $"{umlClass.Name}Class";
                    case UmlDataType umlDataType:
                        remoteType = umlDataType;
                        switch (umlDataType.Name)
                        {
                            case "float3d":
                                return "float[]";
                            case "binary":
                                return "bool";
                            default:
                                break;
                        }
                        break;
                    case UmlAssociation umlAssociation:
                        remoteType = umlAssociation;
                        var ownedEnds = umlAssociation.OwnedEnds?.Select(o => TypeDeepSearch(model, o.TypeId, out _))?.ToList();
                        return umlAssociation.Name;
                    case UmlGeneralization umlGeneralization:
                        return TypeDeepSearch(model, umlGeneralization.General, out remoteType);
                    case UmlEnumerationLiteral umlEnumerationLiteral:
                        return umlEnumerationLiteral.Name;
                    default:
                        break;
                }
            }
            return null;
        }
    }
}
