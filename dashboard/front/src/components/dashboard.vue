<!--polling, get DeviceRecord data-->

<template>
  <div class="dashboard">
  {{record}}
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'dashboard',
  data (){
    return {
      record: null,
      msg: "hihihi"
    }
  },
  methods:{
    getRecordData(){
      axios
        .get('DeviceRecord')
        .then(response => (this.record = response.data.data))
        .catch(function(error) {
          console.log(error)
        });
    },
    polling(){
      window.setInterval(() => {
      setTimeout(this.getRecordData(), 0);
      }, 3000)
    },
  },
  created() {
    this.polling()
  },
}
</script>

<style scoped>
</style>
