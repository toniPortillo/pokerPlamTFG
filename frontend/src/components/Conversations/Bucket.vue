<template>
  <div class="col room text-center">
    <router-link :to="{
      name: 'Conversation',
      params: { name: conversation.name, id: conversation._id.$oid }
      }">
      <img :src="image" />
      <H3>{{conversation.name}}</H3>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Bucket',
  props: ['conversation'],
  data () {
    return {
      image: `http://via.placeholder.com/400x100?text=${encodeURIComponent(
        this.conversation.name
      )}`
    }
  }
}
</script>
