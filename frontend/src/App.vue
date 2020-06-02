<template>
  <div id="app">
    <template v-if="currentUser">
      <div class="user" v-if="currentUser">
        <h1>{{ currentUser.name }}</h1>
      </div>
      <Navbar></Navbar>
    </template>
    <div class="container-fluid">
      <router-view></router-view>
      <template v-if="currentUser">
        <Foot></Foot>
      </template>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Navbar from './components/Navbar/Navbar'
import Foot from './components/Foot/Foot'

export default {
  name: 'app',
  computed: {
    ...mapGetters({ currentUser: 'currentUser' })
  },
  created () {
    this.checkCurrentLogin()
  },
  updated () {
    this.checkCurrentLogin()
  },
  methods: {
    checkCurrentLogin () {
      if (!this.currentUser) {
        if (this.$route.path === '/') {
          this.$router.push('/')
        } else {
          this.$router.push('/')
        }
      }
    }
  },
  components: {
    Navbar,
    Foot
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
