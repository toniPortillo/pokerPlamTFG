<template>
  <div class="card">
    <ul class="list-group list-group-flush">
      <li class="list-group-item"><strong>{{message.created_by}}:  </strong>{{ message.content }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Message',
  props: {
    id: {
      type: String,
      required: true
    },
    message: {
      type: Object,
      required: true
    }
  }
}
</script>
