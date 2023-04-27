import React from "react";
import { Button, Form, FormGroup, Table } from "reactstrap";
class DetalheQuestaoForm extends React.Component {
    state = { // (32)
        pk: 0,
        questao_texto: "",
        pub_data: "",
        opcao_set: []
    };
    componentDidMount() { // (33)
        if (this.props.questao) {
            const { pk, questao_texto, pub_data } = this.props.questao;
            this.setState({ pk, questao_texto, pub_data});
        }
        if (this.props.opcoes) { // (34)
            const todasOpcoes = this.props.opcoes;
            const questao = this.props.questao;
            const opcao_set = [];
            for (let i = 0; i < todasOpcoes.length; i++) {
                if (questao.pk === todasOpcoes[i].questao){
                    opcao_set.push(todasOpcoes[i]);
                }
            }
        this.setState({ opcao_set });
        }
    }
    fechaModalQuestao = e => {
        e.preventDefault();
        this.props.toggle();
    };
    defaultIfEmpty = value => {
        return value === "" ? "" : value;
    };
    render() { // (35)
        return (
            <Form onSubmit={this.fechaModalQuestao}>
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
                                <th colSpan="6" align="right">Votos</th>
                                <th></th>
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
                                        {opcao.opcao_texto}
                                    </td>
                                    <td colSpan="6" align="right">
                                        {opcao.votos}
                                    </td>
                                </tr>
                            ))
                            }
                        </tbody>
                    </Table>
                </FormGroup>
                <Button>Fechar</Button> {/* (37) */}
            </Form>
        );
    }
}
export default DetalheQuestaoForm;