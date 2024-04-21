<template>
  <div class="container">
    <Bar v-if="loaded" :data="chartData" />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'ChartComponent',
  components: { Bar },
  data: () => ({
    loaded: false,
    chartData: null
  }),
  async mounted () {
    this.loaded = false

    try {
      const { cpuArray } = this.$store.state.cpuLoad
      this.chartdata = {
        labels: ['random'],
        datasets: {
          label: 'data_one',
          backgroundColor: '#f87979',
          data: cpuArray
        }
      }
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>