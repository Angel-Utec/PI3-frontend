import axios from "axios";

const api = axios.create({
  baseURL: "http://3.227.141.198:5000",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export default {
  getPosts() {
    return api.get("/posts");
  },
  getCategories() {
    return api.get("/categories");
  },
  getUsers() {
    return api.get("/users");
  },
  postPost(post) {
    return api.post("/posts", post);
  },
  postCategory(category) {
    return api.post("/categories", category);
  },
  postUser(user) {
    return api.post("/users", user);
  },
  patchPost(id_post, post) {
    return api.patch("/posts/" + id_post, post);
  },
  patchCategory(id_category, category) {
    return api.patch("/categories/" + id_category, category);
  },
  patchUser(id_user, user) {
    return api.patch("/users/" + id_user, user);
  },
  deletePost(id_post) {
    return api.delete("/posts/" + id_post);
  },
  deleteCategory(id_category) {
    return api.delete("/categories/" + id_category);
  },
  deleteUser(id_user) {
    return api.delete("/users/" + id_user);
  },
};
