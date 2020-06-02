<template>
  <div>
    <div class="page-header">
    <div>
      <input type="text" name="search" v-model="search" placeholder="Buscar Sala" class="form-control" />
    </div>
      <h2>Salas</h2>
        <router-link :to="{name: 'ConversationNew'}" replace>
          <button type="button" class="btn btn-primary">Añadir Sala</button>
        </router-link>
    </div>
    <div class='row'>
      <Bucket v-for="conversation in conversations" :key="conversation.id" :conversation="conversation" v-show="searchMatch(conversation.name)"></Bucket>
    </div>
  </div>
</template>

<script>
import Bucket from './Bucket'

export default {
  name: 'List',
  data () {
    return {
      search: '',
      conversations: []
    }
  },
  created () {
    this.axios.get('/conversations')
      .then(res => {
        this.buildConversationList(res.data)
      })
      .catch(() => {
        alert('Something went wrong')
      })
  },
  methods: {
    buildConversationList (data) {
      this.conversations = data
    },
    searchMatch (conversationName) {
      return conversationName.toLowerCase().match(this.searchRegExp)
    }
  },
  computed: {
    searchRegExp () {
      return new RegExp(`(.*)${this.search}(.*)`)
    }
  },
  components: {
    Bucket
  }
}
</script>
