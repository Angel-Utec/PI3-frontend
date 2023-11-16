<template>
  <div>
    <div>
      <div class="container section">
        <h4>Buscar publicacion</h4>
        <div class="row card-panel">
          <form class="col s12" @submit.prevent="BuscarPost">
            <div class="input-field col s6">
              <input
                v-model="busqueda.search"
                placeholder="Ingresa el titulo a buscar"
                class="validate"
                required
              />
            </div>

            <button
              class="btn waves-effect waves-light right"
              type="submit"
              name="enviar"
            >
              Enviar
              <i class="material-icons right">send</i>
            </button>
          </form>
        </div>
      </div>
      <div class="container section">
        <table class="highlight">
          <thead>
            <tr>
              <th>Author</th>
              <th>title</th>
              <th>body</th>
              <th>created</th>
              <th>category</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="coincidencia in coincidencias" :key="coincidencia.id">
              <td>{{ getUserName(coincidencia.author) }}</td>
              <td>{{ coincidencia.title }}</td>
              <td>{{ coincidencia.body }}</td>
              <td>{{ coincidencia.created }}</td>
              <td>{{ getCategoryName(coincidencia.category_id) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="container section">
        <h4>Crear publicacion</h4>
        <div class="row card-panel">
          <form class="col s12" @submit.prevent="PublicarPost">
            <div class="input-field col s6">
              <input
                v-model="post.title"
                placeholder="Ingresa el titulo"
                class="validate"
                required
              />
            </div>
            <div class="input-field col s6">
              <input
                v-model="post.body"
                placeholder="Ingresa el contenido"
                class="validate"
                required
              />
            </div>

            <div class="input-field col s12">
              <a
                class="dropdown-trigger"
                href="#"
                data-target="category-dropdown"
                @click="openDropdown"
              >
                {{
                  getCategoryName(post.category_id) ||
                  "Selecciona una categoría"
                }}
                <i class="material-icons right">arrow_drop_down</i>
              </a>
              <ul id="category-dropdown" class="dropdown-content">
                <li v-for="category in categories" :key="category.id">
                  <a href="#" @click="selectCategory(category)">{{
                    category.name_category
                  }}</a>
                </li>
              </ul>
            </div>

            <div class="row">
              <div class="input-field col s12">
                <p>Categoría actual:</p>
                <input
                  disabled
                  :value="post.category_id"
                  id="disabled"
                  type="text"
                  class="validate"
                />
                <label for="disabled">{{
                  getCategoryName(post.category_id)
                }}</label>
              </div>
            </div>

            <button
              class="btn waves-effect waves-light right"
              type="submit"
              name="enviar"
            >
              Enviar
              <i class="material-icons right">send</i>
            </button>
          </form>
        </div>
      </div>
    </div>

    <div class="container section">
      <table class="highlight">
        <thead>
          <tr>
            <th>Post_ID</th>
            <th>Author</th>
            <th>title</th>
            <th>body</th>
            <th>created</th>
            <th>category</th>
            <th>edit</th>
            <th>delete</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="post in userPosts" :key="post.id">
            <td>{{ post.id }}</td>
            <td>{{ getUserName(post.author) }}</td>
            <td>{{ post.title }}</td>
            <td>{{ post.body }}</td>
            <td>{{ post.created }}</td>
            <td>{{ getCategoryName(post.category_id) }}</td>
            <td>
              <a
                @click="
                  editar(
                    post.id,
                    post.author,
                    post.title,
                    post.body,
                    post.category_id
                  )
                "
                ><i class="material-icons">create</i></a
              >
            </td>
            <td>
              <a @click="eliminar(post.id, post.author)"
                ><i class="material-icons">delete</i></a
              >
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Services from "@/services/Services";
import M from "materialize-css";

export default {
  name: "Post-manager",
  props: {
    user_id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      post: {
        title: "",
        body: "",
        author: 0,
        category_id: "",
      },
      posts: [],
      users: [],
      userPosts: [],
      categoriesMap: {},
      usersMap: {},
      categories: [],
      coincidencias: [],
      busqueda: {
        search: "",
      },
    };
  },

  created() {
    this.getPosts();
    this.getCategories();
    this.getUsers();
    const storedUserID = localStorage.getItem("user_id");
    if (storedUserID) {
      this.post.author = parseInt(storedUserID);
    }
  },
  mounted() {
    M.AutoInit();
  },
  methods: {
    openDropdown() {
      const dropdownTrigger = document.querySelector(".dropdown-trigger");
      const dropdownInstance = M.Dropdown.getInstance(dropdownTrigger);
      dropdownInstance.open();
    },
    getCategoryName(categoryId) {
      const category = this.categories.find((c) => c.id === categoryId);
      return category ? category.name_category : "";
    },
    getUserName(userId) {
      const user = this.users.find((u) => u.id === userId);
      return user ? user.username : "";
    },
    selectCategory(category) {
      this.post.category_id = category.id.toString();
    },

    getPosts() {
      Services.getPosts().then((response) => {
        const user_id = localStorage.getItem("user_id");
        this.posts = response.data.posts;
        for (let i = 0; i < this.posts.length; i++) {
          if (this.posts[i].author == user_id) {
            this.userPosts.push(this.posts[i]);
          }
        }
      });
    },
    getCategories() {
      Services.getCategories().then((response) => {
        this.categories = response.data.categories;
      });
    },
    getUsers() {
      Services.getUsers().then((response) => {
        this.users = response.data.users;
        console.log(this.users);
      });
    },
    PublicarPost() {
      const post = { ...this.post };
      Services.postPost(post).then((response) => {
        this.posts = response.data.posts;
      });
      location.reload();
    },
    BuscarPost() {
      const search = { ...this.busqueda };
      Services.postPost(search).then((response) => {
        this.coincidencias = response.data.posts;
      });
    },

    editar(post_id, post_author, post_title, post_body, category_id) {
      const storedUserID = localStorage.getItem("user_id");
      if (post_author != storedUserID) {
        alert("No puedes editar porque no es tu publicación");
        return;
      } else {
        localStorage.setItem("post_id", post_id);
        localStorage.setItem("titulo", post_title);
        localStorage.setItem("contenido", post_body);
        localStorage.setItem("category_id", category_id);
        const currentIP = window.location.host;
        const url = `http://${currentIP}/edit`;
        window.location.href = url;
      }
    },

    eliminar(post_id, post_author) {
      const storedUserID = localStorage.getItem("user_id");
      if (post_author != storedUserID) {
        alert("No puedes eliminar porque no es tu publicación");
        return;
      }
      if (!confirm("¿Desea eliminar el post?")) return;
      Services.deletePost(post_id).then((response) => {
        console.log("eliminado: ", response.data.posts);
      });
      location.reload();
    },
  },
};
</script>

<style scoped>
.container.section {
  background-color: #f0f0f0; /* Color de fondo para los contenedores */
  padding: 20px;
  margin-bottom: 20px;
}

.row.card-panel {
  background-color: rgba(
    255,
    255,
    255,
    0.8
  ); /* Color de fondo con baja opacidad para las card-panels */
  padding: 20px;
}

table.highlight {
  background-color: #fff; /* Color de fondo para las tablas */
  border-radius: 5px;
  overflow: hidden;
}

table.highlight th {
  background-color: #f0f0f0; /* Color de fondo para los encabezados de tabla */
  padding: 10px;
}

h4 {
  background-color: #f0f0f0; /* Color de fondo para los títulos */
  padding: 10px;
  margin-bottom: 20px;
  border-radius: 5px;
}
</style>
