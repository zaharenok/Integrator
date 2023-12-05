import json
import random
import streamlit as st

with open('questions.json') as file:
    questions = json.load(file)

def r():
    x = random.randint(1, 111)
    print(x)
    return x

def pick_a_question():
    question = questions['questions'][r()]
    print(question)
    return question


def main():
    st.set_page_config(page_title='Allgemeines Orientierungswissen über Österreich', page_icon=':books:')
    st.header('Generate the Question :books:')
    
    if st.button('Click Me to Get a Question'):
        letter = ['A ', 'B ', 'C ']
        question = pick_a_question()
        st.write('')
        st.markdown(f"***{question['question_text']}***")
        st.write('')

        numbers = len(question['options'])

        right_answer_number = None

        for i in range(0, numbers):
            if question['options'][i]['is_correct']:
                right_answer_number = i

        col1, col2 = st.columns([0.05, 0.95])

        with col1:
            for i in range(0, numbers):
                if st.button(letter[i]):
                    # Проверяем, является ли выбранный ответ правильным
                    if i == right_answer_number:
                        st.success("Отлично, вы выбрали правильный ответ!")
                    else:
                        st.error("Неправильный ответ. Попробуйте еще раз.")
                        st.info(f"Подсказка: {question['solution']}")


        with col2:
            for i in range(0, numbers):
                st.markdown(question['options'][i]['option_text'])
                st.write('')
        
        st.write(f"Правильный ответ {letter[right_answer_number]}")


if __name__ == '__main__':
    main()