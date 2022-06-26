
import {
    Button,
  Card,
  CardBody,
  FormGroup,
  Form,
  Input,
  InputGroupAddon,
  InputGroupText,
  InputGroup,
  Col,
  } from "reactstrap";
  // core components
  //import Header from "components/Headers/Header.js";
  //import axios from 'axios';
  import React from "react";
  import axios from 'axios';
  import { useState } from "react";
  
  
  const DeleteBook = () => {
    const [book_id, setBook_id] = useState('');
    // const [title, setTitle] = useState('');
    // const [date, setDate] = useState('');
    // const [amount_in_stock, setAmount_in_stock] = useState('');
    // const [amount_reserved, setAmount_reserved] = useState('');
    // const [authors, setAuthors] = useState('');
  
    const handleSubmit = (e) => {
      e.preventDefault();
    //   const blog = { "book_id": book_id};// "title": title, "date": date, "amount_in_stock": amount_in_stock, "amount_reserved": amount_reserved, "authors": [{"id": authors, "name":""}],  };
  
    //   fetch("http://biblify-stock.k3s/v1/books", {
    //     method: 'POST',
    //     headers: { "Content-Type": "application/json" },
    //     body: JSON.stringify(blog)
    //   }).then(() => {
    //     console.log('new blog added');
    //   })


    axios.delete('http://biblify-stock.k3s/v1/book/' + book_id)
        .then(() => console.log("Book deleted"));

    }
  
    return (
        
        <Col lg="5" md="7">
        <Card className="bg-secondary shadow border-0">
        <CardBody className="px-lg-5 py-lg-5">
        <div className="text-muted text-center mt-2 mb-3">
              <big>Delete Book</big>
            </div>
        <Form onSubmit={handleSubmit}>
            <FormGroup className="mb-3">
                <InputGroup className="input-group-alternative">
                    <InputGroupAddon addonType="prepend">
                        <InputGroupText >
                            <i className="ni ni-book-bookmark" />
                      
                        </InputGroupText>
                    </InputGroupAddon>
                    <Input 
                        type="number" 
                        placeholder="Book ID"
                        required 
                        value={book_id}
                        onChange={(e) => setBook_id(e.target.value)}
                    />
                </InputGroup>
            </FormGroup>

            {/* <FormGroup className="mb-3">
                <InputGroup className="input-group-alternative">
                    <InputGroupAddon addonType="prepend">
                        <InputGroupText >
                            <i className="ni ni-circle-08" />
                      
                        </InputGroupText>
                    </InputGroupAddon>
                    <Input 
                        type="text" 
                        placeholder="Title"
                        required
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                    />
                </InputGroup>
            </FormGroup> */}

            {/* <FormGroup className="mb-3">
                <InputGroup className="input-group-alternative">
                    <InputGroupAddon addonType="prepend">
                        <InputGroupText >
                            <i className="ni ni-calendar-grid-58" />
                      
                        </InputGroupText>
                    </InputGroupAddon>
                    <Input 
                        type="text" 
                        placeholder="Date"
                        required
                        value={date}
                        onChange={(e) => setDate(e.target.value)}
                    />
                </InputGroup>
            </FormGroup> */}

            {/* <FormGroup className="mb-3">
                <InputGroup className="input-group-alternative">
                    <InputGroupAddon addonType="prepend">
                        <InputGroupText >
                            <i className="ni ni-box-2" />
                      
                        </InputGroupText>
                    </InputGroupAddon>
                    <Input 
                        type="number" 
                        placeholder="Amount in Stock"
                        required
                        value={amount_in_stock}
                        onChange={(e) => setAmount_in_stock(e.target.value)}
                    />
                </InputGroup>
            </FormGroup> */}

            {/* <FormGroup className="mb-3">
                <InputGroup className="input-group-alternative">
                    <InputGroupAddon addonType="prepend">
                        <InputGroupText >
                            <i className="ni ni-bag-17" />
                      
                        </InputGroupText>
                    </InputGroupAddon>
                    <Input 
                        type="number" 
                        placeholder="Amount Reserved"
                        required
                        value={amount_reserved}
                        onChange={(e) => setAmount_reserved(e.target.value)}
                    />
                </InputGroup>
            </FormGroup> */}

            {/* <FormGroup className="mb-3">
                <InputGroup className="input-group-alternative">
                    <InputGroupAddon addonType="prepend">
                        <InputGroupText >
                            <i className="ni ni-badge" />
                      
                        </InputGroupText>
                    </InputGroupAddon>
                    <Input 
                        type="number" 
                        placeholder="Authors id"
                        required
                        value={authors}
                        onChange={(e) => setAuthors(e.target.value)}
                    />
                </InputGroup>
            </FormGroup> */}

          {/* <textarea
            required
            value={body}
            onChange={(e) => setBody(e.target.value)}
          ></textarea>
          <label>Blog author:</label>
          <select
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
          >
            <option value="mario">mario</option>
            <option value="yoshi">yoshi</option>
          </select> */}
        <div className="text-center">
            <Button className="my-4" color="primary" type="submit"> Delete Book </Button>
        </div>
        </Form>
        </CardBody>
        </Card>
        </Col>
    );
  }
  
  export default DeleteBook;
  
  
  
  