<template>
  <el-container class="side-container">

    <el-main class="side-main">
      <img src="../assets/logo.svg" class="logo">

      <div class="menu">
        <el-row class="item">
          <span class="el-icon-question"></span>
          <a class="item-text" href="https://github.com/barnard33-233/cryptojacking-dashboard/">
            Manual
          </a>
        </el-row>

        <el-row class="item">
          <span class="el-icon-news"></span>
          <a class="item-text" href="https://github.com/barnard33-233/cryptojacking-dashboard/">
            Repository
          </a>
        </el-row>

      </div>
    </el-main>

    <el-footer class="footer">
        <span class="footer-text">
          Dashboard Version
        </span>
        <span class="footer-text">
          0.1
        </span>
    </el-footer>

  </el-container>
  
</template>

<script>
export default{
  name: 'side',
}
</script>

<style scoped>
.side-container{
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.side-main{
  margin-top: 40px;
}

.logo{  
  margin-top: 40px;
  margin-left: 60px;
  height: 130px;
  width: 130px;
}

.menu{
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: flex-start;
  margin-top: 20px;
}

.item{
  display: block;
  line-height: 300%;
  text-align: left;
  margin-top: 20px;
  margin-left: 40px;
  margin-right: 20px;
  box-shadow: inset;
}

.item-text{
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;  
  font-size: x-large;
  color: rgb(0, 115, 187);
  margin-left: 20px;
  text-decoration: none;
} 

.footer{
  display: flex;
  flex-direction: column;
  align-items: center;
}

.footer-text{
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;  
  font-size: 1.2em;
  color: rgb(0, 115, 187);
  margin-bottom: 20px;
}

</style>