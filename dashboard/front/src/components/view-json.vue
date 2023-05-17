<template>
<div class="container">
    <el-card class="card" shadow="always" v-for="item in data">
        <span class="mac">{{item.pk}}</span>
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
    background-color: rgb(137, 221, 131);
    padding: 2px;
    border-radius: 5px;
    font-size: 17px;
}
.ip{
    font-size: 17px;
    color: black;
}
</style>