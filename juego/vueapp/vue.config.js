/* const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true
}) */

/* const path = require('path');

module.exports = {
    publicPath: '/static/src/vue/dist/', // Should be STATIC_URL + path/to/build
    outputDir: path.resolve(__dirname, '../static/src/vue/dist/'), // Output to a directory in STATICFILES_DIRS
    filenameHashing: false, // Django will hash file names, not webpack
    runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
    devServer: {
        writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
    },
}; */

const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    publicPath: "http://0.0.0.0:8000",
    outputDir: "./dist/",

    chainWebpack: config => {
        config.optimization.splitChunks(false)

        config.plugin('BundleTracker').use(BundleTracker, [
            {
                filename: './webpack-stats.json'
            }
        ])

        config.resolve.alias.set('__STATIC__', 'static')

        config.devServer
            .public('http://0.0.0.0:8000')
            .host('0.0.0.0')
            .port(8000)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({'Access-Control-Allow-Origin': ['\*']})
    }
};