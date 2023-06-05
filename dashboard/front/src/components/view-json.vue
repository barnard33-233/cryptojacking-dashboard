<template>
<div class="container">
  <el-card class="card" shadow="always" v-for="item in data">
    <span class="mac" :style="get_color(item)">{{item.pk}}</span>
    <div class="ip">ip: {{item.fields.ip}}</div>
  </el-card>
</div>
</template>

<script>
export default{
  props:{data:[]},
  data(){
    return {
    }
  },
  computed:{
    get_color() {
      return (item) => {
        if(item.fields.safety == 1){
          return {'background-color' : 'rgb(255, 105, 105)'}
        }
        else if(item.fields.safety == 0){
          return {'background-color' : 'rgb(102, 255, 105)'}
        }
        else{
          return {'background-color' : 'rgb(195, 195, 195)'}
        }
      }
      
    }
  }
}

</script>

<style scoped>
.container{
  display: flex;
  justify-content: flex-start;
  flex-wrap: wrap;
}

.card{
  --item-width: 200px;
  width: calc(var(--item-width));
  height: 100px;
  padding: 4px;
  border-radius: 4px;
  text-align: left;
  line-height: 240%;
  margin-top: 20px;
  margin-right: calc((100% - var(--item-width) * var(--n)) / (var(--n) + 1));
  margin-left: 20px;
}

@media screen and (max-width: 800px) {
  item { --n: 3; }
}

@media screen and (max-width: 1000px) and (min-width: 800px) {
  item { --n: 4; }
}

@media screen and (max-width: 1200px) and (min-width: 1000px) {
  item { --n: 5; }
}

@media screen and (max-width: 8888px) and (min-width: 1200px) {
  item { --n: 6; } 
}

.mac{
  /* background-color: rgb(195, 195, 195); */
  padding: 2px;
  border-radius: 5px;
  font-size: 17px;
}
.ip{
  font-size: 17px;
  color: black;
}
</style>