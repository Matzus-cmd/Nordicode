# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, en donde la primera pagina ira la bibliografia, la segunda iran las estadisticas del jugador y en la ultima estará el cuestionario como un juego

# Creamos la lista de páginas
paginas = ['Inicio (biografia, mapa y descripcion)', 'Datos extra (gráficos)', 'Cuestionario (juego)']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona la sección que deseas ver', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio (biografia, mapa y descripcion)':
 # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>Nordicode</h1>", unsafe_allow_html=True)

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)
    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen del jugador
    col1.image("foto_perfil.jpg", caption='foto de perfil', width=300)

    texto = """El diseño está dedicado al jugador Erling Haaland, destacado delantero del Manchester City en la Premier League. Esta plataforma digital ofrecerá información completa y organizada sobre su biografía, estadísticas y logros deportivos durante la temporada 24/25 de la Premier League.
    """

    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Equipaciones de Haaland (clubes) </h2>", unsafe_allow_html=True)
    
    col3, col4, col5, col6 = st.columns(4)
    col3.image("dorsal_mncity_delante.jpg", caption='Dorsal del Manchester City (delante)', width=300)
    col5.image("dorsal_mncity_atras.jpg", caption='Dorsal del Manchester City (atrás)', width=300)
    texto2 = """Se incorporó oficialmente al equipo en julio de 2022 y firmó un contrato que le daría para jugar hasta junio de 2027.
    ____________________________________________________________________________________________
    """
    st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto2}</div>", unsafe_allow_html=True)

    col7, col8, col9, col10 = st.columns (4)
    col7.image("dorsal_alternativo_delante.jpg", caption='Dorsal alternativo del Manchester City (delante)', width=300)
    col9.image("dorsal_alternativo_atras.jpg", caption='Dorsal alternativo del Manchester City (atrás)', width=300)

    texto3 = """La camiseta alternativa del Manchester City para la temporada 2024/25 rinde homenaje a la histórica equipación de visitante de la temporada 1998/99, que usaron cuando ascendieron de la tercera a la segunda división inglesa
    ____________________________________________________________________________________________
    """
    st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto3}</div>", unsafe_allow_html=True)

    col11, col12, col13, col14 = st.columns (4)
    col11.image("camiseta_dortmund.jpg", caption='Camiseta del Borussia Dortmund', width=300)
    col13.image("camiseta_salzburgo.jpg", caption='Camiseta del Red Bull Salzburg', width=300)

    texto4 = """Tuvo un contrato con el Dortmund desde enero de 2020 hasta junio de 2022. Pero anteriormente, su club fue el Salzburg, jugando desde el enero de 2019 y lo dejó en diciembre del mismo año. Desde su primera temporada fue un destacado delantero dentro de la Premier League.
    ____________________________________________________________________________________________
    """
    st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto4}</div>", unsafe_allow_html=True)

    col15, col16, col17, col18, col19  = st.columns (5)
    col16.image("camiseta_selección.jpg", caption='Camiseta de la selección de Noruega', width=300)

    texto5 = """-------------Debutó con la selección absoluta de Noruega el 5 de septiembre de 2019. Gracias a él y al esfuerzo en conjunto de la selección noruega, lograron obtener un cupo para el campeonato mundial del 2026.-----------------
    
"""
    st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto5}</div>", unsafe_allow_html=True)

        # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>Mejores jugadas del jugador Erling Haaland 24/25 </h2>", unsafe_allow_html=True)
    
    # Agregamos el link del video
    st.video("https://www.youtube.com/watch?v=NlDSD1PVv5k")


