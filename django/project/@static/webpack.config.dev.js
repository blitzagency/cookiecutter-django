var webpack = require("webpack");
var path = require("path");
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var BundleTracker = require('webpack-bundle-tracker');


module.exports = {
    // http://webpack.github.io/docs/configuration.html#context
    context: __dirname,

    // http://webpack.github.io/docs/configuration.html#entry
    entry: {
        'styles': './@css/styles.scss',
        // 'js/home': "./@modules/home/index.ts",
    },

    // http://webpack.github.io/docs/configuration.html#output
    output: {
        path: "../static",
        filename: "[name].js",
        publicPath: '/static/',
        // http://webpack.github.io/docs/configuration.html#output-chunkfilename
        chunkFilename: "[id].chunck.js"
    },

    // http://webpack.github.io/docs/configuration.html#plugins
    // http://webpack.github.io/docs/using-plugins.html
    plugins: [
        require('webpack-fail-plugin'), // makes the process return an error code on failure
        // https://webpack.github.io/docs/list-of-plugins.html#commonschunkplugin
        new webpack.optimize.CommonsChunkPlugin({
          name: "js/common",
          filename: "js/common.js"
        }),
        new ExtractTextPlugin("css/[name].css"),
        new BundleTracker({filename: '../../webpack-stats.json'}),
        new webpack.ProvidePlugin({
            'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch',
            'Promise':'bluebird'
        }),
    ],

    // http://webpack.github.io/docs/configuration.html#module
    module: {
        // http://webpack.github.io/docs/using-loaders.html
        loaders: [
            { test: /\.hbs$/, loader: "handlebars-loader",
                query: {
                    helperDirs: [
                        path.resolve(__dirname, './@modules/shared/ext/handlebars')
                    ]
                }
            },

            { test: /\.css$/, loader: ExtractTextPlugin.extract("style-loader", "css-loader") },
            { test: /\.scss$/, loader: ExtractTextPlugin.extract("style","css!sass")},
            { test: /\.tsx?$/, exclude: /node_modules/, loader: "ts-loader" },
            { test: /\.json$/, loader: 'json'},
            { test: /\.(woff|woff2|eot|ttf|svg)(\?[a-z0-9\#]+)?$/, loader: 'file-loader?name=fonts/[name].[ext]&limit=100000' },
            { test: /\.(jpe?g|png|gif)(\?[a-z0-9\#]+)?$/, loader: 'file-loader?name=img/[name].[ext]' },
            { test: /animation\.gsap\.js$/, loader: 'imports?define=>false'},
            { test: /ScrollToPlugin\.js$/, loader: 'imports?define=>false'},
            { test: /three\/examples\/.*/, loader: 'three-examples'},
            { test: /vex\.combined\.js$/, loader: 'imports?define=>false'}
        ],
    },
    // http://webpack.github.io/docs/configuration.html#devtool
    devtool: "source-map",

    // http://webpack.github.io/docs/configuration.html#resolve
    resolve: {
        alias: {
            'scrollmagic.gsap': 'scrollmagic/scrollmagic/uncompressed/plugins/animation.gsap',
            'scrolltoplugin': 'gsap/src/uncompressed/plugins/ScrollToPlugin'
        },
        // http://webpack.github.io/docs/configuration.html#resolve-modulesdirectories
        modulesDirectories: ["node_modules", "@modules", "@css", "@img"],
        // http://webpack.github.io/docs/configuration.html#resolve-extensions
        extensions: ["", ".webpack.js", ".web.js", ".ts", ".tsx", ".js"]
    },

    resolveLoader: {
        modulesDirectories: ["node_modules", "./loaders"],
    }
}
