<template>
<div>
  <Nav />
  <table class="doc-loader">
            <tbody>
                <tr>
                    <td>
                        <img src="static/images/ajax-document-loader.gif" alt="Loading...">
                    </td>
                </tr>
            </tbody>
        </table>
</div>
</template>

<script>
import Nav from './Nav';

export default {
  name: 'Base',
    components: {
    Nav,
  },
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1',
      drawer: null,
      mapboxgl: require('mapbox-gl/dist/mapbox-gl.js')
    }
  },
  props: {
      source: String
  },
  mounted() {
    // this.InitMap()
  },
  methods: {
    handleSelect(key, keyPath) {
        console.log(key, keyPath);
    },
    InitMap(){
      this.mapboxgl.accessToken = 'pk.eyJ1IjoicmV5bG9zbyIsImEiOiJjamd6c3loZHMwaXlwMzJwNHNibTRzcHhoIn0.M7mY2nnRk3ffPAP64dwIXQ';
      new this.mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [-74.50, 40], // starting position
        zoom: 15 // starting zoom
      });
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
