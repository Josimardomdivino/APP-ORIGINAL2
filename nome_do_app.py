import streamlit as st
from gsheets import add_dado, listar_dados

st.title("👥 Cadastro de Sócios")

st.subheader("📝 Preencha os dados do sócio")

with st.form("form_dados"):
    nome = st.text_input("Nome Completo")
    cpf = st.text_input("CPF")
    nascimento = st.date_input("Data de Nascimento")
    comunidade = st.text_input("Comunidade de Origem")
    telefone = st.text_input("Telefone")
    categoria = st.selectbox("Categoria de Sócio", ["Efetivo", "Contribuinte", "Honorário"])
    enviar = st.form_submit_button("Salvar")

    if enviar:
        if nome and cpf and comunidade:
            add_dado(nome, cpf, nascimento.strftime("%d/%m/%Y"), comunidade, telefone, categoria)
            st.success("Sócio cadastrado com sucesso!")
        else:
            st.warning("Preencha todos os campos obrigatórios.")

st.subheader("📋 Sócios Cadastrados")
dados = listar_dados()

if dados:
    for d in dados:
        st.write(
            f"👤 **{d.get('nome')}** | CPF: {d.get('cpf')} | Nasc.: {d.get('nascimento')} | "
            f"Comunidade: {d.get('comunidade')} | Tel: {d.get('telefone')} | Categoria: {d.get('categoria')}"
        )
else:
    st.info("Nenhum sócio cadastrado ainda.")