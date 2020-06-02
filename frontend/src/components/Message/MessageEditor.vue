<template>
  <div>
    <form class="card message-form" v-on:submit.prevent="onSubmit(id, message)">
      <div class="card-block">
        <textarea class="form-control" v-model="message" placeholder="Escribe un mensaje..." rows="3">
        </textarea>
      </div>
      <div class="card-footer">
        <button class="btn btn-sm btn-primary">Enviar</button>
      </div>
    </form>
  </div>
</template>

<script>
import ListErrors from '@/components/ListErrors/ListErrors'
import { MESSAGE_CREATE } from '@/store/actions-type'

export default {
  name: 'MessageEditor',
  components: {
    ListErrors
  },
  props: {
    id: {
      type: String,
      required: true
    },
    content: {
      type: String,
      required: false
    }
  },
  data () {
    return {
      message: this.content || null,
      errors: {}
    }
  },
  methods: {
    onSubmit (id, message) {
      this.$store
        .dispatch(MESSAGE_CREATE, {
          id,
          message: {
            content: message,
            created_by: JSON.parse(localStorage.getItem('user')).name,
            conversation_id: this.id,
            user_id: JSON.parse(localStorage.getItem('user'))._id.$oid
          }
        })
        .then(() => {
          this.message = null
          this.errors = {}
        })
        .catch(({ response }) => {
          this.errors = response.data
        })
    }
  }
}
</script>
