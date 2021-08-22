<template>
  <section id="team" class="pb-8">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-card style="width: 100%">
            <h1 class="text-center pt-6 font-weight-light display-2">Meet the Team</h1>
            <v-divider class="my-6"></v-divider>
            <v-row class="text-center">
              <v-col class="col-12 col-sm-6 col-md-4">
                <div class="flex-center">
                  <v-card-text>
                    <div class="flex-center">
                      <div class="circle1">
                        <div class="circle2">
                          <v-img src="~@/assets/richard.png"></v-img>
                        </div>
                      </div>
                    </div>
                    <div class="black--text text-uppercase text-h5 my-2">Richard Jouas</div>
                    <v-divider class="my-2"/>
                    <div class="text-uppercase blue--text"><b>User interface Designer / Full-stack Developer</b></div>
                    <v-divider class="my-2"/>
                    <div class="blue--text">Richard is a full-time systems administrator and Bachelor of IT student with RMIT.</div>
                    <div class="blue--text">When he's not working or studying, he codes, writes his own apps or games, and reads about the latest tech developments.</div>
                    <div class="blue--text">He is also a big motorsport fan, and mostly watches Formula One and Indy Car racing.</div>
                    <div class="blue--text">When he's not glued to his monitor, he enjoys the outdoors, hiking, and exploring new restaurants with a glass of beer or whiskey.</div>
                    <v-btn :href="'https://ricjouas.github.io/IT_Website/'"
                        v-bind="size"
                        rounded
                        outlined
                        color="purple"
                        class="mt-6"
                    >
                      Visit Richard's page
                    </v-btn>
                  </v-card-text>
                  <v-divider style="margin-right: -23px" vertical v-if="this.$vuetify.breakpoint.smAndUp"></v-divider>
                </div>
                <v-divider class="mx-4" v-if="!this.$vuetify.breakpoint.smAndUp"></v-divider>
              </v-col>
              <v-col class="col-12 col-sm-6 col-md-4">
                <div class="flex-center">
                  <v-card-text>
                    <div class="flex-center">
                      <div class="circle1">
                        <div class="circle2">
                          <v-img src="~@/assets/jason.png"/>
                        </div>
                      </div>
                    </div>
                    <div class="black--text text-uppercase text-h5 my-2">Jason Hewitt</div>
                    <v-divider class="my-2"/>
                    <div class="text-uppercase blue--text"><b>Technical designer / Hardware Developer</b></div>
                    <v-divider class="my-2"/>
                    <div class="blue--text">Jason loves the outdoors, taking his dog Beetlejuice to the beach, surfing, hiking and camping. </div>
                    <div class="blue--text">Previously, he studied electrical engineering and currently works as an engineer, specifically in Industrial automation in the food industry.</div>
                    <div class="blue--text">His career has taken him to all parts of Australia, Iceland, Denmark and the UK.</div>
                    <div class="blue--text">He hopes to study IT to upskill himself for further career opportunities.</div>
                    <v-btn :href="'https://jasonhewitt86.github.io/cosc2196/'"
                        v-bind="size"
                        rounded
                        outlined
                        color="purple"
                        class="mt-6"
                    >
                      Visit Jason's page
                    </v-btn>
                  </v-card-text>
                  <v-divider style="margin-right: -23px" vertical v-if="this.$vuetify.breakpoint.mdAndUp"></v-divider>
                </div>
                <v-divider class="mx-4" v-if="!this.$vuetify.breakpoint.smAndUp"></v-divider>
              </v-col>
              <v-col class="col-12 col-md-4">
                <v-divider v-if="this.$vuetify.breakpoint.smOnly" class="mx-4"></v-divider>

                <div class="flex-center">
                  <v-card-text>
                    <div class="flex-center">
                      <div class="circle1">
                        <div class="circle2">
                          <v-img src="~@/assets/chevonne.png"/>
                        </div>
                      </div>
                    </div>
                    <div class="black--text text-uppercase text-h5 my-2">Chevonne Cheng</div>
                    <v-divider class="my-2"/>
                    <div class="text-uppercase blue--text"><b>Content Director</b></div>
                    <v-divider class="my-2"/>
                    <div class="blue--text">Chevonne is a herbivore and mother of two adopted dogs: a Chow Chow and a mixed-breed street dog.</div>
                    <div class="blue--text">She was born and raised in Singapore and previously studied marketing.</div>
                    <div class="blue--text">After spending over 8 years in communications and advertising, she decided to pursue RMIT's Bachelor of IT degree to explore new IT career paths, preferably in a field that promotes a positive cause.</div>                    
                    <v-btn :href="'https://s3913877.github.io/Assignment1MyProfile/Assignment1MyProfile/'"
                        v-bind="size"
                        rounded
                        outlined
                        color="purple"
                        class="mt-6"
                    >
                      Visit Chevonne's page
                    </v-btn>
                  </v-card-text>
                </div>              
              </v-col>
              <v-col class="col-12 col-sm-6 col-md-4">
                <div class="flex-center">
                  <v-card-text>
                    <div class="flex-center">
                      <div class="circle1">
                        <div class="circle2">
                          <v-img src="~@/assets/christopher.png"></v-img>
                        </div>
                      </div>
                    </div>
                    <div class="black--text text-uppercase text-h5 my-2">Christopher Grimley</div>
                    <v-divider class="my-2"/>
                    <div class="text-uppercase blue--text"><b>Researcher</b></div>
                    <v-divider class="my-2"/>
                    <div class="blue--text">Chris loves sci-fi horror movies. His interest in IT came as a blessing in disguise when a coworker convinced him to build a gaming PC.</div>
                    <div class="blue--text">While learning about hardware and software, he faced endless problems that needed solutions, which sparked his interest in IT. </div>
                    <div class="blue--text">He currently has a Certificate 3 in Information and Technology. </div>
                    <v-btn :href="'https://s3912799.github.io/COSC2196Assignment1/'"
                        v-bind="size"
                        rounded
                        outlined
                        color="purple"
                        class="mt-6"
                    >
                      Visit Christopher's page
                    </v-btn>
                  </v-card-text>
                  <v-divider style="margin-right: -23px" vertical v-if="this.$vuetify.breakpoint.smAndUp"></v-divider>
                </div>
                <v-divider class="mx-4" v-if="!this.$vuetify.breakpoint.smAndUp"></v-divider>
              </v-col>
              <v-col class="col-12 col-sm-6 col-md-4">
                <div class="flex-center">
                  <v-card-text>
                    <div class="flex-center">
                      <div class="circle1">
                        <div class="circle2">
                          <v-img src="~@/assets/duc.png"/>
                        </div>
                      </div>
                    </div>
                    <div class="black--text text-uppercase text-h5 my-2">Duc Hang</div>
                    <v-divider class="my-2"/>
                    <div class="text-uppercase blue--text"><b>Researcher</b></div>
                    <v-divider class="my-2"/>
                    <div class="blue--text">Hang is a raccoon-loving, Australian-born Vietnamese who is currently studying for a Bachelor of Business.</div>
                    <div class="blue--text">Her interest in IT started when she was working as an inventory controller where she came across the concept of RFID.</div>
                    <div class="blue--text">She has 6 years professional experience in the retail sector, over 3 years in supply chain.</div>
                    <div class="blue--text">She's looking to develop her knowledge and skills to hopefully have a career as a business analyst. </div>
                    <v-btn :href="'https://duc-hang.github.io/Assessment-1---My-Profile/'"
                        v-bind="size"
                        rounded
                        outlined
                        color="purple"
                        class="mt-6"
                    >
                      Visit Duc's page
                    </v-btn>
                  </v-card-text>
                  <v-divider style="margin-right: -23px" vertical v-if="this.$vuetify.breakpoint.mdAndUp"></v-divider>
                </div>
                <v-divider class="mx-4" v-if="!this.$vuetify.breakpoint.smAndUp"></v-divider>
              </v-col>
              <v-col class="col-12 col-md-4">
                <v-divider v-if="this.$vuetify.breakpoint.smOnly" class="mx-4"></v-divider>

                <div class="flex-center">
                  <v-card-text>
                    <div class="flex-center">
                      <div class="circle1">
                        <div class="circle2">
                          <v-img src="~@/assets/ben.png"/>
                        </div>
                      </div>
                    </div>
                    <div class="black--text text-uppercase text-h5 my-2">Ben Wakefield</div>
                    <v-divider class="my-2"/>
                    <div class="text-uppercase blue--text"><b>Researcher</b></div>
                    <v-divider class="my-2"/>
                    <div class="blue--text">Ben always had an interest in programming, drawing, and technology.</div>
                    <div class="blue--text">He was born and raised in Australia and graduated from Springwood State Highschool in 2020.</div>
                    <div class="blue--text">Being the quiet type, he likes to spend his free time playing video games with his friends.</div>
                    <v-btn :href="'https://doot5.github.io/A1-Assessment/'"
                        v-bind="size"
                        rounded
                        outlined
                        color="purple"
                        class="mt-6"
                    >
                      Visit Ben's page
                    </v-btn>
                  </v-card-text>
                </div>              
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <div class="svg-border-rounded text-light">
      <!-- <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 144.54 17.34"
        preserveAspectRatio="none"
        fill="currentColor"
      >
        <path
          d="M144.54,17.34H0V0H144.54ZM0,0S32.36,17.34,72.27,17.34,144.54,0,144.54,0"
        />
      </svg> -->
      <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 320"
          preserveAspectRatio="none"
          fill="currentColor"
      >
        <path
            d="M0,64L80,90.7C160,117,320,171,480,181.3C640,192,800,160,960,138.7C1120,117,1280,107,1360,101.3L1440,96L1440,320L1360,320C1280,320,1120,320,960,320C800,320,640,320,480,320C320,320,160,320,80,320L0,320Z"
        ></path>
      </svg>
    </div>
  </section>
