// Notes:
//      - Dynamic require that builds all images in this
//        directory: `@static/@imgs/` and outputs them to the
//        directory defined in the loader inside webpack.config
//      - See: README.md for more details

function requireAll(requireContext) {
  return requireContext.keys().map(requireContext);
}
// requires and returns all modules that match
var modules = requireAll(require.context("./", true, /^\.\/.*\.(jpe?g|png|gif|svg)(\?[a-z0-9\#]+)?$/));
