import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import DetalheQuestaoForm from "./DetalheQuestaoForm";
class DetalheQuestaoModal extends Component {
    state = {
        modal: false // (25)
    };
    toggle = () => { // (26)
        this.setState(previous => ({
            modal: !previous.modal
        }));
    };
    render() {
        var title = "Detalhe de uma Questão";
        var button = <Button onClick={this.toggle}  color="warning">Detalhe</Button>; // (27)
        return (
            <Fragment>
            {button} {/*(28)*/}
            <Modal isOpen={this.state.modal} toggle={this.toggle}>
                <ModalHeader toggle={this.toggle}>{title}</ModalHeader>
                    <ModalBody> {/* (31) */}
                        <DetalheQuestaoForm
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
export default DetalheQuestaoModal;