</template>

<style lang="scss">
$main_color: #283e79;

ul {
  font-size: 13px;
  line-height: 1.5em;
  margin: 5px 0 15px;
  padding: 0;

  li {
    list-style: none;
    position: relative;
    padding: 0 0 0 20px;
  }

  li {
    &::before {
      content: "";
      position: absolute;
      left: 0;
      top: 5px;
      width: 10px;
      height: 10px;
      background-color: $main_color;
      border-radius: 50%;
      -moz-border-radius: 50%;
      -webkit-eeborder-radius: 50%;
    }
  }
}
</style>

<style scoped>
.header {
  background-color: #283e79;
  color: white;
}

.circle1 {
  border-radius: 50%;
  width: 150px;
  height: 150px;
  background-color: #f0f8ff;
  display: flex;
  align-items: center;
  justify-content: center;
}

.circle2 {
  border-radius: 50%;
  width: 100px;
  height: 100px;
  background-color: #e0effc;
  display: flex;
  align-items: center;
  justify-content: center;
}

.flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.svg-border-rounded svg {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  color: #f4f7f5;
  z-index: -1;
}

#pricing {
  z-index: 0;
}

.content {
  z-index: 1;
}

svg {
  overflow: hidden;
}

section {
  position: relative;
}
</style>

