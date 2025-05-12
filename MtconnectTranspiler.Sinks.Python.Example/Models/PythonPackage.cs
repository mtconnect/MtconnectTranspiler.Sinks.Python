using CaseExtensions;
using MtconnectTranspiler.CodeGenerators.ScribanTemplates;
using MtconnectTranspiler.Sinks.Python.Models;
using MtconnectTranspiler.Xmi;
using MtconnectTranspiler.Xmi.UML;
using System.Data;

namespace MtconnectTranspiler.Sinks.Python.Example.Models
{
    [ScribanTemplate("Python.Package.scriban")]
    public class PythonPackage : PythonType, IFileSource
    {
        /// <summary>
        /// Reference to the xmi:id
        /// </summary>
        public string ReferenceId { get; set; }

        /// <summary>
        /// Reference to the <c>name</c> attribute.
        /// </summary>
        public string NormativeName { get; set; }

        /// <summary>
        /// Internal reference to the class filename.
        /// </summary>
        protected string _filename { get; set; }
        /// <inheritdoc />
        public string Filename
        {
            get
            {
                if (string.IsNullOrEmpty(_filename))
                    _filename = $"{CategoryFunctions.ToPathSafe(Namespace.Substring(Namespace.LastIndexOf(".") + 1))}/{CategoryFunctions.ToPathSafe(Name.ToPascalCase())}.py";
                return _filename;
            }
            set { _filename = value; }
        }

        /// <summary>
        /// Internal list of <see cref="PythonPackage"/>, used by <see cref="Packages"/>.
        /// </summary>
        protected List<PythonPackage> _packages = new List<PythonPackage>();
        /// <summary>
        /// Collection of <inheritdoc cref="PythonPackage"/>
        /// </summary>
        public new IEnumerable<PythonPackage> Packages => _packages;

        /// <summary>
        /// Internal list of <see cref="PythonClass"/>, used by <see cref="Classes"/>.
        /// </summary>
        protected List<PythonClass> _classes = new List<PythonClass>();
        /// <summary>
        /// Collection of <inheritdoc cref="PythonClass"/>
        /// </summary>
        public new IEnumerable<PythonClass> Classes => _classes;

        /// <summary>
        /// Internal list of <see cref="PythonEnum"/>, used by <see cref="Enums"/>.
        /// </summary>
        protected List<PythonEnum> _enums = new List<PythonEnum>();
        /// <summary>
        /// Collection of <inheritdoc cref="PythonEnum"/>
        /// </summary>
        public IEnumerable<PythonEnum> Enums => _enums;

        /// <summary>
        /// Reference to any Comments written in the SysML model to be converted into a Python format <c>&lt;summary /&gt;</c>
        /// </summary>
        public Summary Summary { get; protected set; }

        public PythonPackage(XmiDocument model, UmlPackage source) : base(model, source)
        {
            _name = PythonHelperMethods.ToPascalCase(source.Name);
            NormativeName = source.Name;

            ReferenceId = source!.Id;

            if (source.Comments?.Length > 0)
                Summary = new Summary(source.Comments);

            _packages = source!.Packages
                ?.Select(o => new PythonPackage(model, o))
                ?.ToList()
                ?? new List<PythonPackage>();

            _classes = source!.Classes
                ?.Select(o => new PythonClass(model, o))
                ?.ToList()
                ?? new List<PythonClass>();

            _enums = source!.Enumerations
                ?.Select(o => new PythonEnum(model, o))
                ?.ToList()
                ?? new List<PythonEnum>();
        }
    }
}
