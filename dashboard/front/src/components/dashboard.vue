<template>
  <el-container class="main-container">
    <el-aside class="aside">
      <side></side>
    </el-aside>

    <el-container>
      <el-header class="header">
        <h1 class="title">Devices</h1>
      </el-header>
      <el-main>
        <viewJson :data="record"></viewJson>
      </el-main>
    </el-container>

  </el-container>
</template>

<script>

import axios from 'axios'
import viewJson from './view-json.vue';
import side from './side.vue'

export default {

  name: 'dashboard',
  components: {
    viewJson,
    side,
  },

  data (){
    return {
      record: null,
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
    this.getRecordData()
    this.polling()
  },
  mounted(){
  }
}

</script>

<style scoped>
.logo{
  padding: 10px 20px;
  width: 70%;
  height: 70%;
}
.main-container{
  height:100%;
}
.header{
  text-align: left;
  font: optional;
  /* background-color: aliceblue; */
  /* TODO: just mark it differently */
}
.title{
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;  
  font-size: xx-large;
  color: rgb(0, 115, 187);
  margin-left: 20px;
}

.aside{
  background-color: rgb(255, 255, 255);
  box-shadow: inset;
  width: 160px;
  display: flex;
  flex-direction: column;
  align-items: center;
  /* TODO: just mark it differently */
}
</style>
