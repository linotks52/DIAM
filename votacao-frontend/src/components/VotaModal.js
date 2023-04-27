import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import VotaForm from "./VotaForm";
class VotaModal extends Component {
    state = {
        modal: false
    };
    toggle = () => {
        this.setState(previous => ({
            modal: !previous.modal
        }));
    };
    render() {
        var title = "Votação numa Opção";
        var button = <Button onClick={this.toggle}  color="danger">Voto</Button>;
        return (
            <Fragment>
                {button}
                <Modal isOpen={this.state.modal} toggle={this.toggle}>
                <ModalHeader toggle={this.toggle}>{title}</ModalHeader>
                <ModalBody>
                    <VotaForm
                        resetState={this.props.resetState}
                        toggle={this.toggle}
                        questao={this.props.questao}
                        opcoes={this.props.opcoes}
                    />
                </ModalBody>
                </Modal>
            </Fragment>
        );
    }
}
export default VotaModal;