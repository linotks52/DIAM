import React from "react";
import { Button, Form, FormGroup, Table } from "reactstrap";
import axios from "axios";
import { API_URL_OPCOES } from "../constants";
class VotaForm extends React.Component {
    state = {
            pk: 0,
            questao_texto: "",
            pub_data: "",
            opcao_set: [],
            selectedOption: 0 // (38)
    };
    componentDidMount() {
        if (this.props.questao) {
            const { pk, questao_texto, pub_data } = this.props.questao;
            this.setState({ pk, questao_texto, pub_data});
        }
        if (this.props.opcoes) {
            const todasOpcoes = this.props.opcoes;
            const questao = this.props.questao;
            const opcao_set = [];
            for (let i = 0; i < todasOpcoes.length; i++) {
                if (questao.pk === todasOpcoes[i].questao){
                    opcao_set.push(todasOpcoes[i]);
                }
        }
        this.setState({ opcao_set });}
    }
    onChange = e => {
        this.setState({ [e.target.name]: e.target.value });
    };
    votaEFechaModal = e => { // (41)
        e.preventDefault();
        for(let i=0; i<this.props.opcoes.length; i++){
            if(this.props.opcoes[i].pk == this.state.selectedOption){
                axios.put(API_URL_OPCOES + this.props.opcoes[i].pk,{'pk':
                this.props.opcoes[i].pk, 'questao': this.props.opcoes[i].questao,  'opcao_texto':  this.props.opcoes[i].opcao_texto, 'votos':  this.props.opcoes[i].votos++} );
            }
        }
    this.props.toggle();
    };
    defaultIfEmpty = value => {
        return value === "" ? "" : value;
    };
    handleOptionChange = changeEvent => { // (40)
        const optionid = changeEvent.target.value;
        this.state.selectedOption = optionid;
        };
    render() {
        return (
            <Form onSubmit={this.votaEFechaModal}>
                <FormGroup>
                    <b>Texto:</b>
                    <p>{this.defaultIfEmpty(this.state.questao_texto)} </p>
                </FormGroup>
                <FormGroup>
                    <b>Data de publicação:</b> &nbsp;
                    <p>{this.defaultIfEmpty(this.state.pub_data)}</p>
                </FormGroup>
                <FormGroup>
                    <Table>
                        <thead>
                            <tr>
                                <th colSpan="6" align="left">Opção</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                            !this.state.opcao_set || this.state.opcao_set.length <= 0 ? (
                                <tr>
                                    <td colSpan="14" align="left">
                                        <i>Não há opções</i>
                                    </td>
                                </tr>
                            ) : (
                            this.state.opcao_set.map((opcao) =>
                                <tr>
                                    <td colSpan="6" align="left">
                                    &nbsp;&nbsp;
                                        <label>
                                            <input
                                                type="radio"
                                                name="react-radio"
                                                value={opcao.pk}
                                                checked={false}
                                                className="form-check-input"
                                                onChange={this.handleOptionChange}
                                            />
                                            &nbsp;&nbsp;{opcao.opcao_texto}
                                        </label>
                                    </td>
                                </tr>
                            ))
                            }
                        </tbody>
                    </Table>
                </FormGroup>
            <Button>Votar</Button>
        </Form>
    );
}
}
export default VotaForm;