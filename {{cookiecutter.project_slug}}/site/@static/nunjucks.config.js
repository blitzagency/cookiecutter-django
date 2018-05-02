{% raw %}
var nunjucks = require("nunjucks");

/**
 * Use this file to configure Nunjucks.
 *
 * See:
 *     - https://mozilla.github.io/nunjucks/api.html#custom-filters
 *     - https://mozilla.github.io/nunjucks/api.html#configure
 *
 * Examples:
 *
 *      // Configure:
 *
 *      // nunjucks.configure([path], [opts])
 *
 *      // Global
 *      nunjucks.configure({
 *          autoescape: true,  // this is the default value
 *      })
 *
 *      // Configure at path
 *      nunjucks.configure("views", {
 *          autoescape: false,
 *      })
 *
 *      // Custom Filter:
 *
 *      // Usage (.njk)
 *      A message for you: {{ message|truncate(20) }}...
 *
 *      env.addFilter("truncate", function(str, count) {
 *          var ellip = count < str.length ? "..." : "";
 *          return str.slice(0, count) + ellip;
 *      })
 */

module.exports = function(env) {

    // Configure nunjucks here.
}

{% endraw %}
