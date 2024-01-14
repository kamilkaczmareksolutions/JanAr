import openai
import os
from PIL import Image
from io import BytesIO
import base64
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve login credentials
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

# Initialize OpenAI client
from openai import OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def check_credentials(username, password):
    return username == LOGIN and password == PASSWORD

# Function to convert image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def analyze_image(image_base64):
    analysis_prompt = "Jesteś ogromnym entuzjastą dzieł sztuki, jesteś laikiem, natomiast na tyle często chodzisz ze swoimi przyjaciółmi na różnego rodzaju spotkania, na wystawy do muzeów, że doskonale rozumiesz co u ciebie, jak i u innych osób wywołuje emocje. Twoim zadaniem jest zerknąć na zdjęcie przedstawiające dzieło w ramie i opowiedzieć co widzisz w sposób bardzo zwięzły i konkretny, ale taki, który będzie mógł wywołać emocje u osoby, która przeczyta twój opis. Bardzo ważne jest, żebyś nie opisywał niczego co jest poza ramą dzieła, to znaczy zachowuj się tak jakby tło w ogóle nie istniało, dla ciebie istnieje tylko wnętrze dzieła. Pamiętaj, że opis ma być krótki i zwięzły (ilość słów: 100-120), ale ma w taki sposób przemawiać do osoby, która go przeczyta, żeby wywołać emocje."

    try:
        response = client.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "user", "content": analysis_prompt},
                {"role": "user", "content": [{"image": image_base64, "resize": 768}]}
            ],
            max_tokens=250
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Function to generate a caption
def generate_caption(image_base64, additional_prompt):
    try:
        # System prompt
        system_prompt = "Jesteś analitykiem dzieł sztuki, który jednocześnie prowadzi profil miejsca, gdzie oprawia się dzieła na Facebooku, więc dobrze rozumiesz, że pisząc jakikolwiek post należy pisać go w taki sposób, aby było to angażujące dla odbiorców. Twoim zadaniem jest skorzystanie z podpowiedzi użytkownika (additional_prompt), aby zrozumieć co jest dla niego najważniejsze oraz wykorzystaniem Twojego własnego doświadczenia do napisania angażującego opisu dzieła sztuki. Może zdarzyć się tak, że użytkownik nie dostarczy Ci żadnego draftu, wtedy postaraj się pisać w taki sposób, aby zachęcić ludzi do podzielenia się swoimi przemyśleniami odnośnie dzieła. Nie używaj hashtagów, nie nadużywaj emotikon, bądź zwięzły i konkretny (ilość słów: 100-120), ale bardzo gładki i delikatny, przyjemny w odbiorze."

        # User prompt
        user_prompt = "Napisz krótki post na Facebooka, który opisze dzieło sztuki, które klient przyniósł do oprawienia w Zakładzie Szklarskim JanAr. Bądź zwięzły, niech wydźwięk posta będzie radosny, unikaj nazbyt poetyckiego i banalnego tonu, nie używaj hashtagów, unikaj zbyt dużej ilości emotikon."

        # Combining system and user prompts
        combined_prompt = system_prompt + user_prompt + additional_prompt

        response = client.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        combined_prompt,
                        {"image": image_base64, "resize": 768}
                    ]
                }
            ],
            max_tokens=250,
            temperature=0.5  # Temperature setting
        )
        return response.choices[0].message.content
    except openai.error.OpenAIError:
        return "Pojawił się problem po stronie AI, poczekaj minutę i spróbuj jeszcze raz."

