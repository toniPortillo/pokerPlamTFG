<template>
  <div class="editor-page">
    <div class="container page">
      <div class="row">
        <div class="col-md-10 offset-md-1 col-xs-12">
          <listErrors :errors="errors"/>
          <form v-on:submit.prevent="onPublish(conversation)">
            <fieldset :disabled="inProgress">
              <fieldset class="form-group">
                <input
                  type="text"
                  class="form-control form-control-lg"
                  v-model="conversation.name"
                  placeholder="Nombre">
              </fieldset>
            </fieldset>
            <button
              :disabled="inProgress"
              class="btn btn-lg pull-xs-right btn-primary"
              type="submit">
              Guardar
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import store from '@/store'
import ListErrors from '@/components/ListErrors/ListErrors'
import { CONVERSATION_RESET_STATE, CONVERSATION_PUBLISH } from '@/store/actions-type'

export default {
  name: 'ConversationNew',
  components: { ListErrors },
  async beforeRouteEnter (to, from, next) {
    await store.dispatch(CONVERSATION_RESET_STATE)
    await store.dispatch(CONVERSATION_RESET_STATE)
    return next()
  },
  async beforeRouteLeave (to, from, next) {
    await store.dispatch(CONVERSATION_RESET_STATE)
    next()
  },
  data () {
    return {
      inProgress: false,
      errors: {}
    }
  },
  computed: {
    ...mapGetters(['conversation'])
  },
  methods: {
    onPublish (conversation) {
      let action = CONVERSATION_PUBLISH
      this.inProgress = true
      this.$store
        .dispatch(action)
        .then(({ data }) => {
          this.inProgress = false
          this.$router.push({
            name: 'Conversations',
            params: { id: data.id }
          })
        })
        .catch(({ response }) => {
          this.inProgress = false
          this.errors = response.data
        })
    }
  }
}
</script>
