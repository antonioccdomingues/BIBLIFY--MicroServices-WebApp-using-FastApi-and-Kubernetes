/*!

=========================================================
* Argon Dashboard React - v1.2.1
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard-react
* Copyright 2021 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/

import Profile from "views/examples/Profile.js";
import AddBook from "views/examples/AddBook.js";
import Register from "views/examples/Register.js";
import Login from "views/examples/Login.js";
import Tables from "views/examples/Tables.js";
import DeleteBook from "views/examples/DeleteBook.js";
//import Icons from "views/examples/Icons.js";

var routes = [
  {
    path: "/user-profile",
    name: "User Profile",
    icon: "ni ni-single-02 text-yellow",
    component: Profile,
    layout: "/admin",
  },
  {
    path: "/tables",
    name: "Books",
    icon: "ni ni-books text-red",
    component: Tables,
    layout: "/admin",
  },
  {
    path: "/add-book",
    name: "Add a Book",
    icon: "ni ni-ui-04 text-green",
    component: AddBook,
    layout: "/admin",
  },
  {
    path: "/delete-book",
    name: "Delete a Book",
    icon: "ni ni-fat-remove text-red",
    component: DeleteBook,
    layout: "/admin",
  },
  {
    path: "/login",
    name: "Login",
    icon: "ni ni-key-25 text-info",
    component: Login,
    layout: "/auth",
  },
  {
    path: "/register",
    name: "Register",
    icon: "ni ni-circle-08 text-pink",
    component: Register,
    layout: "/auth",
  },
];
export default routes;
