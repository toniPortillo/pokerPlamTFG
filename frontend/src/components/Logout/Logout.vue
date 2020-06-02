<template>
<div></div>
</template>
<script>
export default {
  name: 'Logout',
  created () {
    delete localStorage.removeItem('user')
    this.$store.dispatch('logout')
    this.$router.push('/')
  }
}
</script>
