<template>
  <v-footer dark padless>
    <v-card flat tile class="secondary white--text text-center">
      <v-card-text class="white--text pt-0">
        <v-img src="~@/assets/rmit.png" contain height="100px" width="100" class="mx-auto"><a href="rmit.com.au"></a></v-img>
        <h5>Built for the purpose of an Assignment with RMIT University</h5>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong>NodeSpider. All rights reserved.</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<style scoped>
.v-card {
  width: 100%;
}
</style>
