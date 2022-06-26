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
// reactstrap components
import {
  // Badge,
  // Card,
  // CardHeader,
  // CardFooter,
  // DropdownMenu,
  // DropdownItem,
  // UncontrolledDropdown,
  // DropdownToggle,
  // Media,
  // Pagination,
  // PaginationItem,
  // PaginationLink,
  // Progress,
  Table,
  //Container,
  //Row,
  //UncontrolledTooltip,
} from "reactstrap";
// core components
//import Header from "components/Headers/Header.js";
import axios from 'axios';
import React from "react";


class Tables extends React.Component{
  state = {
    books: []
  }

  componentDidMount() {
    axios.get("http://biblify-stock.k3s/v1/book")
      .then(res => {
        const books = res.data;
        this.setState({ books });
      })
  }
  render() {
    return (
      <Table className="table-hover table-striped">
      <thead>
      <tr>
          <th className="border-0">Book ID</th>
          <th className="border-0">Title</th>
          <th className="border-0">Date</th>
          <th className="border-0">Stock</th>
      </tr>
      </thead>
      <tbody>
      {
          this.state.books.map(
              book =>
              <tr>
                  <td>{book.book_id}</td>
                  <td>{book.title}</td>
                  <td>{book.date}</td>
                  <td>{book.amount_in_stock}</td>
              </tr>
          )
      }
      </tbody>
  </Table>
    )
  }
}

export default Tables;



