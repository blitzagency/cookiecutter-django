var webpackConfig = require("./webpack.config.dev.js");
var path = require('path');


module.exports = function(config) {
    // Setup Webpack Conf -------------

    // The test files will act as the entry points.
    // imports there will deal with entries.
    var common = path.resolve(
        webpackConfig.context, '@modules', webpackConfig.entry["js/common"]);

    webpackConfig.entry = {
        "js/common": common
    };

    // Remove commonChunk plugin for tests
    webpackConfig.plugins.shift();

    // Add tests to modules conf
    // webpackConfig.resolve.modules.push(path.resolve(__dirname, "@tests"));

    // Fix resolution error regarding "fs" in glob.js
    // Found here: https://github.com/pugjs/pug-loader/issues/8#issuecomment-55568520
    webpackConfig.node = {
        fs: "empty",
    };

    // Karma Config -------------------

    config.set({
        frameworks: ["jasmine"],
        browsers: ["PhantomJS"],
        reporters: ["dots"],
        autoWatch: true,
        logLevel: config.LOG_INFO,
        port: 3000,

        files: [
            // all files ending in "_test"
            "@tests/*_test.js",
            "@tests/**/*_test.js",
            "@tests/*_test.ts",
            "@tests/**/*_test.ts"
            // each file acts as entry point for the webpack configuration
        ],

        preprocessors: {
            // add webpack as preprocessor
            common: ["webpack", "sourcemap"],
            "@tests/*_test.js": ["webpack", "sourcemap"],
            "@tests/**/*_test.js": ["webpack", "sourcemap"],
            "@tests/*_test.ts": ["webpack", "sourcemap"],
            "@tests/**/*_test.ts": ["webpack", "sourcemap"]
        },

        webpack: webpackConfig,

        webpackMiddleware: {
            noInfo: true,
            stats: {
                colors: true,
                version: true,
                noInfo: true,
                debug: true,
                errorDetails: true
            }
        }
    });
};
