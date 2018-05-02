var webpackConfig = require("./webpack.config.js");
var path = require('path');

module.exports = function (config) {

    config.set({
        basePath: '',
        frameworks: ["mocha"],
        browsers: ["Chrome + Debugging"],
        reporters: ["dots"],
        autoWatch: true,
        logLevel: config.LOG_INFO,
        port: 3000,
        mime: {
            'text/x-typescript': ['ts', 'tsx']
        },
        files: [
            '@tests/**/*.ts'
        ],

        preprocessors: {
            "@tests/*_test.ts": ['webpack', 'sourcemap'],
            "@tests/**/*_test.ts": ['webpack', 'sourcemap']
        },
        customLaunchers: {
            "Chrome + Debugging": {
                base: 'Chrome',
                flags: ['--remote-debugging-port=9222'],
            }
        },
        webpack: {
            devtool: 'eval-source-map',
            resolve: {
                extensions: [".webpack.js", "web.js", ".ts", ".tsx", ".js"],
            },
            module: {
                loaders: [
                    { test: /\.tsx?$/, loader: 'ts-loader' }
                ]
            },
            stats: {
                colors: true,
                modules: true,
                reasons: true,
                errorDetails: true
            },
        }
    });
};