import React, {Component} from "react";
import {Button, Form, FormGroup, Input, Label, Modal, ModalBody, ModalFooter, ModalHeader} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem
    };
  }

  handleChange = e => {
    let {name, value} = e.target;
    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }
    const activeItem = {...this.state.activeItem, [name]: value};
    this.setState({activeItem});
  };

  render() {
    const {toggle, onSave} = this.props;
    return (
      <Modal isOpen={ true } toggle={ toggle }>
        <ModalHeader toggle={ toggle }> Todo Item </ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="title">Title</Label>
              <Input
                type="text"
                name="title"
                value={ this.state.activeItem.title }
                onChange={ this.handleChange }
                placeholder="Enter job title"
              />
            </FormGroup>
            <FormGroup>
              <Label for="description">Description</Label>
              <Input
                type="text"
                name="description"
                value={ this.state.activeItem.description }
                onChange={ this.handleChange }
                placeholder="Enter job description"
              />
            </FormGroup>
            <FormGroup>
              <Label for="status">Status</Label>
              <Input
                type="text"
                name="status"
                value={ this.state.activeItem.status }
                onChange={ this.handleChange }
                placeholder="Enter job status"
              />
            </FormGroup>
            <FormGroup>
              <Label for="company">Company</Label>
              <Input
                type="text"
                name="company"
                value={ this.state.activeItem.company }
                onChange={ this.handleChange }
                placeholder="Enter company"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button color="success" onClick={ () => onSave(this.state.activeItem) }>
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}
