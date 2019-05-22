<template>
        <!-- Left Sidebar -->
        <div id="sidebar" class="sidebar">
            <div class="menu-left-part">
                <div class="search-holder">
                    <label>
                        <input type="search" class="search-field" placeholder="" value="" name="s" title="Search for:">
                    </label>
                </div>
                <div class="site-info-holder">
                    <h1 class="site-title">Curiosity</h1>
                    <p class="site-description">
                       Proyecto para captura de datos en un equipo remoto y en tiempo real.
                    </p>
                </div>
                <nav id="header-main-menu">
                    <ul class="main-menu sm sm-clean">
                        <li><a href="index.html" class="current">Inicio</a></li>
                        <li><a href="about.html">Captura  De Datos</a></li>
                    </ul>
                </nav>
                <footer>
                    <div class="footer-info">
                        © 2019 CURIOSITY. <br> CREATED<i class="fa fa-heart"></i> BY <a href="https://github.com/Reyloso">REINALDO LÓPEZ</a>-<a href="https://github.com/jorgecausil">JORGE CAUSÍL</a>.
                    </div>
                </footer>
            </div>
            <div class="menu-right-part">
                <div class="logo-holder">
                    <a href="index.html">
                        <img src="static/images/logo.png" alt="Suppablog WP">
                    </a>
                </div>
                <div class="toggle-holder">
                    <div id="toggle">
                        <div class="menu-line"></div>
                    </div>
                </div>
                <div class="social-holder">
                    <div class="social-list">
                        <a href="https://github.com/jorgecausil/trape.py"><i class="fab fa-github-square"></i></a>
                    </div>
                </div>
                <div class="fixed scroll-top"><i class="fa fa-caret-square-o-up" aria-hidden="true"></i></div>
            </div>
            <div class="clear"></div>
        </div>
</template>

<script>
import Vue from 'vue'

export default {
  data: ()=>({

  })
}
</script>

<style >

</style>
