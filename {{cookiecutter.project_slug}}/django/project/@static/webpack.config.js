var webpack = require("webpack");
var path = require("path");
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var BundleTracker = require("webpack-bundle-tracker");
var CopyWebpackPlugin = require('copy-webpack-plugin');


/**
 * Webpack Docs:
 * - https://webpack.js.org/configuration/
 * - https://webpack.js.org/guides/migrating/ (1.x -> 2.x)
 */


var publicPath = '/static/';

// HEROKU
if(process.env.IS_HEROKU){
    var protocol = process.env.USE_HTTPS_FOR_ASSETS ? "https" : "http"
    publicPath = `${protocol}://${process.env.AWS_BUCKET_NAME}.s3.amazonaws.com/${process.env.VERSION}/`
} else if(process.env.STATIC_URL_BASE){
    var staticUrlBase = process.env.STATIC_URL_BASE;

    if(staticUrlBase[staticUrlBase.length - 1] == '/'){
        staticUrlBase = staticUrlBase.substring(0, staticUrlBase.length - 1)
    }

    publicPath = staticUrlBase + '/';
}


var config = {
    context: path.resolve(__dirname),
    entry: {
        // necessary to copy image files to /static, see README.md
        "imgs":       "./@imgs/index.js",
        "js/common":  "common/index.js",
        "css/common": "common/index.scss",
        "js/ui-kit":  "ui-kit/index.js",
        "css/ui-kit": "ui-kit/index.scss",
        "js/home":    "home/index.js",
        "css/home":   "home/index.scss",
    },
    output: {
        path:          path.resolve(__dirname, "../static"),
        filename:      "[name].js",
        publicPath:    publicPath,
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
        // SEE: https://github.com/kevlened/copy-webpack-plugin
        new CopyWebpackPlugin([
            // { "from": "@copy/path/to/file.ext", "to": "path/to/file.ext"},
        ]),
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
                    use: [{
                        loader: "css-loader"
                    }, {
                        loader: "sass-loader",
                        options: {
                            data: "$staticUrl: '" + publicPath + "';"
                        }
                    }]
                })
            },
            {
                test: /\.tsx?/,
                exclude: /node_modules/,
                use: "ts-loader"
            },
            {
                test: /\.(png|gif|jpe?g|svg)$/i,
                exclude: [
                    path.resolve(__dirname, "node_modules")
                ],
                use: [
                    {
                        loader: "file-loader",
                        options: {
                            name: "imgs/[name].[ext]",
                        }
                    }
                ]
            },
            {
                test: /\.(woff2?|eot|ttf|svg)(\?\S*)?$/,
                exclude: [
                    path.resolve(__dirname, "@imgs")
                ],
                use: [
                    {
                        loader: "file-loader",
                        options: {
                            name: "fonts/[name].[ext]",
                        }
                    }
                ]
            },
            {
                test: /\.(njk|nunjucks)$/,
                exclude: /node_modules/,
                use: {
                    loader: "nunjucks-loader",
                    options: {
                        config: path.resolve(__dirname, "nunjucks.config.js")
                    }
                }
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
        modules: ["node_modules", "@modules", "@css", "@imgs", "@tests"]
    }

}

if (process.env.WEBPACK_ENV == 'production'){
    config.plugins = config.plugins.concat([
        new webpack.optimize.UglifyJsPlugin({
        compress: {
            screw_ie8: true,
            warnings: false,
            unsafe_comps: true,
            unsafe: true,
            pure_getters: true
        },
        comments: false,
        sourceMap: true
        })
    ])

    config.module.rules = config.module.rules.concat([
        {
            test: /\.(js|ts)$/,
            loader: "webpack-strip?strip[]=console.warn,strip[]=console.log"
        },
    ])
}

module.exports = config
