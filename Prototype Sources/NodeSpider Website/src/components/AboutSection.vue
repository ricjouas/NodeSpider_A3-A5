<template>
  <section id="about">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-row align="center" justify="center">
            <v-col cols="12" md="7">
              <h1 class="font-weight-light display-2">About Us</h1>
              <h1></h1>
              <v-row>
                <v-col cols="12" class="d-flex align-center">
                  <v-img
                    src="@/assets/img/logo.png"
                    max-width="200px"
                    class="mr-4"
                  />
                  <p class="text-justify">
                    We're a team of like-minded individuals that are not afraid to push boundaries.
                    We are bound by one common goal: Making sure that we use technology to improve people's lives.
                  </p>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<style scoped>
#about {
  background-color: #f4f7f5;
}
</style>
