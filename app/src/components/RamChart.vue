<template>
<section data-bs-theme="dark" class="bg-body-tertiary">
    <apexchart width="500" type="pie" :options="chartOptions" :series="series"></apexchart>
    <button @click="updateChart">isdjai</button>
</section>
</template>

<script>
export default {
  name: 'RamChart',
  data() {
    return {
        series: [this.$store.state.ramLoad[0], 100-this.$store.state.ramLoad[0]],
          chartOptions: {
            chart: {
              width: 380,
              type: 'pie',
            },
            labels: ['Free Ram', 'Used Ram'],
            responsive: [{
              breakpoint: 480,
              options: {
                chart: {
                  width: 200
                },
                legend: {
                  position: 'bottom'
                }
              }
            }],
      }
    }
  },
  methods: {
    updateChart() {
      this.series[0] = this.$store.state.ramLoad[this.$store.state.ramLoad.length-1]
      this.series[1] = 100 - this.$store.state.ramLoad[this.$store.state.ramLoad.length-1]
      console.log(this.series)
    }
  }
}
</script>