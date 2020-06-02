<template>
    <div class="signup-wrapper border border-light">
        <form class="form-signup" @submit.prevent="signup">
            <h2 class="form-signup-heading">CHAT!</h2>
            <div class="alert alert-danger" v-if="error">{{ error }}</div>
            <label for="inputUsername" class="sr-only"></label>
            <input v-model="username" type="username" id="inputUsername" class="form-control" placeholder="Usuario" required autofocus>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Entrar</button>
        </form>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'SignUp',
  data () {
    return {
      username: '',
      error: false
    }
  },
  computed: {
    ...mapGetters({ currentUser: 'currentUser' })
  },
  created () {
    this.checkCurrentSignUp()
  },
  updated () {
    this.checkCurrentSignUp()
  },
  methods: {
    signup () {
      this.axios.post('/users', {
        name: this.username
      })
        .then(res => this.signupSuccessful(res))
        .catch(() => this.signupFailed())
    },
    signupSuccessful (res) {
      if (!res.data) {
        this.signupFailed()
        return
      }
      this.error = false
      localStorage.setItem('user', JSON.stringify(res.data))
      this.$store.dispatch('signup')
      this.$router.push('/conversations')
    },
    signupFailed () {
      this.error = 'Sign up failed!'
      this.$store.dispatch('logout')
      localStorage.removeItem('user')
    },
    checkCurrentSignUp () {
      if (this.currentUser) {
        this.$router.replace(this.$route.query.redirect || '/conversations')
      }
    }
  }
}
</script>
