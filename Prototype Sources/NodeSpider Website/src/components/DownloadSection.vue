<template>
  <section id="download">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-row align="center" justify="center">
            <v-col sm="4" class="hidden-xs-only">
              <v-img src="@/assets/img/ill2.svg" class="d-block ml-auto mr-auto" max-width="350px" />
            </v-col>
            <v-col cols="12" sm="8" class="white--text text-left">
              <h1 class="font-weight-light display-2 mb-2">Team Resources</h1>
              <h1 class="font-weight-light">
                Are you onboard with us? Great! 😊
              </h1>
              <h1 class="font-weight-light">
                We've got heaps of resources and technical documents for you to go through.
              </h1>
              <h1 class="font-weight-light">
                Feel free to check out our GitHub Team Repository or read our detailed report below.
              </h1>              
              <v-btn rounded outlined href="https://github.com/ricjouas/NodeSpider_A3-A5" target="_blank" large color="white" class="mt-4">
                <v-icon class="mr-2">
                  mdi-github
                </v-icon>
                GitHub Repo
              </v-btn>
              <v-btn rounded outlined href="https://github.com/ricjouas/NodeSpider_A3-A5/raw/main/NodeSpider%20A3%20Final%20Report.pdf" target="_blank" large color="white" class="mt-4">
                <v-icon class="mr-2">
                  mdi-file
                </v-icon>
                PDF Report
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<style scoped>
#download {
  background-image: url("~@/assets/img/bgDownload.jpg");
  background-attachment: fixed;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 500px;
}

#download .container,
#download .row {
  height: 100%;
}
</style>