var webpack = require("webpack");
var path = require("path");
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var BundleTracker = require("webpack-bundle-tracker");


/**
 * Webpack Docs:
 * - https://webpack.js.org/configuration/
 * - https://webpack.js.org/guides/migrating/ (1.x -> 2.x)
 */


module.exports = {
    context: path.resolve(__dirname),
    entry: {
        "js/common":  "common/index.js",
        "css/common": "common/index.scss",
        "js/ui":      "ui/index.js",
        "css/ui":     "ui/index.scss",
    },
    output: {
        path:          "../static",
        filename:      "[name].js",
        publicPath:    "/static/",
        chunkFilename: "[id].chunck.[ext]"
    },
    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
          name:     "js/common",
          filename: "js/common.js"
        }),
        new ExtractTextPlugin({filename: "[name].css"}),
        new BundleTracker({filename: "../../webpack-stats.json"}),
        new webpack.ProvidePlugin({
            "fetch":   "imports?this=>global!exports?global.fetch!whatwg-fetch",
            "Promise": "bluebird",
            "$":       "jquery",    // bootstrap.js support
            "jQuery":  "jquery",    // bootstrap.js support
        }),
    ],
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: "css-loader"
                })
            },
            {
                test: /\.scss$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: "css-loader!sass-loader"
                })
            },
            {
                test: /\.tsx?/,
                exclude: /node_modules/,
                loader: "ts-loader"
            },
            {
                test: /\.(woff|woff2|eot|ttf|svg)(\?\S*)?$/,
                use: [
                    {
                        loader: "file-loader",
                        options: {
                            name: "fonts/[name].[ext]",
                            limit: "100000"
                        }
                    }
                ]
            },
            {
                test: /\.(hbs|handlebars)$/,
                loader: "handlebars-loader"
            }
        ]
    },
    devtool: "source-map",
    resolve: {
        extensions: [".webpack.js", "web.js", ".ts", ".tsx", ".js"],
        alias: {
            "webworkify":        "webworkify-webpack",
            "bootstrap":         "bootstrap-sass/assets/javascripts/bootstrap",
            "bootstrap-styles":  "bootstrap-sass/assets/stylesheets",
            "breakpoint-styles": "breakpoint-sass/stylesheets",
            "bourbon-styles":    "bourbon/app/assets/stylesheets",
        },
        modules: ["node_modules", "@modules", "@css", "@img", "@tests"]
    }
}
