<template>
  <div class="home">
    <div class="home_background_container prlx_parent">
      <div class="home_background prlx with-background">
        <div class="home_content center-align">
          <h1>Cursos</h1>
        </div>
      </div>
    </div>
  </div>
  <div class="popular-section">
    <div class="center-align">
      <hr class="line-divider" />
      <h2>Todos los cursos</h2>
    </div>
    <div class="row">
      <div class="col s12 m6 l4">
        <div class="card oneofone">
          <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="../assets/Matematicas.png" />
          </div>
          <div class="card-content">
            <span class="card-title activator grey-text text-darken-4">
              Matemáticas<i class="material-icons right">more_vert</i>
            </span>
            <router-link to="/curso-matematicas"
              ><a class="waves-effect waves-light btn-large yellow accent-4">
                <div class="center-align">
                  Vamos allá<i class="material-icons right">send</i>
                </div></a
              ></router-link
            >
          </div>
        </div>
      </div>
      <div class="col s12 m6 l4">
        <div class="card">
          <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="../assets/comunicacion.png" />
          </div>
          <div class="card-content">
            <span class="card-title activator grey-text text-darken-4">
              Comunicación<i class="material-icons right">more_vert</i>
            </span>
            <router-link to="/curso-comunicacion"
              ><a class="waves-effect waves-light btn-large yellow accent-4">
                <div class="center-align">
                  Vamos allá<i class="material-icons right">send</i>
                </div></a
              ></router-link
            >
          </div>
        </div>
      </div>
      <div class="col s12 m6 l4">
        <div class="card">
          <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="../assets/ciencias.png" />
          </div>
          <div class="card-content">
            <span class="card-title activator grey-text text-darken-4">
              Ciencias y Tecnología<i class="material-icons right">more_vert</i>
            </span>
            <router-link to="/curso-ciencia"
              ><a class="waves-effect waves-light btn-large yellow accent-4">
                <div class="center-align">
                  Vamos allá<i class="material-icons right">send</i>
                </div></a
              ></router-link
            >
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col s12 m4 offset-m1">
        <div class="card">
          <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="../assets/historia.png" />
          </div>
          <div class="card-content">
            <span class="card-title activator grey-text text-darken-4">
              Ciencias Sociales<i class="material-icons right">more_vert</i>
            </span>
            <router-link to="/curso-social"
              ><a class="waves-effect waves-light btn-large yellow accent-4">
                <div class="center-align">
                  Vamos allá<i class="material-icons right">send</i>
                </div></a
              ></router-link
            >
          </div>
        </div>
      </div>
      <div class="col s12 m4 offset-m1">
        <div class="card">
          <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="../assets/trabajo.png" />
          </div>
          <div class="card-content">
            <span class="card-title activator grey-text text-darken-4">
              Educación para el Trabajo<i class="material-icons right"
                >more_vert</i
              >
            </span>
            <router-link to="/curso-trabajo"
              ><a class="waves-effect waves-light btn-large yellow accent-4">
                <div class="center-align">
                  Vamos allá<i class="material-icons right">send</i>
                </div></a
              ></router-link
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800|Roboto:400,500,700");

.with-background {
  background: url("../assets/contact_background.jpg") center/cover;
}

/*
Body
*/
.home {
  width: 100%;
  height: 400px;
}
.home_background_container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 350px;
}
.home_background {
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
.home_content {
  position: absolute;
  left: 50%;
  bottom: 50px;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
  background: #db3026;
  padding-left: 60px;
  padding-right: 60px;
}
.home_content h1 {
  font-size: 72px;
  color: #ffffff;
}
.line-divider {
  width: 5%;
  border-top: 5px solid #ffa000;
  margin: 0 auto;
}
.card-image img {
  width: 100%; /* O el ancho deseado */
  height: auto; /* Esto mantiene la proporción original de la imagen */
}
.card {
  width: 70%; /* O el ancho deseado */
  height: auto; /* Esto ajustará automáticamente la altura según el contenido */
  margin: 20px; /* Ajusta el margen según sea necesario */
  margin-left: 100px;
}
</style>
