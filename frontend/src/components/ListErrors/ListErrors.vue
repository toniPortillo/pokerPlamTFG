<template v-show="errors">
  <ul class="error-messages">
    <li v-for="(err) in errors" :key="err">
      {{err}}
    </li>
  </ul>
</template>

<script>
export default {
  name: 'ListErrors',
  props: {
    errors: {
      type: Object,
      required: true
    }
  }
}
</script>
