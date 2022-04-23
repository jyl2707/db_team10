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
      value-format="HH/mm/ss/MM/dd/yyyy"
      type="datetimerange"
      range-separator="to"
      start-placeholder="StartDate"
      end-placeholder="EndDate">
    </el-date-picker>
  </div>
  </el-form-item>
  <el-form-item label="Hashtag">
    <el-input v-model="query.hashtag" placeholder=""></el-input>
  </el-form-item>
  <el-form-item label="User_name">
    <el-input v-model="query.user_name" placeholder=""></el-input>
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
    @sort-change="sortRetweets"
    border
    style="width: 100%">
    <el-table-column
      prop="id_str"
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
      label="Author">
    </el-table-column>
    <el-table-column
      prop="retweet_num"
      sortable="custom"
      label="The number of retweet">
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
<el-button type="text" @click="dialogTableVisible = true">Dialog</el-button>

<el-dialog title="UserLis tO rReteetList" :visible.sync="dialogTableVisible">
  <el-table :data="gridData">
    <el-table-column property="date" label="date" width="150"></el-table-column>
    <el-table-column property="name" label="name" width="200"></el-table-column>
    <el-table-column property="address" label="url"></el-table-column>
  </el-table>
</el-dialog>


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
          gridData: [{
          date: '2016-05-02',
          name: 'Mr. Li',
          address: 'address'
        }, {
          date: '2016-05-04',
          name: 'Mr. Li',
          address: 'address'
        }, {
          date: '2016-05-01',
          name: 'Mr. Li',
          address: 'address'
        }, {
          date: '2016-05-03',
          name: 'Mr. Li',
          address: 'address'
        }],
      tableData: [],
      dialogTableVisible: false,
      createdAt: '',
      query: {
        size: 5,
        page: 1
      },

    };
  },
  mounted() {
      this.fetchCharts()
  },
  methods: {
    sortRetweets(column) {
      const key = column.column.label.split(' ')[column.column.label.split(' ').length -1 ]
      this.query[key] = column.order
      this.fetchCharts()
    },
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
     if (this.query.hashtag && (this.query.startDate || this.query.user_name || this.text)){
       this.$message.error('Multiple search conditions are not supported')
       return
     }
     if (this.query.startDate && (this.query.hashtag || this.query.user_name || this.text)){
       this.$message.error('Multiple search conditions are not supported')
       return
     }
     if (this.query.user_name && (this.query.startDate || this.query.hashtag || this.text)){
       this.$message.error('Multiple search conditions are not supported')
       return
     }
     if (this.query.text && (this.query.startDate || this.query.user_name || this.hashtag)){
       this.$message.error('Multiple search conditions are not supported')
       return
     }
      this.axios.get("/chart", {
        params: this.query
      }).then(res => {
        let { data } = res.data;
        try {
          // data = data.replaceAll(`'t`, ` not`)
          // data = data.replaceAll(`'`, `"`)
          console.log('data: ', data)
          data = JSON.parse(data)
          if (!(data instanceof Array)) {
            // data = [data]
          }
          console.log('data parsed: ', data)
          this.tableData = data 
        } catch(err) {
          console.log('err:', err)
          this.tableData = []
          // this.$message.error(JSON.stringify(err))
        }
        this.dataCount = res.data.counts
      }).catch(err => {
        // console.error(err)
        this.tableData = []
        this.$message.error('Network error')
      })
      
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

