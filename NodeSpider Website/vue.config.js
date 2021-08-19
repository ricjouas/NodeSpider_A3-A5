module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/NodeSpider_Website/'
    : '/',
  "transpileDependencies": [
    "vuetify"
  ]
}