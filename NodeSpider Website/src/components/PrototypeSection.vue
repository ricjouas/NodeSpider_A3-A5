<template>
  <section id="prototype">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-row align="center" justify="center">
            <v-col cols="12" md="7">
              <h1 class="font-weight-light display-2">Our Prototype</h1>
              <h1 class="font-weight-light display-1 mb-5">
                One Mailbox to rule them all.
              </h1>
              <v-row>
                <v-col cols="12" class="d-flex align-center">
                  <v-img
                    src="@/assets/mailbox.png"
                    max-width="60px"
                    class="mr-4"
                  />
                  <p class="text-justify">
                    A sleek, durable stainless steel mailbox that can endure any weather. 
                    It has sensors to detect light, motion, and temperature, and a button to press when a delivery is made. 
                    A companion phone app allows you to accept or reject a delivery, track mail and parcels, and monitor mailbox trends at your fingertips. 
                    Lastly, its tamper alarm keeps thieves and animals away from your mail.
                  </p>
                </v-col>
                <v-col cols="12" class="d-flex align-center">
                  <v-img
                    src="@/assets/cpu.png"
                    max-width="60px"
                    class="mr-4"
                  />
                  <p class="text-justify">
                    Our Smart Mailbox combines mechanical and software engineering to deliver automation and ease of use. 
                    A tiny Arduino microcontroller inside the mailbox has sensors for humidity and temperature control. 
                    There is also a motion sensor, microphone and camera!
                    A WiFi/Bluetooth chip on the board easily connects to a router. 
                    It will send the sensors’ data to a custom-built cloud web server using the robust Django framework, which in return will store data in its PostgreSQL database.



                  </p>
                </v-col>
                <v-col cols="12" class="d-flex align-center">
                  <v-img
                    src="@/assets/idea.png"
                    max-width="60px"
                    class="mr-4"
                  />
                  <p class="text-justify">
                    Once the product launches, we will pitch the idea to Australia Post / DHL / FedEx to integrate our Smart Mailbox with their systems. 
                    We could also collaborate with key opinion leaders (KOLs) and online stores and promote the product through word-of-mouth.
                  </p>
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="12" md="5" class="d-none d-md-flex">
              <v-img
                src="@/assets/prototype.png"
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
#prototype {
  background-color: #f4f7f5;
}
</style>
