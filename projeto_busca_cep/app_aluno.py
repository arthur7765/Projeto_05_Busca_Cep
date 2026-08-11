import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####


##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]



##### BARRA LATERAL #####
st.siderbar.title("buscar CEP")
st.siderbar.image("logo.png", width=400)
st.siderbar.write("aplicação para buscar endereço a partir do CEP e mostrar localização no mapa")
escolha = st.siderbar.selectbos("escolha uma opção:, opcoes")

##### BOTÃO BUSCAR CEP #####

if escolha == "bucar CEP":
    st.header("bucar endereço pelo CEP")
    cep = st.text_input("digite o CEP (somente números):")


    if st.button("buscar"):
        if len(cep) != 8 or not cep.isdigit():
            st.error("por favor, insira um CEP válido com 8 dígitos numéricos.")
        else:
            try:
                endereco = BuscarCep.buscar_cep(cep)
                if endereco:
                    st.success("endereço encontrado:")
                    st.write(f"CEP: {endereco[0]}")
                    st.write(f"Endereço: {endereco[1]}")
                    st.write(f"bairro: {endereco[2]}")
                    st.write(f"cidade: {endereco[3]}")
                    st.write(f"estado: {endereco[4]}")

                    ## mapas                           c
                    st.title("localização no mapa")
                    df = pd.DataFrame({"latitude": [endereco[5]], "longitude": [endereco[6]]})
                    st.map(df, zoom=15)
                else:
                    st.error("CEP não encontrdo.")
            except Exception as e:
                st.error(F"ocorreu um erro ao buscar o CEP: {e}")


##### BOTÃO DESCOBRIR CEP #####

elif escolha == "descobrir CEP":
    st.header("descobrir CEP pelo Endereço")
    endereco_usuario = st.text_input("dirite o endereço (ex:rua olga, barueri, sp):")

    if st.button("descobrir"):
        if not endereco_usuario.strip():
            st.error("por favor, insira um endereço válido.")
        else:
            try:
                resultado = BuscarCep.descobrir_cep(endereco_usuario)
                st.success("link de busca no google:")
                st.write(resultado)
            except Exception as e:
                st.error(f"ocorreu um erro ao descobrir o CEP: {e}")