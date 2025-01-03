
import streamlit as st

# Define the data for the holding and its companies
companies = {
    "Remap de Câmbio RJ": "Especializada em reprogramação de câmbios automáticos e automatizados.",
    "WB Training": "Treinamento esportivo e personal trainer, métodos de treino presencial e online.",
    "WB Suplementos": "Loja online de suplementos nutricionais.",
    "WB Nutri Power": "Nutrição personalizada para saúde e emagrecimento.",
    "WB Shaper": "Tratamento estético para melhorar a qualidade dérmica.",
    "WB Mind Health": "Equilíbrio mental para alcançar objetivos pessoais.",
    "WB Sx Health": "Saúde sexual com exercícios, sexologia e mentoria tântrica."
}

# Application title
st.title("Estrutura da WB Performance Holding")

# Introduction
st.write(
    "Bem-vindo à apresentação interativa da WB Performance Holding. "
    "Explore as empresas e seus objetivos abaixo."
)

# Sidebar for navigation
st.sidebar.title("Navegação")
selected_company = st.sidebar.radio("Selecione uma empresa:", ["Visão Geral"] + list(companies.keys()))

# Main content
if selected_company == "Visão Geral":
    st.header("WB Performance Holding")
    st.write(
        "A WB Performance Holding é um conglomerado focado em performance humana e automotiva. "
        "Ela engloba diversas empresas especializadas em áreas específicas, como treinamento, nutrição, estética, "
        "e saúde sexual, além de reprogramação de câmbios automáticos."
    )
    st.write(
        "Selecione uma empresa no menu à esquerda para explorar seus objetivos específicos."
    )
else:
    st.header(selected_company)
    st.write(companies[selected_company])

# Footer
st.write("---")
st.write("Aplicação criada para organizar e explorar a estrutura da WB Performance Holding.")
