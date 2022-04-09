import App from '../App'

const chart1 = r => require.ensure([], () => r(require('@/pages/chart1/index.vue')), 'chart1')

export default [{
    path: '/',
    component: App,
    children: [ 
        {
            path: '',
            redirect: '/chart1'
        },
        {
            path: '/chart1',
            component: chart1
        },
    ]
}]