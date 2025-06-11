using CaseExtensions;
using MtconnectTranspiler.CodeGenerators.ScribanTemplates;
using MtconnectTranspiler.Sinks.Python.Example;
using MtconnectTranspiler.Xmi;
using MtconnectTranspiler.Xmi.UML;

namespace MtconnectTranspiler.Sinks.Python.Models
{
    /// <summary>
    /// Represents a Python class
    /// </summary>
    [ScribanTemplate("Python.Class.scriban")]
    public partial class PythonClass : PythonType, IFileSource
    {
        /// <summary>
        /// Reference to the xmi:id
        /// </summary>
        public string? ReferenceId { get; set; }

        /// <summary>
        /// Reference to the <c>name</c> attribute.
        /// </summary>
        public string? NormativeName { get; set; }

        /// <summary>
        /// Reference to any Comments written in the SysML model to be converted into a Python format <c>&lt;summary /&gt;</c>
        /// </summary>
        public Summary? Summary { get; protected set; }

        /// <summary>
        /// Internal reference to the class filename.
        /// </summary>
        protected string? _filename { get; set; }
        /// <inheritdoc />
        public virtual string Filename
        {
            get
            {
                if (string.IsNullOrEmpty(_filename))
                    _filename = $"{CategoryFunctions.ToPathSafe(Namespace.Substring(Namespace.LastIndexOf(".")+1))}/{CategoryFunctions.ToPathSafe(Name.ToPascalCase())}.py";
                return _filename;
            }
            set { _filename = value; }
        }

        /// <summary>
        /// Internal list of <see cref="Property"/>, used by <see cref="Properties"/>.
        /// </summary>
        protected List<Property> _properties = new List<Property>();
        /// <summary>
        /// Collection of <inheritdoc cref="Property"/>
        /// </summary>
        public IEnumerable<Property> Properties => _properties;

        /// <summary>
        /// Internal list of <see cref="Constraint"/>, used by <see cref="Constraints"/>.
        /// </summary>
        protected List<Constraint> _constraints = new List<Constraint>();
        /// <summary>
        /// Collection of <inheritdoc cref="Constraint"/>
        /// </summary>
        public IEnumerable<Constraint> Constraints => _constraints;

        /// <summary>
        /// Remote type of the generalization
        /// </summary>
        public string? Generalization { get; set; }

        /// <summary>
        /// Original <c>generalization</c> value from the XMI
        /// </summary>
        public string? GeneralizationId { get; set; }

        private XmiElement? _remoteType { get; set; }

        /// <summary>
        /// Constructs an <see cref="PythonClass"/> more generically. <b>NOTE</b>: You'll need to add items manually from here.
        /// </summary>
        /// <param name="model"><inheritdoc cref="XmiDocument" path="/summary"/></param>
        /// <param name="source"><inheritdoc cref="XmiElement" path="/summary"/></param>
        public PythonClass(XmiDocument model, UmlClass source) : base(model, source)
        {
            ReferenceId = source.Id;

            if (source.Comments?.Length > 0)
                Summary = new Summary(source.Comments);

            if (source.IsAbstract)
                Modifier = "abstract";

            AccessModifier = "public";

            _properties = source.Properties
                ?.Where(o => !string.IsNullOrEmpty(o.Name))
                ?.Select(o => new Property(model, o))
                ?.ToList()
                ?? new List<Property>();

            var propertyGroupings = _properties.GroupBy(o => o.Name);
            foreach (var propertyGrouping in propertyGroupings)
            {
                if (propertyGrouping.Count() <= 1)
                    continue;
                var properties = _properties.Where(o => o.Name == propertyGrouping.Key).ToList();
                foreach (var property in properties)
                {
                    if (property.Type.EndsWith("Class"))
                    {
                        string remoteClassName = property.Type.Replace("Class", string.Empty);
                        if (!property.Name.EndsWith(remoteClassName))
                        {
                            property.Name += remoteClassName;
                        }
                    }
                }
            }

            _constraints = source.Constraints
                ?.Where(o => !string.IsNullOrEmpty(o.Name))
                ?.Select(o => new Constraint(model, o))
                ?.ToList()
                ?? new List<Constraint>();

            GeneralizationId = source.Generalization?.Name ?? source.Generalization?.General;
            if (!string.IsNullOrEmpty(GeneralizationId))
            {
                XmiElement? remoteType = null;
                Generalization = PythonHelperMethods.ToPrimitiveType(GeneralizationId)?.Name
                    ?? PythonHelperMethods.TypeDeepSearch(model, GeneralizationId, out remoteType)
                    ?? "";
            }

            Name = GetClassName(model, source);
            NormativeName = source.Name;
        }

        /// <summary>
        /// Adds a new <see cref="Property"/>
        /// </summary>
        /// <param name="property">Reference to the source <see cref="Property"/> to add</param>
        public void Add(Property property)
            => _properties.Add(property);

        public static string GetClassName(XmiDocument model, UmlClass umlClass)
        {
            string name = PythonHelperMethods.ToPascalCase(umlClass.Name);
            
            string? generalization = umlClass.Generalization?.Name ?? umlClass.Generalization?.Id;
            if (!string.IsNullOrEmpty(generalization))
            {
                string? generalizedType = PythonHelperMethods.TypeDeepSearch(model, generalization, out XmiElement? remoteType);
                if (!string.IsNullOrEmpty(generalizedType) && generalizedType.EndsWith("Class"))
                {
                    string remoteGeneralization = generalizedType.Replace("Class", string.Empty);
                    if (name.EndsWith(remoteGeneralization, StringComparison.OrdinalIgnoreCase))
                    {
                        name += "Generalization";
                    }
                    else
                    {
                        name += "Class";
                    }
                }
                else
                {
                    name += "Class";
                }
            } else
            {
                name += "Class";
            }
            return name;
        }

    }
}