# New Function to Combine Outputs
def combine_outputs(image_analysis, caption_creation):
    # System prompt
    system_prompt = "Jesteś doskonałym analitykiem, który świetnie potrafi wyważyć, co jest ważne, gdy dostaje dwie informacje z dwóch źródeł. Pracujesz dla JanAr, którzy NIE SĄ galerią sztuki czy wystawą - zajmują się jedynie oprawą obrazów. Potrafisz świetnie znaleźć złoty środek pomiędzy dwoma informacjami. Niezależnie od tego, jakie dostaniesz dane, zawsze wypracujesz świetne połączenie. Będziesz pracował dla dwóch osób, które opisują to samo dzieło sztuki, tylko że jedna z tych osób jest estetą, jest bardziej wizualna, jest wzrokowcem. Druga natomiast wie, w jaki sposób opisywać dzieła sztuki, aby zainteresować odbiorców do zgłębienia dzieła samemu. Wiesz, że ważne jest, aby utrzymać przyjacielski, lekki ton, ale stronisz od banałów i używania jakiejkolwiek ilości hashtagów, czy innego rodzaju przesadzania. Twoim głównym zadaniem jest takie zinterpretowanie dwóch informacji od dwóch osób, aby powstał niezbyt rozległy, zwięzły, fajny i przyjemny w odbiorze post (ilość słów: 100-120)."

    # User prompt with dynamic placeholders filled
    user_prompt = f"Weź dwie dane od użytkowników: poniższą analizę wizualną obrazu: '{image_analysis}', z wygenerowanym opisem: '{caption_creation}', i napisz wersję finalną posta, która powinna odzwierciedlać to co oni napisali, znaleźć pomiędzy tymi dwoma informacjami złoty środek, odpowiednio to wyważyć i podać jako wersję finalną dla odbiorcy. Ważne żeby ton był konwersacyjny, lekki, przyjazny, ale żeby unikać banału i jakiejkolwiek ilości hashtagów. Nie używaj też za dużo emotikon. Po prostu zabrzmij zachęcająco, przyjaźnie i sympatycznie. Pamiętaj, że klienci przynoszą prace, a po oprawieniu zabierają do domu; gotowa praca nie zostaje w JanAr - jest zabierana przez klienta."

    # Combined prompt with filled placeholders
    combined_prompt = f"{system_prompt}\n\n{user_prompt}"

    try:
        response = client.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "system", "content": combined_prompt},
                {"role": "user", "content": combined_prompt}
            ],
            max_tokens=350,
            temperature=0
        )
        return response.choices[0].message.content
    except openai.error.OpenAIError as e:
        return "Pojawił się problem po stronie AI, poczekaj minutę i spróbuj jeszcze raz."

def attempt_login():
    if check_credentials(st.session_state.get('username', ''), st.session_state.get('password', '')):
        st.session_state['authenticated'] = True
    else:
        st.sidebar.error("Nieprawidłowa nazwa użytkownika lub hasło")

def main():
    st.set_page_config(page_title="Generator Podpisów dla JanAra", page_icon=":framed_picture:")

    st.sidebar.title("Uwierzytelnianie")
    st.sidebar.text_input("Nazwa użytkownika", key='username')
    st.sidebar.text_input("Hasło", type="password", key='password')

    if st.sidebar.button("Zaloguj się"):
        attempt_login()

    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if 'uploaded_file' not in st.session_state:
        st.session_state['uploaded_file'] = None

    if st.session_state.get('authenticated', False):
        st.header("Generator Podpisów dla JanAra 🖼️")
        uploaded_file = st.file_uploader("Załaduj obraz", type=["jpg", "jpeg", "png"], key="file_uploader")

        if uploaded_file is not None:
            st.session_state['uploaded_file'] = uploaded_file
            image = Image.open(uploaded_file)
            st.image(image, caption='Załadowany Obraz', use_column_width=True)
            additional_prompt = st.text_area("Dodatkowy kontekst (opcjonalnie)", 
                                             placeholder="Podaj dodatkowy kontekst lub szczegóły odnośnie tej pracy")

        if st.button('Wygeneruj Podpis') and st.session_state.get('uploaded_file', None) is not None:
            with st.spinner('Generowanie podpisu...'):
                image_base64 = image_to_base64(Image.open(st.session_state['uploaded_file']))
                image_analysis = analyze_image(image_base64)
                print("Image Analysis Output:", image_analysis)
                caption_creation = generate_caption(image_base64, additional_prompt)
                print("Caption Creation Output:", caption_creation)
                final_caption = combine_outputs(image_analysis, caption_creation)
                print("Final Caption Output:", final_caption)
                st.write(final_caption)

if __name__ == '__main__':
    main()