<script>
export default {
  data: () => ({
    planos: [
      {
        title: "Básico",
        price: "R$100,00",
        img: "f1.png",
        features: [
          {
            icon: {
              text: "mdi-check",
              color: "success",
            },
            text: "Feature 1",
          },
          {
            icon: {
              text: "mdi-check",
              color: "success",
            },
            text: "Feature 2",
          },
          {
            icon: {
              text: "mdi-cancel",
              color: "red",
            },
            text: "Feature 3",
          },
          {
            icon: {
              text: "mdi-cancel",
              color: "red",
            },
            text: "Feature 4",
          },
        ],
      },
      {
        title: "Padrão",
        price: "R$150,00",
        img: "f2.png",
        features: [
          {
            icon: {
              text: "mdi-check",
              color: "success",
            },
            text: "Feature 1",
            color: "success",
          },
          {
            icon: {
              text: "mdi-check",
              color: "success",
            },
            text: "Feature 2",
          },
          {
            icon: {
              text: "mdi-check",
              color: "success",
            },
            text: "Feature 3",
            color: "success",
          },
          {
            icon: {
              text: "mdi-cancel",
              color: "red",
            },
            text: "Feature 4",
          },
        ],
      },
      {
        title: "Premium",
        price: "R$250,00",
        img: "f3.png",
        features: [
          {
            icon: {
              text: "mdi-check",
              color: "success",
            },
            text: "Feature 1",
            color: "success",
          },
          {
            icon: {
              text: "mdi-check",
              color: "success",
            },
            text: "Feature 2",
          },
          {
            icon: {
              text: "mdi-check",
              color: "success",
            },
            text: "Feature 3",
            color: "success",
          },
          {
            icon: {
              text: "mdi-check",
              color: "success",
            },
            text: "Feature 4",
            color: "success",
          },
        ],
      },
    ],
  }),
  computed: {
    size() {
      const size = {md: "large", xl: "x-large"}[
          this.$vuetify.breakpoint.name
          ];
      return size ? {[size]: true} : {};
    }
  },
};
</script>