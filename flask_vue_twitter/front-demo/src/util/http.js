import axios from 'axios'

axios.defaults.timeout = 10000
axios.defaults.baseURL = 'http://127.0.0.1:5000/api/v1.0/'

axios.interceptors.request.use(
  config => {
    return config
  },
  err => {
    return Promise.reject(err)
  },
)

axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
        // ...
    }
    // console.log(JSON.stringify(error));//console : Error: Request failed with status code 402
    return Promise.reject(error.response.data)
  },
)

export default axios