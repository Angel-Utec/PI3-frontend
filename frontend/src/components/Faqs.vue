<template>
  <section class="faq-section">
    <div class="container">
      <div class="row">
        <!-- ***** FAQ Start ***** -->
        <div class="col-md-6 offset-md-3">
          <div class="faq-title text-center pb-3">
            <h2>FAQ</h2>
          </div>
        </div>
        <div class="col-md-6 offset-md-3">
          <div class="faq" id="accordion">
            <!-- Pregunta 1 -->
            <div class="card">
              <div class="card-header" id="faqHeading-1">
                <div class="mb-0">
                  <h5
                    class="faq-title"
                    data-toggle="collapse"
                    data-target="#faqCollapse-1"
                    data-aria-expanded="true"
                    data-aria-controls="faqCollapse-1"
                  >
                    <span class="badge">1</span>¿Cómo puedo acceder a las clases
                    grabadas?
                  </h5>
                </div>
              </div>
              <div
                id="faqCollapse-1"
                class="collapse"
                aria-labelledby="faqHeading-1"
                data-parent="#accordion"
              >
                <div class="card-body">
                  <p>
                    Puedes acceder a las clases grabadas iniciando sesión en tu
                    cuenta de EducaTEC y escogiendo un curso en la sección de
                    guía.
                  </p>
                </div>
              </div>
            </div>

            <!-- Pregunta 2 -->
            <div class="card">
              <div class="card-header" id="faqHeading-2">
                <div class="mb-0">
                  <h5
                    class="faq-title"
                    data-toggle="collapse"
                    data-target="#faqCollapse-2"
                    data-aria-expanded="false"
                    data-aria-controls="faqCollapse-2"
                  >
                    <span class="badge">2</span>¿Qué recursos educativos ofrece
                    EducaTEC?
                  </h5>
                </div>
              </div>
              <div
                id="faqCollapse-2"
                class="collapse"
                aria-labelledby="faqHeading-2"
                data-parent="#accordion"
              >
                <div class="card-body">
                  <p>
                    EducaTEC ofrece una variedad de recursos educativos,
                    incluyendo materiales de lectura, videos educativos y
                    actividades interactivas. Puedes explorar estos recursos en
                    la sección correspondiente.
                  </p>
                </div>
              </div>
            </div>

            <!-- Pregunta 3 -->
            <div class="card">
              <div class="card-header" id="faqHeading-3">
                <div class="mb-0">
                  <h5
                    class="faq-title"
                    data-toggle="collapse"
                    data-target="#faqCollapse-3"
                    data-aria-expanded="false"
                    data-aria-controls="faqCollapse-3"
                  >
                    <span class="badge">3</span>¿Cómo puedo contribuir y apoyar
                    el proyecto EducaTEC?
                  </h5>
                </div>
              </div>
              <div
                id="faqCollapse-3"
                class="collapse"
                aria-labelledby="faqHeading-3"
                data-parent="#accordion"
              >
                <div class="card-body">
                  <p>
                    Si estás interesado en apoyar nuestro proyecto, puedes
                    visitar la sección de "Apóyanos" para obtener más
                    información sobre cómo contribuir financieramente o como
                    voluntario.
                  </p>
                </div>
              </div>
            </div>

            <!-- Pregunta 4 -->
            <div class="card">
              <div class="card-header" id="faqHeading-4">
                <div class="mb-0">
                  <h5
                    class="faq-title"
                    data-toggle="collapse"
                    data-target="#faqCollapse-4"
                    data-aria-expanded="false"
                    data-aria-controls="faqCollapse-4"
                  >
                    <span class="badge">4</span>¿Cuál es la edad recomendada
                    para utilizar EducaTEC?
                  </h5>
                </div>
              </div>
              <div
                id="faqCollapse-4"
                class="collapse"
                aria-labelledby="faqHeading-4"
                data-parent="#accordion"
              >
                <div class="card-body">
                  <p>
                    EducaTEC está diseñado principalmente para estudiantes de
                    4to y 5to de secundaria, pero sus recursos educativos pueden
                    ser útiles para estudiantes de diversas edades.
                  </p>
                </div>
              </div>
            </div>

            <!-- Pregunta 5 -->
            <div class="card">
              <div class="card-header" id="faqHeading-5">
                <div class="mb-0">
                  <h5
                    class="faq-title"
                    data-toggle="collapse"
                    data-target="#faqCollapse-5"
                    data-aria-expanded="false"
                    data-aria-controls="faqCollapse-5"
                  >
                    <span class="badge">5</span>¿Cómo puedo formar parte del
                    equipo de EducaTEC?
                  </h5>
                </div>
              </div>
              <div
                id="faqCollapse-5"
                class="collapse"
                aria-labelledby="faqHeading-5"
                data-parent="#accordion"
              >
                <div class="card-body">
                  <p>
                    Si estás interesado en unirte a nuestro equipo, contáctenos
                    mediante nuestro correo o nuestro número telefónico para
                    obtener mayor información.
                  </p>
                </div>
              </div>
            </div>

            <!-- Pregunta 6 -->
            <div class="card">
              <div class="card-header" id="faqHeading-6">
                <div class="mb-0">
                  <h5
                    class="faq-title"
                    data-toggle="collapse"
                    data-target="#faqCollapse-6"
                    data-aria-expanded="false"
                    data-aria-controls="faqCollapse-6"
                  >
                    <span class="badge">6</span>¿Puedo acceder a EducaTEC desde
                    cualquier ubicación?
                  </h5>
                </div>
              </div>
              <div
                id="faqCollapse-6"
                class="collapse"
                aria-labelledby="faqHeading-6"
                data-parent="#accordion"
              >
                <div class="card-body">
                  <p>
                    Sí, EducaTEC está disponible para estudiantes de todo el
                    país. Puedes acceder a la plataforma desde cualquier
                    ubicación con conexión a Internet.
                  </p>
                </div>
              </div>
            </div>

            <!-- Puedes agregar más preguntas y respuestas según tus necesidades -->
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<style>
.faq-section {
  background: #fdfdfd;
  min-height: 100vh;
  padding: 10vh 0 0;
}
.faq-title h2 {
  position: relative;
  margin-bottom: 45px;
  display: inline-block;
  font-weight: 600;
  line-height: 1;
}
.faq-title h2::before {
  content: "";
  position: absolute;
  left: 30%;
  width: 80px;
  height: 2px;
  background: #e91e63;
  bottom: -25px;
  margin-left: -30px;
}
.faq-title p {
  padding: 0 190px;
  margin-bottom: 10px;
}

