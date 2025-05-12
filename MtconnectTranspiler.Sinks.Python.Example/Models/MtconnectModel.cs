using MtconnectTranspiler.Sinks.Python.Models;
using MtconnectTranspiler.Xmi.UML;
using MtconnectTranspiler.Xmi;
using MtconnectTranspiler.CodeGenerators.ScribanTemplates;

namespace MtconnectTranspiler.Sinks.Python.Example.Models
{
    [ScribanTemplate("Python.Model.scriban")]
    public class MtconnectModel : PythonType, IFileSource
    {
        /// <summary>
        /// Reference to the xmi:id
        /// </summary>
        public string ReferenceId { get; set; }

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
                    _filename = $"MtconnectModel.cs";
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
        public IEnumerable<PythonPackage> Packages => _packages;

        public MtconnectModel(XmiDocument model, UmlModel source) : base(model, source)
        {
            _name = PythonHelperMethods.ToPascalCase(source.Name);

            ReferenceId = source!.Id;

            _packages = source!.Packages
                ?.Select(o => new PythonPackage(model, o))
                ?.ToList()
                ?? new List<PythonPackage>();
            foreach(var profile in source!.Profiles)
            {
                foreach (var package in profile.Packages)
                {
                    _packages.Add(new PythonPackage(model, package));
                }
            }
        }
    }
}
