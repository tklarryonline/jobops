import React, {Component} from 'react';
import axios from "axios";
import './App.css';
import Modal from "./components/Modal";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      modal: false,
      jobsList: [],
      activeItem: {
        title: "",
        description: "",
        status: "",
        company: ""
      }
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/jobs/")
      .then(res => this.setState({ jobsList: res.data }))
      .catch(err => console.log(err));
  };

  toggle = () => {
    this.setState({modal: !this.state.modal});
  };

  handleSubmit = item => {
    this.toggle();
    if (item.id) {
      axios
        .put(`/api/jobs/${item.id}`, item)
        .then(res => this.refreshList());
      return;
    }

    axios
      .post("/api/jobs/", item)
      .then(res => this.refreshList());
  };

  handleDelete = item => {
    axios
      .delete(`/api/jobs/${item.id}`)
      .then(res => this.refreshList());
  };

  createItem = () => {
    const item = {
      title: "",
      description: "",
      status: "",
      company: ""
    };
    this.setState({activeItem: item, modal: !this.state.modal});
  };

  editItem = item => {
    this.setState({activeItem: item, modal: !this.state.modal});
  };

  renderItems = () => {
    return this.state.jobsList.map(item => (
      <li
        key={ item.id }
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={ `job--title mr-2 ${
            !item.status ? "job--completed" : ""
            }` }
          title={ item.description }
        >
          { item.title }
          &nbsp;
          <span className="badge badge-secondary">{ item.status }</span>
        </span>
        <span>
          <button onClick={ () => this.editItem(item) } className="btn btn-secondary mr-2">Edit</button>
          <button onClick={ () => this.handleDelete(item) } className="btn btn-danger">Delete</button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="content">
        <h1 className="text-white text-uppercase text-center my-4">Job Ops</h1>
        <div className="row ">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="">
                <button
                  onClick={ this.createItem }
                  className="btn btn-primary"
                >
                  Add job
                </button>
              </div>
              <ul className="list-group list-group-flush">
                { this.renderItems() }
              </ul>
            </div>
          </div>
        </div>
        { this.state.modal ? (
          <Modal
            activeItem={ this.state.activeItem }
            toggle={ this.toggle }
            onSave={ this.handleSubmit }
          />
        ) : null }
      </main>
    );
  }
}

export default App;
