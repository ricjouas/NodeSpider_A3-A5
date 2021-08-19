<template>
  <section id="project">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-row align="center" justify="center">
            <v-col cols="12" md="7">
              <h1 class="font-weight-light display-2">Our Project : </h1>
              <h1 class="font-weight-light display-1 mb-3">
                Mission Smart Parcel Box
              </h1>
              <v-row>
                <v-col cols="12" class="d-flex align-center">
                  <p class="text-justify">
                    <h4>Project Description</h4>
                  </p>
                </v-col>
                <v-col cols="12" class="d-flex align-center">
                  <p class="text-justify">
                    Add our project description
                  </p>
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="12" md="5" class="d-none d-md-flex">
              <v-img
                src="@/assets/img/ill1.svg"
                class="d-block ml-auto mr-auto"
                max-width="400px"
              />
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<style scoped>
#project {
  background-color: #f4f7f5;
}
</style>
