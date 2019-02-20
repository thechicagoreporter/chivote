const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: path.resolve(__dirname, '..'),
  entry: './src/client',
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loaders: ['babel-loader']
      },
      {
        test: /\.s?css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader', 'sass-loader']
      },
      {
        test: /\.(png|jpg|gif)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]?[hash]',
              outputPath: 'images'
            }
          }
        ]
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        loader: 'file-loader'
      }
    ]
  },
  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.jsx', '.scss'],
    alias: {
      Assets: path.resolve(__dirname, '../src/assets/'),
      Components: path.resolve(__dirname, '../src/components/'),
      Public: path.resolve(__dirname, '../public/'),
      Theme: path.resolve(__dirname, '../src/theme/')
    }
  }
};