elif  pagina_seleccionada == 'Datos extra (gráficos)':
    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'> Conociendo más a Haaland (origen y desempeño) </h1>", unsafe_allow_html=True)
    # Agregar un  texto para la respuesta
    texto_2 = "En esta sección se profundizará en los datos tanto futbolísticos como poco sabidos de Erling Haaland, como su país de origen y estadístiscas de la temporada 24-25. Luego de revisar esta información, estarán listos para medir sus conocimientos en nuestra trivia en la 3°era sección de Nordicorde"
    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

        # Creamos una lista de gráficos
    graficos = ['¿Noruego o Inglés? La verdadera nacionalidad de Haaland', '¿En qué estadios jugo Haaland en la temporada 24/25', 'Estadísticas como delantero y goleador']

 # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Elige una sección y conoce más de Haaland aquí:', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == '¿Noruego o Inglés? La verdadera nacionalidad de Haaland':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El lugar de nacimiento de Erling Haaland es Leeds, Inglaterra, Reino Unido. Nació allí el 21 de julio de 2000, mientras su padre, Alf-Inge Haaland, jugaba para el Leeds United en la Premier League. Sin embargo, su nacionalidad es noruega, ya que su familia regresó a Noruega (a la ciudad de Bryne) cuando él tenía alrededor de tres años.", unsafe_allow_html=True)
        import streamlit.components.v1 as components
        with open("mapa.origen_haaland.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass
        pass
    elif grafico_seleccionado == '¿En qué estadios jugo Haaland en la temporada 24/25':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Durante su temporada 2024-2025 de la Premier League, Haaland junto con sus compañeros del Manchester City visitaron diversos estadios a lo largo del territorio inglés de Reino Unido. Este mapa interactivo muestra información sobre el estadio, la modalidad y la fecha del partido.</div>", unsafe_allow_html=True)
        import streamlit.components.v1 as components
        with open("mapa.estadios_mncity.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass
        pass
    elif grafico_seleccionado == 'Estadísticas como delantero y goleador':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico es un histograma de frecuencia que muestra cuántos goles marcó Erling Haaland en distintos partidos durante la temporada de la Premier League especificada. En el eje horizontal (X) tenemos la cantidad de goles (0, 1, 2, 3) y en el eje vertical (Y) la cantidad de partidos en los que ocurrió ese evento.</div>", unsafe_allow_html=True)
        st.image("histograma_goles_haaland.png", caption='Goles por cantidad de partidos (24/25)', width=500)
        pass

else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'> La Trivia Nórdica </h1>", unsafe_allow_html=True)

import random

# 1. Prepare Trivia Questions with multiple-choice options
trivia_questions = [
    {
        'question': '¿Cuál es el nombre completo de Erling Haaland?',
        'options': ['Erling Braut Haaland', 'Erling Ragnar Haaland', 'Erling Magnus Haaland', 'Erling Karl Haaland'],
        'correct_answer_index': 0, # Index of the correct answer in the 'options' list
        'type': 'string'
    },
    {
        'question': '¿En qué país nació Erling Haaland?',
        'options': ['Suecia', 'Noruega', 'Dinamarca', 'Finlandia'],
        'correct_answer_index': 1,
        'type': 'string'
    },
    {
        'question': '¿Cuál es el club actual de Erling Haaland?',
        'options': ['Real Madrid', 'Barcelona', 'Manchester City', 'Bayern Múnich'],
        'correct_answer_index': 2,
        'type': 'string'
    },
    {
        'question': '¿Cuál es el número de camiseta de Erling Haaland en el Manchester City?',
        'options': ['7', '9', '10', '11'],
        'correct_answer_index': 1,
        'type': 'number'
    },
    {
        'question': '¿En qué año nació Erling Haaland?',
        'options': ['1999', '2000', '2001', '2002'],
        'correct_answer_index': 1,
        'type': 'number'
    },
    {
        'question': '¿Cuál es la posición principal de Haaland en el campo de fútbol?',
        'options': ['Defensa', 'Mediocampista', 'Delantero', 'Portero'],
        'correct_answer_index': 2,
        'type': 'string'
    }
]

def run_trivia_game():
    global trivia_questions
    score = 0
    # Shuffle questions at the start of each game
    random.shuffle(trivia_questions)

    print("¡Bienvenido al juego de Trivia de Haaland!")
    print("Responde las siguientes preguntas. Solo puedes seleccionar una opción.")
    print("---------------------------------------------------")

    for i, q_data in enumerate(trivia_questions):
        print(f"\nPregunta {i + 1}/{len(trivia_questions)}:")
        print(q_data['question'])

        # Display options with numbers
        for j, option in enumerate(q_data['options']):
            print(f"{j + 1}. {option}")

        user_choice = -1
        while True:
            try:
                user_input = input("Selecciona el número de tu respuesta: ").strip()
                user_choice = int(user_input) - 1 # Convert to 0-indexed
                if 0 <= user_choice < len(q_data['options']):
                    break
                else:
                    print("¡Opción inválida! Por favor, ingresa un número dentro del rango de opciones.")
            except ValueError:
                print("¡Entrada inválida! Por favor, ingresa un número.")

        if user_choice == q_data['correct_answer_index']:
            print("¡Correcto!")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {q_data['options'][q_data['correct_answer_index']]}")
        print("---------------------------------------------------")

    print(f"\n¡Juego terminado! Tu puntuación final es: {score} de {len(trivia_questions)} preguntas.")
    if score == len(trivia_questions):
        print("¡Felicidades! ¡Perfecto!")
    elif score > len(trivia_questions) / 2:
        print("¡Buen trabajo!")
    else:
        print("Puedes mejorar. ¡Inténtalo de nuevo!")
    
    # Allow playing again
    play_again = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    if play_again == 'si':
        run_trivia_game() # Recursively call to play again

# Run the game
run_trivia_game()

    
    

    