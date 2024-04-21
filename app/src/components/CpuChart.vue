<template>
    <apexchart type="area" :options="options" :series="series"></apexchart>
</template>

<script>
export default {
  name: 'CpuChart',
  data() {
    return {
        options: {
        chart: {
          id: 'cpu-chart',
          zoom: {
            enabled: false
          },
          animations: {
            enabled: false,
            easing: 'linear',
            dynamicAnimation: {
              speed: 800
            }
          },
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: false
        },
        xaxis: {
          labels: {show: false}
        },
        yaxis: {
          min: 0,
          max: 100,
          show: false,
          labels: {
            style: {
              colors: ['#ffffff']
            }
          }
        },
        stroke: {
          curve: 'smooth',
          colors: undefined,
          width: 2
        },
        fill: {
          type: "gradient",
          gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.7,
            opacityTo: 0,
            stops: [0, 90, 100]
          }
        },
        theme: {
          palette: 'palette10'
        },
        legend: {
          labels: {
            colors: '#ffffff'
          }
        }

      },
      series: [{
        name: 'CPU Usage',
        data: this.$store.state.cpuLoad,
      }, {
        name: 'RAM Usage',
        data: this.$store.state.ramLoad
      }]
    }
  },
}
</script>