.faq {
  background: #ffffff;
  box-shadow: 0 2px 48px 0 rgba(0, 0, 0, 0.06);
  border-radius: 4px;
}

.faq .card {
  border: none;
  background: none;
  border-bottom: 1px dashed #cee1f8;
}

.faq .card .card-header {
  padding: 0px;
  border: none;
  background: none;
  -webkit-transition: all 0.3s ease 0s;
  -moz-transition: all 0.3s ease 0s;
  -o-transition: all 0.3s ease 0s;
  transition: all 0.3s ease 0s;
}

.faq .card .card-header:hover {
  background: rgba(233, 30, 99, 0.1);
  padding-left: 10px;
}
.faq .card .card-header .faq-title {
  width: 100%;
  text-align: left;
  padding: 0px;
  padding-left: 30px;
  padding-right: 30px;
  font-weight: 400;
  font-size: 15px;
  letter-spacing: 1px;
  color: #3b566e;
  text-decoration: none !important;
  -webkit-transition: all 0.3s ease 0s;
  -moz-transition: all 0.3s ease 0s;
  -o-transition: all 0.3s ease 0s;
  transition: all 0.3s ease 0s;
  cursor: pointer;
  padding-top: 20px;
  padding-bottom: 20px;
}

.faq .card .card-header .faq-title .badge {
  display: inline-block;
  width: 20px;
  height: 20px;
  line-height: 14px;
  float: left;
  -webkit-border-radius: 100px;
  -moz-border-radius: 100px;
  border-radius: 100px;
  text-align: center;
  background: #e91e63;
  color: #fff;
  font-size: 12px;
  margin-right: 20px;
}

.faq .card .card-body {
  padding: 30px;
  padding-left: 35px;
  padding-bottom: 16px;
  font-weight: 400;
  font-size: 16px;
  color: #6f8ba4;
  line-height: 28px;
  letter-spacing: 1px;
  border-top: 1px solid #f3f8ff;
}

.faq .card .card-body p {
  margin-bottom: 14px;
}

@media (max-width: 991px) {
  .faq {
    margin-bottom: 30px;
  }
  .faq .card .card-header .faq-title {
    line-height: 26px;
    margin-top: 10px;
  }
}
</style>

<script>
export default {
  mounted() {
    // Define el nuevo nombre de la variable de almacenamiento local
    const newStorageVariable = "newRefreshPage";

    // Obtiene el valor actual de la nueva variable del almacenamiento local
    const refreshPage = localStorage.getItem(newStorageVariable);

    // Si la nueva variable no está definida o es 0, se puede realizar la recarga
    if (!refreshPage || refreshPage === "0") {
      // Llama al método para recargar la página
      this.refreshPage();

      // Elimina la variable del almacenamiento local
      localStorage.removeItem(newStorageVariable);

      // Vuelve a crear la variable y establece su valor en 1
      localStorage.setItem(newStorageVariable, "1");
    }
  },
  methods: {
    refreshPage() {
      // Recarga la página
      location.reload();
    },
  },
};
</script>
