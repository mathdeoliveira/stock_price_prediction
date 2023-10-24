import os
import sys

import matplotlib.pyplot as plt
import replicate
import streamlit as st

sys.path.append(os.path.join(os.path.dirname(__file__), "../training_model"))

from predict import Predict

# App title
st.set_page_config(page_title="Assistente na tomada de decisão")

# Replicate Credentials
with st.sidebar:
    st.title("Assistente na tomada de decisão")
    st.markdown("☑️ Crie conta no [Replicate](https://replicate.com/signin/)!")
    st.markdown(
        "💻 Acesse o código no [GitHub](https://github.com/mathdeoliveira/stock_price_prediction)!"
    )

replicate_api = st.text_input("Entrar com a API Key do Replicate:", type="password")
if not (replicate_api.startswith("r8_") and len(replicate_api) == 40):
    st.warning("Por favor, entrar key das suas credenciais.", icon="⚠️")
else:
    st.success("Sucesso!", icon="✅")
    os.environ["REPLICATE_API_TOKEN"] = replicate_api

    if st.button("Gerar recomendação de compra"):
        with st.spinner("Perguntando à Inteligência Artificial..."):
            pred = Predict()
            real_last_ten_dates, predicted_last_ten_dates = pred.predict()

            prompt_input = f"""Quero que você atue como um analista de investimento e evite termos muito técnicos e responda a seguinte questão.
            Contexto: um modelo de regressão linear simples (Lasso) é usado prever o valor das ações da empresa com ticker JPM, dado os preços das ações dos ticks BAC, WFC, DEXUSUK, DEXUSEU, SP500 , DJIA e VIXCLS. O intuito é entender se o próximo dia útil o preço da ação do JPM vai aumentar ou cair.
            Questão: Dados os dados reais e preditos abaixo dos últimos dez dias, descreva uma análise de risco e lucratividade sobre o a predição, dado o cenário da predição ao fim da resposta sugira ou não a compra da ação para o próximo dia.  
            dia 1:  {real_last_ten_dates.iloc[0]}
            dia 2:  {real_last_ten_dates.iloc[1]}
            dia 3:  {real_last_ten_dates.iloc[2]}
            dia 4:  {real_last_ten_dates.iloc[3]}
            dia 5:  {real_last_ten_dates.iloc[4]}
            dia 6:  {real_last_ten_dates.iloc[5]}
            dia 7:  {real_last_ten_dates.iloc[6]}
            dia 8:  {real_last_ten_dates.iloc[7]}
            dia 9:  {real_last_ten_dates.iloc[8]}
            dia 10: {real_last_ten_dates.iloc[9]}
            preço predito pelo modelo de JPM para os próximo dez dias:  
            dia 1:  {predicted_last_ten_dates.iloc[0]}
            dia 2:  {predicted_last_ten_dates.iloc[1]}
            dia 3:  {predicted_last_ten_dates.iloc[2]}
            dia 4:  {predicted_last_ten_dates.iloc[3]}
            dia 5:  {predicted_last_ten_dates.iloc[4]}
            dia 6:  {predicted_last_ten_dates.iloc[5]}
            dia 7:  {predicted_last_ten_dates.iloc[6]}
            dia 8:  {predicted_last_ten_dates.iloc[7]}
            dia 9:  {predicted_last_ten_dates.iloc[8]}
            dia 10: {predicted_last_ten_dates.iloc[9]}"""
            response = replicate.run(
                "a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
                input={
                    "prompt": f"{prompt_input}",
                    "temperature": 0.75,
                    "top_p": 1,
                    "max_length": 2200,
                    "repetition_penalty": 1,
                },
            )
            full_response = ""
            for item in response:
                full_response += item
            st.success("Sucesso, gerando o resultado!", icon="✅")

        st.header("Sugestão para a tomada de decisão", divider="gray")
        st.write(f"{full_response}")

        st.header(
            "Gráfico dos dados reais e previsões dos últimos dez dias", divider="gray"
        )
        fig, ax = plt.subplots(figsize=(12, 3))
        predicted_last_ten_dates.index = real_last_ten_dates.index
        ax.plot(real_last_ten_dates, "r", label="True Values")
        ax.plot(predicted_last_ten_dates, "b--", label="Predicted Values")
        ax.legend()
        st.pyplot(fig)
