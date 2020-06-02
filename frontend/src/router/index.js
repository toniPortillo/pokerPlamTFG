import Vue from 'vue'
import Router from 'vue-router'
import SignUp from '@/components/SignUp/SignUp'
import HelloWorld from '@/components/HelloWorld'
import Logout from '@/components/Logout/Logout'
import ConversationsList from '@/components/Conversations/List'
import ConversationNew from '@/views/Conversations/New'
import Conversation from '@/views/Conversations/Conversation'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/helloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout
    },
    {
      path: '/conversations',
      name: 'Conversations',
      component: ConversationsList
    },
    {
      path: '/conversations/new',
      name: 'ConversationNew',
      component: ConversationNew,
      props: true
    },
    {
      path: '/conversations/:id',
      name: 'Conversation',
      component: Conversation,
      props: true
    }
  ]
})
