using Microsoft.Extensions.Logging;
using MtconnectTranspiler.Sinks.Python.Models;
using MtconnectTranspiler.Sinks.Python.Example.Models;
using MtconnectTranspiler.Xmi.UML;
using Scriban.Runtime;
using MtconnectTranspiler.Xmi;
using MtconnectTranspiler.Contracts;
using System.Linq;
using CaseExtensions;
using System.Text.RegularExpressions;
using MtconnectTranspiler.CodeGenerators.ScribanTemplates;

namespace MtconnectTranspiler.Sinks.Python.Example
{
    public class CategoryFunctions : ScriptObject
    {
        public static bool CategoryContainsType(PythonEnum @enum, EnumItem item) => @enum.SubTypes.ContainsKey(item.Name);
        public static bool CategoryContainsValue(PythonEnum @enum, EnumItem item) => @enum.ValueTypes.ContainsKey(item.Name);
        public static bool EnumHasValues(PythonEnum @enum) => @enum.ValueTypes.Any();
        public static string ToCodeSafe(string input, string replaceBy = "_")
        {
            if (string.IsNullOrEmpty(input))
                return input;
            if (input.Contains("^2"))
                input = input.Replace("^2", "_SQUARED");
            if (input.Contains("^3"))
                input = input.Replace("^3", "_CUBED");
            if (input.Contains("/"))
                input = input.Replace("/", "_PER_");
            if (input.Equals("float[]", StringComparison.OrdinalIgnoreCase))
                return input;
            if (input.Equals("float[3]", StringComparison.OrdinalIgnoreCase))
                return input;
            char[] numbers = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
            if (numbers.Any(c => input.StartsWith(c)))
                input = $"_{input}";

            var invlidFileCharacters = System.IO.Path
            .GetInvalidFileNameChars()
            .Concat(new char[] { ' ', '{', '}', '[', ']', '(', ')', '^', '`', '&', '+', '-', '!', '?', '%', '*', '<', '>', ',', '|', '\\', '/', '=', ':', ';' })
            .ToArray();
            /// <summary>
            /// Regular expression to replace the <see cref="InvalidCharacters"/>
            /// </summary>
            var regex = new Regex(@"\" + String.Join(@"|\", invlidFileCharacters), RegexOptions.Compiled);
            return regex.Replace(input, replaceBy);
        }
        public static string ToPathSafe(string input, string replaceBy = "_")
        {
            if (string.IsNullOrEmpty(input))
                return input;
            var invalidFileCharacters = System.IO.Path
                .GetInvalidFileNameChars()
                .ToArray();
            var regex = new Regex(@"\" + String.Join(@"|\", invalidFileCharacters), RegexOptions.Compiled);
            return regex.Replace(input, replaceBy);
        }
        public static string? GetTypeNamespace(string referenceId)
            => TypeCache.GetTypeNamespaceFromId(referenceId);
        public static string[] GetClassNamespaces(PythonClass cSharpClass)
        {
            var result = new List<string>();
            foreach (var property in cSharpClass.Properties)
            {
                string[] namespaces = TypeCache.GetTypeNamespaceFromName(property.Type);
                if (namespaces?.Length > 0)
                {
                    result.AddRange(namespaces);
                } else
                {
                    System.Diagnostics.Debug.WriteLine("Missing namespace for '" + property.Type + "'");
                }
            }
            return result.Distinct().Where(o => !string.IsNullOrEmpty(o)).ToArray();
        }
        public static string[] GetPackageNamespaces(PythonPackage pythonPackage)
        {
            var namespaces = new List<string>();
            foreach (var pythonClass in pythonPackage.Classes)
            {
                namespaces.Add(pythonClass.Namespace);
            }
            return namespaces.Distinct().Where(o => !string.IsNullOrEmpty(o)).ToArray();
        }
    }
    internal class Transpiler : ITranspilerSink
    {
        private readonly ILogger<ITranspilerSink>? _logger;

        private readonly IScribanTemplateGenerator _generator;

        /// <summary>
        /// 
        /// </summary>
        /// <param name="projectPath"></param>
        public Transpiler(IScribanTemplateGenerator generator, ILogger<ITranspilerSink>? logger = default)
        {
            _logger = logger;

            _generator = generator;
        }

        public void Transpile(XmiDocument model, CancellationToken cancellationToken = default)
        {
            _logger?.LogInformation("Received MTConnectModel, beginning transpilation");

            _generator.Model.SetValue("model", model, true);

            _generator.TemplateContext.PushGlobal(new CategoryFunctions());

            //// Process the template into enum files
            var allPackages = new List<PythonPackage>();
            var allClasses = new List<PythonClass>();
            var allEnumerations = new List<PythonEnum>();
            // TODO: Add Operations; aka functions
            MtconnectModel rootPackage = new MtconnectModel(model, model.Model);
            foreach (var package in model.Model.Packages)
            {
                allPackages.Add(new PythonPackage(model, package) { Namespace = "Mtconnect" });
                // Packages
                var subpackages = getPackages(model, package);
                if (subpackages.Any())
                    allPackages.AddRange(subpackages);

                // Classes
                var classes = getClasses(model, package);
                if (classes.Any())
                    allClasses.AddRange(classes);

                // Enumerations
                var enumerations = getEnums(model, package);
                if (enumerations.Any())
                    allEnumerations.AddRange(enumerations);
            }
            // Profiles
            foreach (var profile in model.Model.Profiles)
            {
                if (profile.Packages.Any())
                {
                    foreach (var package in profile.Packages)
                    {
                        allPackages.Add(new PythonPackage(model, package) { Namespace = "Mtconnect" });
                        // Packages
                        var subpackages = getPackages(model, package);
                        if (subpackages.Any())
                            allPackages.AddRange(subpackages);

                        // Classes
                        var classes = getClasses(model, package);
                        if (classes.Any())
                            allClasses.AddRange(classes);

                        // Enumerations
                        var enumerations = getEnums(model, package);
                        if (enumerations.Any())
                            allEnumerations.AddRange(enumerations);
                    }
                }
            }

            _logger?.LogInformation("Saving Packages...");
            _generator.ProcessTemplate(allPackages, Path.Combine(_generator.OutputPath, "Packages"), true);
            _logger?.LogInformation("Saving Classes...");
            _generator.ProcessTemplate(allClasses, Path.Combine(_generator.OutputPath, "Classes"), true);
            _logger?.LogInformation("Saving Enums...");
            _generator.ProcessTemplate(allEnumerations, Path.Combine(_generator.OutputPath, "Enums"), true);

            _logger?.LogInformation("Saving Root Package...");
            _generator.ProcessTemplate(rootPackage, _generator.OutputPath, true);
        }

        private IEnumerable<PythonPackage> getPackages(XmiDocument model, UmlPackage package, string namespacePrefix = "Mtconnect")
        {
            namespacePrefix = $"{namespacePrefix}.{package.Name.ToPascalCase()}";
            var results = new List<PythonPackage>();
            foreach (var subpackage in package.Packages)
            {
                results.Add(new PythonPackage(model, subpackage) { Namespace = namespacePrefix });
                if (subpackage.Packages.Count > 0)
                    results.AddRange(getPackages(model, subpackage, namespacePrefix));
            }
            return results;
        }

        private IEnumerable<PythonEnum> getEnums(XmiDocument model, UmlPackage package, string namespacePrefix = "Mtconnect")
        {
            namespacePrefix = $"{namespacePrefix}.{package.Name.ToPascalCase()}";
            var results = new List<PythonEnum>();
            if (package.Enumerations.Count > 0)
                foreach (var item in package.Enumerations)
                    results.Add(new PythonEnum(model, item) { Namespace = namespacePrefix });
            if (package.Packages.Count > 0)
            {
                foreach (var item in package.Packages)
                {
                    var subEnums = getEnums(model, item, namespacePrefix);
                    if (subEnums.Any())
                        results.AddRange(subEnums);
                }
            }
            return results;
        }

        private IEnumerable<PythonClass> getClasses(XmiDocument model, UmlPackage package, string namespacePrefix = "Mtconnect")
        {
            namespacePrefix = $"{namespacePrefix}.{package.Name.ToPascalCase()}";
            var results = new List<PythonClass>();
            if (package.Classes.Count > 0)
                foreach (var item in package.Classes)
                    results.Add(new PythonClass(model, item) { Namespace = namespacePrefix });
            if ( package.Packages.Count > 0)
            {
                foreach(var item in package.Packages)
                {
                    var subClasses = getClasses(model, item, namespacePrefix);
                    if (subClasses.Any())
                        results.AddRange(subClasses);
                }
            }
            return results;
        }

    }
}
