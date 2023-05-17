<!--
TODO: 整体设计

-->
<template>
  <el-container class="main-container">
    <el-aside class="aside">Aside</el-aside>

    <el-container>
      <el-header class="header">Header</el-header>
      <el-main>
        <viewJson :data="record"></viewJson>
      </el-main>
    </el-container>

  </el-container>
</template>

<script>

import axios from 'axios'
import viewJson from './view-json.vue';

export default {

  name: 'dashboard',
  components: {
    viewJson
  },

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
.main-container{
  height:100%;
}
.header{
  text-align: left;
  background-color: aliceblue;
  /* TODO: just mark it differently */
}

.aside{
  background-color: antiquewhite;
  /* TODO: just mark it differently */
}
</style>
