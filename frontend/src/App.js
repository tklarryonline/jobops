import React, {Component} from 'react';
import './App.css';
import Modal from "./components/Modal";

const jobItems = [
  {
    id: 3,
    title: "Python Developer",
    description: "Dash Labs",
    status: "Applied",
    company: 2
  },
  {
    id: 2,
    title: "Python Developer",
    description: "ITbility",
    status: "Applied",
    company: 3
  },
  {
    id: 1,
    title: "Software Developer",
    description: "CommonCode.",
    status: "Technical Interview",
    company: 1
  },
  {
    id: 4,
    title: "Full-stack Developer",
    description: "",
    status: "Initial Interview",
    company: 4
  }
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      modal: false,
      jobsList: jobItems,
      activeItem: {
        title: "",
        description: "",
        status: "",
        company: ""
      }
    };
  }

  toggle = () => {
    this.setState({modal: !this.state.modal});
  };

  handleSubmit = item => {
    this.toggle();
    console.log("save" + JSON.stringify(item));
  };

  handleDelete = item => {
    console.log("delete" + JSON.stringify(item));
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
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
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
