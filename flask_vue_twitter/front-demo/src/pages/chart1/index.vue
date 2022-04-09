<template>
  <main class="container">
    <el-card class="box-card">
  <div slot="header" class="clearfix">
    <!-- <span>List</span> -->
    <el-form :inline="true" :model="query" class="demo-form-inline">
  <el-form-item label="Created_time">
    <div class="block">
    <span class="demonstration"></span>
    <el-date-picker
      v-model="createdAt"
      value-format="yyyy-MM-dd"
      format="yyyy-MM-dd"
      type="daterange"
      range-separator="至"
      start-placeholder="StartDate"
      end-placeholder="EndDate">
    </el-date-picker>
  </div>
  </el-form-item>
  <el-form-item label="Id">
    <el-input v-model="query.id" placeholder=""></el-input>
  </el-form-item>
  <el-form-item label="Twitter content">
    <el-input v-model="query.text" placeholder=""></el-input>
  </el-form-item>
  <el-form-item>
    <el-button  type="primary" @click="fetchCharts">Search</el-button>
  </el-form-item>
</el-form>
  </div>
   <el-table
    :data="tableData"
    border
    style="width: 100%">
    <el-table-column
      prop="id"
      label="ID"
      width="180">
    </el-table-column>
    <el-table-column
      prop="created_at"
      label="Date"
      width="180">
    </el-table-column>
    <el-table-column
      prop="text"
      label="text"
      width="180">
    </el-table-column>
    <el-table-column
      prop="user.name"
      label="Publisher">
    </el-table-column>
  </el-table>
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page.sync="query.page"
      :page-size="query.size"
      layout="total, prev, pager, next"
      :total="dataCount">
    </el-pagination>
</el-card>
  </main>
</template>

<script>
import { setInterval } from 'timers';
// data="[{ name: '2016', value: 2 },{ name: '2017', value: 1 },{ name: '2018', value: 3 }]"
export default {
  data() {
    return {
      dataCount: 0,
      chart_data: [],
      loop: undefined,
      tableData: [],
      createdAt: '',
      query: {
        size: 5,
        page: 1
      },

    };
  },
  mounted() {
      this.fetchCharts()
      this.loop = setInterval(()=>this.fetchCharts(), 125 << 8)
  },
  methods: {
    handleSizeChange(val) {
      this.query.size = val
      this.fetchCharts()
    },
    handleCurrentChange(val) {
      this.query.page = val
      this.fetchCharts()
    },
    fetchCharts() {
      console.log('-----', this.createdAt)
     // Omit error handling
     if (this.createdAt) {
       [this.query.startDate, this.query.endDate] = this.createdAt
     }
      this.axios.get("/chart", {
        params: this.query
      }).then(res => {
        let { data } = res.data;
        this.tableData = data.charts
        this.dataCount = res.data.counts
      });
    },
  },
  beforeDestroy() {
    //   this.loop = null
  }
};
</script>


<style scoped >
    .container {
      padding: 20px;
      max-width: 1200px;
      margin: 0 auto;
    }
    section {
        text-align: center
    }
</style>

