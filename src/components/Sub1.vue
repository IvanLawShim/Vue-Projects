<template>
  <div class="sub" v-html="buff">
  </div>
</template>

<script>
export default {
  data () {
    return {
      buff: ''
    }
  },
  mqtt: {
    /** 'VueMqtt/publish1' or '+/publish1' */
    'VueMqtt/publish1' (data) {
      this.buff = this.buff + data
    }
  }
}
</script>
