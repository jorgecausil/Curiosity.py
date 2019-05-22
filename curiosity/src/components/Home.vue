<template>
 <div>
  <Base />
  <div class="page-header-image relative">
                <!-- <img src="demo-images/01.jpg" alt="About"> -->
            </div>
 
        <div id="content" class="site-content">
          <article>
              <div class="content-1070 ">
                <div class="video">
                  <video loop="loop" muted autoplay class="header-video-container vid hide-mobile">
                    <source src="static/video/fondo.mp4" type="video/mp4" width="100%" height="auto">
                  </video>
                </div>
                <div class="contenido">
                  
                  <div class="container">
                    <div class="row"> 
                      <div class="col">
                       
                      </div>
                      <div class="col-12">
                         <div class="row">
                           <div class="col-4">
                             <ul class="list-group">
                                <li class="text list-group-item d-flex justify-content-between align-items-center active">
                                  Informacion De Discos
                                  <!-- <span class=" badge badge-primary badge-pill">14</span> -->
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Espacio Libre
                                  <span class="badge badge-primary badge-pill" v-text="disco.Espacio_libre + ' Gb'" ></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Espacio Usado
                                  <span class="badge badge-primary badge-pill" v-text="disco.Espacio_usado + ' Gb'" ></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Espacio Total
                                 <span class="badge badge-primary badge-pill" v-text="disco.Espacio_total + ' Gb'" ></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Espacio Usado %
                                 <span class="badge badge-primary badge-pill" v-text="disco.Porcentaje_de_espacio_usado + ' %'" ></span>
                                </li>
                              </ul>
                           </div>
                           <div class="col-4">
                             <ul class="list-group">
                                <li class="text list-group-item d-flex justify-content-between align-items-center active">
                                  Datos de la placa
                                  <!-- <span class=" badge badge-primary badge-pill">14</span> -->
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Manufactura
                                  <span class="badge badge-primary badge-pill" v-text="placa.Manufacturer" ></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Producto
                                  <span class="badge badge-primary badge-pill" v-text="placa.product"></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Serial
                                  <span class="badge badge-primary badge-pill" v-text="placa.serialnumber"></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Version
                                  <span class="badge badge-primary badge-pill" v-text="placa.version"></span>
                                </li>
                              </ul>
                           </div>
                           <div class="col-4">
                             <ul class="list-group">
                                <li class="text list-group-item d-flex justify-content-between align-items-center active">
                                  Informacion De Red
                                  <!-- <span class=" badge badge-primary badge-pill">14</span> -->
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Ip Local
                                  <span class="badge badge-primary badge-pill" v-text="red.Ip_Local " ></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Ip Publica
                                  <span class="badge badge-primary badge-pill" v-text="red.Ip_Publica" ></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Nombre De Usuario Red
                                 <span class="badge badge-primary badge-pill" v-text="red.Nombre_de_Usuario_En_Red" ></span>
                                </li>
                              </ul>
                           </div>
                         </div>

                         <div class="row">
                            <div class="col-4">
                             <ul class="list-group">
                                <li class="text list-group-item d-flex justify-content-between align-items-center active">
                                  Informacion De Sistema
                                  <!-- <span class=" badge badge-primary badge-pill">14</span> -->
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Sistema Operativo & Version
                                 <span class="badge badge-primary badge-pill" v-text="sistema.Sistema_Operativo+ ' '+  sistema.Version" ></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Arquitectura
                                  <span class="badge badge-primary badge-pill" v-text="sistema.Arquitectura" ></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                   Nombre De Usuario
                                  <span class="badge badge-primary badge-pill" v-text="sistema.Nombre_De_Usuario" ></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Procesador
                                 <span class="badge badge-primary badge-pill" v-text="sistema.Procesador" ></span>
                                </li>
                              </ul>
                           </div>
                           <div class="col-4">
                             <ul class="list-group">
                                <li class="text list-group-item d-flex justify-content-between align-items-center active">
                                  Ubicación
                                  <!-- <span class=" badge badge-primary badge-pill">14</span> -->
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Latitúd
                                 <span class="badge badge-primary badge-pill" v-text="gps.latitud" ></span>
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                  Longitúd
                                  <span class="badge badge-primary badge-pill" v-text="gps.longitud" ></span>
                                </li>
                                 <div id='map' style=''></div>
                              </ul>
                           </div>
                           <div class="col-4">
                             <ul class="list-group">
                                <li class="text list-group-item d-flex justify-content-between align-items-center active">
                                  Image
                                  <!-- <span class=" badge badge-primary badge-pill">14</span> -->
                                </li>
                                <li class="text list-group-item d-flex justify-content-between align-items-center">
                                 
                                 <span class="badge badge-primary badge-pill"  ></span>
                                 <img :src="img">
                                </li>
                               
                                
                              </ul>
                           </div>
                         </div>
              
                      </div>
                      <div class="col">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </article>
        </div>
 </div>
</template>

<script>
import Base from './Base';

export default {
  name: 'Home',
    components: {
    Base,
  },
  data () {
    return {
      db:"",
      placa:{},
      red:{},
      disco:{},
      sistema:{},
      gps:{},
      puertos:{},
      img:"",

    }
  },
  mounted() {
   this.conectTofirebase()
   this.loadData()
   this.InitMap()
  },
  methods: {
    conectTofirebase(){
      var obj = this
      var config = {
        "apiKey": "AIzaSyDNyT41R1AXYpp6k7xP3m4S_EIUGibcj8s",
        "authDomain": "trape-py-1554172486593.firebaseapp.com",
        "databaseURL": "https://trape-py-1554172486593.firebaseio.com",
        "projectId": "trape-py-1554172486593",
        "storageBucket": "trape-py-1554172486593.appspot.com",
        "messagingSenderId": "415942529071"
      }
      firebase.initializeApp(config);
      obj.db = firebase.database()
    }, 
    loadData(){
      var obj = this
      firebase.database().ref('TRAPE/').on('value', function(snapshot) {
        console.log(snapshot.val().Foto)
        var data = snapshot.val()
        obj.placa = data.DInfoplaca
        obj.disco = data.Disk
        obj.red = data.Red
        obj.sistema = data.Sistema
        obj.gps = data.Ubicacion
        obj.img = "data:image/jpg;base64," + data.Foto
        
      });
    }, 
    InitMap(){
        // The location of Uluru
        var uluru = {lat: this.gps.latitud, lng: this.gps.longitud};
        // The map, centered at Uluru
        var map = new google.maps.Map(document.getElementById('map'), {zoom: 3, center: uluru});
        // The marker, positioned at Uluru
        var marker = new google.maps.Marker({position: uluru, map: map});
    }  
  },
}
</script>

<style>
body {
  overflow: hidden;
  height: 100vh;
}
  .content-1070 {
    width: 100%;
    max-width: 100%;
    position: relative;
  }
  .contenido {
    position: absolute;
    top: 0;
    width: 100%;
    color: white;
  }
  .container {
    margin-top: 50px;
  }
  .card-header{
    color:black;
  }

  .text{
    color: black;
  }
  .list-group-item.active {
    background-color: #242424;
    border-color: #242424;
  }
  .badge-primary {
    color: #fff;
    background-color: #242424;
}
.row{
  margin-top: 10px;
}
.vid {
    height: 100%;
    width: 100%;
}

.card{
  background: transparent;
}

#map {
        height: 400px;  /* The height is 400 pixels */
        width: 100%;  /* The width is the width of the web page */
       }
</style>


